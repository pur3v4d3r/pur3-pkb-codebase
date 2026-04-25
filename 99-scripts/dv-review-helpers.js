// ═══════════════════════════════════════════════════════════════════════════
// dv-review-helpers.js
// Shared DataviewJS helper module for the Review Dashboard.
// Loaded via:
//     const code = await dv.io.load("99-scripts/dv-review-helpers.js");
//     const REVIEW = (new Function("dv", code + "\nreturn REVIEW;"))(dv);
//
// All functions are tolerant of missing frontmatter fields. The vault's
// permanent notes do not yet have `last-reviewed` / `review-frequency` /
// `importance` / `mastery-stage`, so a fallback chain is used:
//     last-reviewed  →  updated  →  file.mtime
// Status bucket and confidence are read from `status` and `confidence`.
// ═══════════════════════════════════════════════════════════════════════════

var REVIEW = (function () {

    // ── Config ───────────────────────────────────────────────────────────
    var FREQ_DAYS = {
        daily: 1, weekly: 7, biweekly: 14, monthly: 30,
        quarterly: 90, biannual: 180, semiannual: 180,
        yearly: 365, annual: 365
    };

    // Default review window if no `review-frequency` field is present.
    var DEFAULT_WINDOW_DAYS = 90;

    // Frontmatter fields treated as outbound relations for density math.
    var RELATIONAL_FIELDS = [
        "related", "prerequisites", "specializes", "broader", "see-also",
        "contrasts-with", "contradicts", "applies-to", "formalizes",
        "instance-of", "supports", "refines"
    ];

    // ── Date helpers ─────────────────────────────────────────────────────
    function _toDate(v) {
        if (v == null) return null;
        // Already a Luxon DateTime (Dataview parses YAML dates this way)
        if (typeof v === "object" && typeof v.isValid === "boolean") {
            return v.isValid ? v : null;
        }
        // String → try to parse
        try {
            var d = dv.date(v);
            return (d && d.isValid) ? d : null;
        } catch (e) { return null; }
    }

    function _daysBetween(d) {
        if (!d) return Infinity;
        try {
            return Math.floor(dv.date("now").diff(d, "days").days);
        } catch (e) { return Infinity; }
    }

    function _lastTouched(p) {
        return _toDate(p["last-reviewed"])
            || _toDate(p.updated)
            || _toDate(p.file.mtime)
            || null;
    }

    function daysSinceReview(p) { return _daysBetween(_lastTouched(p)); }
    function daysSinceUpdate(p) {
        return _daysBetween(_toDate(p.updated) || _toDate(p.file.mtime));
    }
    function daysSinceCreation(p) {
        return _daysBetween(_toDate(p.created) || _toDate(p.file.ctime));
    }

    // ── Review window / overdue ──────────────────────────────────────────
    function reviewWindow(p) {
        var f = (p["review-frequency"] || "").toString().toLowerCase().trim();
        return FREQ_DAYS[f] || DEFAULT_WINDOW_DAYS;
    }

    function overdueRatio(p) {
        var d = daysSinceReview(p);
        if (d === Infinity) return Infinity;
        return d / reviewWindow(p);
    }

    function isOverdue(p) { return overdueRatio(p) > 1; }

    // ── Relations / centrality ───────────────────────────────────────────
    function _isLiveLink(v) {
        return v && typeof v === "object" && v.path && String(v.path).trim().length > 0;
    }

    function outboundRelations(p) {
        var perField = {};
        var total = 0;
        for (var i = 0; i < RELATIONAL_FIELDS.length; i++) {
            var f = RELATIONAL_FIELDS[i];
            var v = p[f];
            if (!v) { perField[f] = 0; continue; }
            var arr = Array.isArray(v) ? v : [v];
            var n = 0;
            for (var j = 0; j < arr.length; j++) {
                if (_isLiveLink(arr[j])) n++;
            }
            perField[f] = n;
            total += n;
        }
        return { total: total, perField: perField };
    }

    function relationalDensity(p) {
        var inb = (p.file && p.file.inlinks && p.file.inlinks.length) || 0;
        return inb + outboundRelations(p).total;
    }

    function isHub(p, threshold) {
        if (threshold == null) threshold = 8;
        return relationalDensity(p) >= threshold;
    }

    function isOrphan(p) {
        var inb = (p.file && p.file.inlinks && p.file.inlinks.length) || 0;
        var out = (p.file && p.file.outlinks && p.file.outlinks.length) || 0;
        var rel = outboundRelations(p).total;
        return (inb + out + rel) === 0;
    }

    // ── Status bucket ────────────────────────────────────────────────────
    function statusBucket(p) {
        var s = (p.status || p.maturity || p["mastery-stage"] || "").toString().toLowerCase().trim();
        if (!s) return "unspecified";
        if (s === "stub") return "seedling";
        return s;
    }

    // ── Importance ───────────────────────────────────────────────────────
    function importanceWeight(p) {
        var i = (p.importance || "").toString().toLowerCase().trim();
        if (i === "critical") return 4;
        if (i === "high") return 3;
        if (i === "medium") return 2;
        if (i === "low") return 1;
        return 0;
    }

    function statusWeight(p) {
        // Older / more mature notes worth more attention when overdue
        switch (statusBucket(p)) {
            case "evergreen": return 2.0;
            case "enriched":  return 1.5;
            case "budding":   return 1.0;
            case "seedling":  return 0.5;
            case "wilting":   return 1.5;
            default:          return 0.7;
        }
    }

    // ── Composite priority score ─────────────────────────────────────────
    // Weights:
    //   overdue ratio × 5
    //   log(1 + density) × 1.5     (centrality)
    //   importance weight × 1.5
    //   status weight × 1
    //   #needs-review tag → +3 flat
    function priorityScore(p) {
        var ratio = overdueRatio(p);
        var ratioComp = (ratio === Infinity) ? 5 : Math.min(ratio, 5);
        var dens = Math.log(1 + relationalDensity(p));
        var imp = importanceWeight(p);
        var stat = statusWeight(p);

        var tags = (p.file && p.file.tags) || [];
        var flagged = false;
        for (var i = 0; i < tags.length; i++) {
            if (String(tags[i]).toLowerCase() === "#needs-review") { flagged = true; break; }
        }

        var score = (ratioComp * 5) + (dens * 1.5) + (imp * 1.5) + stat;
        if (flagged) score += 3;
        return score;
    }

    // ── Badges (display helpers) ─────────────────────────────────────────
    function ageBadge(d) {
        if (d === Infinity || d == null) return "—";
        if (d < 7)   return "🟢 " + d + "d";
        if (d < 30)  return "🟡 " + d + "d";
        if (d < 90)  return "🟠 " + d + "d";
        if (d < 180) return "🔴 " + d + "d";
        return "🟣 " + d + "d";
    }

    function ratioBadge(r) {
        if (r === Infinity) return "🆕 never";
        if (r <= 1)   return "✅ " + r.toFixed(1) + "×";
        if (r <= 1.5) return "🟡 " + r.toFixed(1) + "×";
        if (r <= 2.5) return "🟠 " + r.toFixed(1) + "×";
        if (r <= 4)   return "🔴 " + r.toFixed(1) + "×";
        return "🟣 " + r.toFixed(1) + "×";
    }

    function priorityBadge(score) {
        if (score >= 25) return "🔥🔥🔥";
        if (score >= 18) return "🔥🔥";
        if (score >= 12) return "🔥";
        if (score >= 6)  return "•";
        return " ";
    }

    // ── Public API ───────────────────────────────────────────────────────
    return {
        FREQ_DAYS: FREQ_DAYS,
        RELATIONAL_FIELDS: RELATIONAL_FIELDS,
        DEFAULT_WINDOW_DAYS: DEFAULT_WINDOW_DAYS,

        daysSinceReview: daysSinceReview,
        daysSinceUpdate: daysSinceUpdate,
        daysSinceCreation: daysSinceCreation,

        reviewWindow: reviewWindow,
        overdueRatio: overdueRatio,
        isOverdue: isOverdue,

        outboundRelations: outboundRelations,
        relationalDensity: relationalDensity,
        isHub: isHub,
        isOrphan: isOrphan,

        statusBucket: statusBucket,
        importanceWeight: importanceWeight,
        statusWeight: statusWeight,
        priorityScore: priorityScore,

        ageBadge: ageBadge,
        ratioBadge: ratioBadge,
        priorityBadge: priorityBadge
    };
})();
