import subprocess, glob, os
base = r"D:\10_pur3v4d3r's-vault\999-report-organizing\_extractor-output\_synthetic-seeds"
dirs = sorted(d for d in glob.glob(os.path.join(base, '2026-04-26-custom-*')) if os.path.isdir(d))
for d in dirs:
    r = subprocess.run(['python', 'synth_seed_builder.py', 'validate', d], capture_output=True, text=True)
    blob = r.stdout + r.stderr
    summary = [l for l in blob.splitlines() if 'Validation summary' in l]
    print(f'{os.path.basename(d):60s} rc={r.returncode}  {summary[0] if summary else blob.strip()[-100:]}')
