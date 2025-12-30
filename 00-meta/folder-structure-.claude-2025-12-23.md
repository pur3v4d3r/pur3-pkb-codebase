
[[2025-12-23]] -> Folder Structure for .claude



Folder PATH listing for volume PUR3V4D3R
Volume serial number is A02C-333C
D:\10_PUR3V4D3R'S-VAULT\.CLAUDE
|   CLAUDE.md
|   GEMINI.md
|   manifest.json
|   settings.json
|   settings.local.json
|   SYSTEM_INIT.md
|
\---__LOCAL-REPO
    +---.claude-plugin
    |       marketplace.json
    |
    +---_possible-memory-system-for-pkb
    |   \---claude-mem-main
    |       |   .gitignore
    |       |   .mcp.json
    |       |   .translation-cache.json
    |       |   CHANGELOG.md
    |       |   CLAUDE.md
    |       |   LICENSE
    |       |   package.json
    |       |   README.md
    |       |   tsconfig.json
    |       |   vitest.config.ts
    |       |
    |       +---.claude
    |       |   |   settings.json
    |       |   |
    |       |   +---agents
    |       |   |       github-morning-reporter.md
    |       |   |
    |       |   \---skills
    |       |       |   CLAUDE.md
    |       |       |
    |       |       \---version-bump
    |       |           |   SKILL.md
    |       |           |
    |       |           \---operations
    |       |                   reference.md
    |       |                   scenarios.md
    |       |                   workflow.md
    |       |
    |       +---.claude-plugin
    |       |       marketplace.json
    |       |
    |       +---.github
    |       |   |   FUNDING.yml
    |       |   |
    |       |   +---ISSUE_TEMPLATE
    |       |   |       bug_report.md
    |       |   |       feature_request.md
    |       |   |
    |       |   \---workflows
    |       |           claude-code-review.yml
    |       |           claude.yml
    |       |           convert-feature-requests.yml
    |       |           summary.yml
    |       |
    |       +---docs
    |       |   +---context
    |       |   |       agent-sdk-v2-preview.md
    |       |   |
    |       |   \---public
    |       |       |   architecture-evolution.mdx
    |       |       |   beta-features.mdx
    |       |       |   claude-mem-logo-for-dark-mode.webp
    |       |       |   claude-mem-logo-for-light-mode.webp
    |       |       |   claude-mem-logomark.webp
    |       |       |   CLAUDE.md
    |       |       |   cm-preview.gif
    |       |       |   configuration.mdx
    |       |       |   context-engineering.mdx
    |       |       |   development.mdx
    |       |       |   docs.json
    |       |       |   endless-mode.mdx
    |       |       |   hooks-architecture.mdx
    |       |       |   installation.mdx
    |       |       |   introduction.mdx
    |       |       |   platform-integration.mdx
    |       |       |   progressive-disclosure.mdx
    |       |       |   trendshift-badge-dark.svg
    |       |       |   trendshift-badge.svg
    |       |       |   troubleshooting.mdx
    |       |       |
    |       |       +---architecture
    |       |       |       database.mdx
    |       |       |       hooks.mdx
    |       |       |       overview.mdx
    |       |       |       pm2-to-bun-migration.mdx
    |       |       |       search-architecture.mdx
    |       |       |       worker-service.mdx
    |       |       |
    |       |       \---usage
    |       |               claude-desktop.mdx
    |       |               export-import.mdx
    |       |               getting-started.mdx
    |       |               private-tags.mdx
    |       |               search-tools.mdx
    |       |
    |       +---plugin
    |       |   |   .mcp.json
    |       |   |   package.json
    |       |   |
    |       |   +---.claude-plugin
    |       |   |       plugin.json
    |       |   |
    |       |   +---hooks
    |       |   |       hooks.json
    |       |   |
    |       |   +---scripts
    |       |   |       cleanup-hook.js
    |       |   |       context-generator.cjs
    |       |   |       context-hook.js
    |       |   |       mcp-server.cjs
    |       |   |       new-hook.js
    |       |   |       save-hook.js
    |       |   |       smart-install.js
    |       |   |       summary-hook.js
    |       |   |       user-message-hook.js
    |       |   |       worker-cli.js
    |       |   |       worker-service.cjs
    |       |   |       worker-wrapper.cjs
    |       |   |
    |       |   +---skills
    |       |   |   |   mem-search.zip
    |       |   |   |
    |       |   |   +---mem-search
    |       |   |   |   |   SKILL.md
    |       |   |   |   |
    |       |   |   |   +---operations
    |       |   |   |   |       .gitkeep
    |       |   |   |   |       by-concept.md
    |       |   |   |   |       by-file.md
    |       |   |   |   |       by-type.md
    |       |   |   |   |       common-workflows.md
    |       |   |   |   |       formatting.md
    |       |   |   |   |       help.md
    |       |   |   |   |       observations.md
    |       |   |   |   |       prompts.md
    |       |   |   |   |       recent-context.md
    |       |   |   |   |       sessions.md
    |       |   |   |   |       timeline-by-query.md
    |       |   |   |   |       timeline.md
    |       |   |   |   |
    |       |   |   |   \---principles
    |       |   |   |           .gitkeep
    |       |   |   |           anti-patterns.md
    |       |   |   |           progressive-disclosure.md
    |       |   |   |
    |       |   |   \---troubleshoot
    |       |   |       |   SKILL.md
    |       |   |       |
    |       |   |       \---operations
    |       |   |               automated-fixes.md
    |       |   |               common-issues.md
    |       |   |               database.md
    |       |   |               diagnostics.md
    |       |   |               reference.md
    |       |   |               worker.md
    |       |   |
    |       |   \---ui
    |       |       |   claude-mem-logo-for-dark-mode.webp
    |       |       |   claude-mem-logomark.webp
    |       |       |   icon-thick-completed.svg
    |       |       |   icon-thick-investigated.svg
    |       |       |   icon-thick-learned.svg
    |       |       |   icon-thick-next-steps.svg
    |       |       |   viewer-bundle.js
    |       |       |   viewer.html
    |       |       |
    |       |       \---assets
    |       |           \---fonts
    |       |                   monaspace-radon-var.woff
    |       |                   monaspace-radon-var.woff2
    |       |
    |       +---private
    |       |   |   POSTMORTEM-worker-debug-failure.md
    |       |   |
    |       |   \---docs
    |       |       \---context
    |       |               search-plan-nov-17.md
    |       |
    |       +---scripts
    |       |   |   analyze-transformations-smart.js
    |       |   |   analyze-usage.js
    |       |   |   build-hooks.js
    |       |   |   build-viewer.js
    |       |   |   build-worker-binary.js
    |       |   |   debug-transcript-structure.ts
    |       |   |   discord-release-notify.js
    |       |   |   dump-transcript-readable.ts
    |       |   |   endless-mode-token-calculator.js
    |       |   |   export-memories.ts
    |       |   |   extract-rich-context-examples.ts
    |       |   |   find-silent-failures.sh
    |       |   |   format-transcript-context.ts
    |       |   |   generate-changelog.js
    |       |   |   import-memories.ts
    |       |   |   publish.js
    |       |   |   smart-install.js
    |       |   |   sync-marketplace.cjs
    |       |   |   sync-to-marketplace.sh
    |       |   |   test-transcript-parser.ts
    |       |   |   transcript-to-markdown.ts
    |       |   |
    |       |   +---bug-report
    |       |   |       cli.ts
    |       |   |       collector.ts
    |       |   |       index.ts
    |       |   |
    |       |   +---extraction
    |       |   |       extract-all-xml.py
    |       |   |       filter-actual-xml.py
    |       |   |       README.md
    |       |   |
    |       |   \---translate-readme
    |       |           cli.ts
    |       |           examples.ts
    |       |           index.ts
    |       |           README.md
    |       |
    |       +---src
    |       |   +---bin
    |       |   |       cleanup-duplicates.ts
    |       |   |       import-xml-observations.ts
    |       |   |
    |       |   +---cli
    |       |   |       worker-cli.ts
    |       |   |
    |       |   +---constants
    |       |   |       observation-metadata.ts
    |       |   |
    |       |   +---hooks
    |       |   |   |   cleanup-hook.ts
    |       |   |   |   context-hook.ts
    |       |   |   |   hook-response.ts
    |       |   |   |   new-hook.ts
    |       |   |   |   save-hook.ts
    |       |   |   |   summary-hook.ts
    |       |   |   |   user-message-hook.ts
    |       |   |   |
    |       |   |   \---shared
    |       |   |           error-handler.ts
    |       |   |
    |       |   +---sdk
    |       |   |       parser.test.ts
    |       |   |       parser.ts
    |       |   |       prompts.ts
    |       |   |
    |       |   +---servers
    |       |   |       mcp-server.ts
    |       |   |
    |       |   +---services
    |       |   |   |   context-generator.ts
    |       |   |   |   worker-service.ts
    |       |   |   |   worker-types.ts
    |       |   |   |   worker-wrapper.ts
    |       |   |   |
    |       |   |   +---process
    |       |   |   |       ProcessManager.ts
    |       |   |   |
    |       |   |   +---sqlite
    |       |   |   |       Database.ts
    |       |   |   |       index.ts
    |       |   |   |       migrations.ts
    |       |   |   |       PendingMessageStore.ts
    |       |   |   |       SessionSearch.ts
    |       |   |   |       SessionStore.ts
    |       |   |   |       types.ts
    |       |   |   |
    |       |   |   +---sync
    |       |   |   |       ChromaSync.ts
    |       |   |   |
    |       |   |   \---worker
    |       |   |       |   BranchManager.ts
    |       |   |       |   DatabaseManager.ts
    |       |   |       |   FormattingService.ts
    |       |   |       |   PaginationHelper.ts
    |       |   |       |   README.md
    |       |   |       |   SDKAgent.ts
    |       |   |       |   SearchManager.ts
    |       |   |       |   SessionManager.ts
    |       |   |       |   SettingsManager.ts
    |       |   |       |   SSEBroadcaster.ts
    |       |   |       |   TimelineService.ts
    |       |   |       |
    |       |   |       +---events
    |       |   |       |       SessionEventBroadcaster.ts
    |       |   |       |
    |       |   |       +---http
    |       |   |       |   |   BaseRouteHandler.ts
    |       |   |       |   |   middleware.ts
    |       |   |       |   |
    |       |   |       |   \---routes
    |       |   |       |           DataRoutes.ts
    |       |   |       |           SearchRoutes.ts
    |       |   |       |           SessionRoutes.ts
    |       |   |       |           SettingsRoutes.ts
    |       |   |       |           ViewerRoutes.ts
    |       |   |       |
    |       |   |       +---session
    |       |   |       |       SessionCompletionHandler.ts
    |       |   |       |
    |       |   |       \---validation
    |       |   |               PrivacyCheckValidator.ts
    |       |   |
    |       |   +---shared
    |       |   |       hook-constants.ts
    |       |   |       hook-error-handler.ts
    |       |   |       paths.ts
    |       |   |       SettingsDefaultsManager.ts
    |       |   |       timeline-formatting.ts
    |       |   |       transcript-parser.ts
    |       |   |       worker-utils.ts
    |       |   |
    |       |   +---types
    |       |   |       database.ts
    |       |   |       transcript.ts
    |       |   |
    |       |   +---ui
    |       |   |   |   claude-mem-logo-for-dark-mode.webp
    |       |   |   |   claude-mem-logomark.webp
    |       |   |   |   icon-thick-completed.svg
    |       |   |   |   icon-thick-investigated.svg
    |       |   |   |   icon-thick-learned.svg
    |       |   |   |   icon-thick-next-steps.svg
    |       |   |   |   icon-thin-completed.svg
    |       |   |   |   icon-thin-investigated.svg
    |       |   |   |   icon-thin-learned.svg
    |       |   |   |   icon-thin-next-steps.svg
    |       |   |   |   viewer-template.html
    |       |   |   |
    |       |   |   \---viewer
    |       |   |       |   App.tsx
    |       |   |       |   index.tsx
    |       |   |       |   types.ts
    |       |   |       |
    |       |   |       +---assets
    |       |   |       |   \---fonts
    |       |   |       |           monaspace-radon-var.woff
    |       |   |       |           monaspace-radon-var.woff2
    |       |   |       |
    |       |   |       +---components
    |       |   |       |       ContextSettingsModal.tsx
    |       |   |       |       ErrorBoundary.tsx
    |       |   |       |       Feed.tsx
    |       |   |       |       GitHubStarsButton.tsx
    |       |   |       |       Header.tsx
    |       |   |       |       ObservationCard.tsx
    |       |   |       |       PromptCard.tsx
    |       |   |       |       ScrollToTop.tsx
    |       |   |       |       SummaryCard.tsx
    |       |   |       |       TerminalPreview.tsx
    |       |   |       |       ThemeToggle.tsx
    |       |   |       |
    |       |   |       +---constants
    |       |   |       |       api.ts
    |       |   |       |       settings.ts
    |       |   |       |       timing.ts
    |       |   |       |       ui.ts
    |       |   |       |
    |       |   |       +---hooks
    |       |   |       |       useContextPreview.ts
    |       |   |       |       useGitHubStars.ts
    |       |   |       |       usePagination.ts
    |       |   |       |       useSettings.ts
    |       |   |       |       useSSE.ts
    |       |   |       |       useStats.ts
    |       |   |       |       useTheme.ts
    |       |   |       |
    |       |   |       \---utils
    |       |   |               data.ts
    |       |   |               formatNumber.ts
    |       |   |               formatters.ts
    |       |   |
    |       |   \---utils
    |       |           bun-path.ts
    |       |           error-messages.ts
    |       |           logger.ts
    |       |           project-name.ts
    |       |           tag-stripping.ts
    |       |           transcript-parser.ts
    |       |
    |       \---tests
    |           |   branch-selector.test.ts
    |           |   bun-path.test.ts
    |           |   smart-install.test.js
    |           |   strip-memory-tags.test.ts
    |           |   user-prompt-tag-stripping.test.ts
    |           |
    |           +---error-handling
    |           |       hook-error-logging.test.ts
    |           |
    |           +---happy-paths
    |           |       batch-observations.test.ts
    |           |       context-injection.test.ts
    |           |       observation-capture.test.ts
    |           |       search.test.ts
    |           |       session-cleanup.test.ts
    |           |       session-init.test.ts
    |           |       session-summary.test.ts
    |           |
    |           +---helpers
    |           |       mocks.ts
    |           |       scenarios.ts
    |           |
    |           +---integration
    |           |       context-inject-early.test.ts
    |           |       full-lifecycle.test.ts
    |           |       hook-execution-environments.test.ts
    |           |
    |           +---security
    |           |       command-injection.test.ts
    |           |
    |           \---services
    |                   chroma-sync-errors.test.ts
    |
    +---__agents
    |   |   agile-sprint-planner.md
    |   |   angular-expert.md
    |   |   api-architect.md
    |   |   architecture.md
    |   |   aspnet-core-expert.md
    |   |   aws-cloud-architect.md
    |   |   backend-developer.md
    |   |   cicd-pipeline-architect.md
    |   |   clean-architecture-expert.md
    |   |   clojure-expert.md
    |   |   code-archaeologist.md
    |   |   code-pairing-assistant.md
    |   |   code-quality-guardian.md
    |   |   code-review-master.md
    |   |   code-reviewer-002.md
    |   |   code-reviewer.md
    |   |   csharp-expert.md
    |   |   dart-flutter-expert.md
    |   |   database-admin.md
    |   |   database-architect.md
    |   |   dependency-manager.md
    |   |   design-patterns-expert.md
    |   |   django-expert.md
    |   |   docker-specialist.md
    |   |   documentation-specialist-002.md
    |   |   documentation-specialist.md
    |   |   elixir-expert.md
    |   |   environment-manager.md
    |   |   expressjs-nodejs-expert.md
    |   |   fastapi-expert.md
    |   |   frontend-developer.md
    |   |   git-workflow-expert.md
    |   |   go-expert.md
    |   |   guidelines-compliance.md
    |   |   haskell-expert.md
    |   |   java-expert.md
    |   |   javascript-typescript-expert.md
    |   |   kotlin-expert.md
    |   |   kubernetes-expert.md
    |   |   laravel-expert.md
    |   |   llm-finetuning-expert.md
    |   |   llmops-engineer.md
    |   |   machine-learning-engineer.md
    |   |   nextjs-expert.md
    |   |   nlp-llm-integration-expert.md
    |   |   observability-engineer.md
    |   |   performance-optimization-specialist.md
    |   |   performance-optimizer.md
    |   |   performance-profiler.md
    |   |   performance-testing-expert.md
    |   |   php-expert.md
    |   |   prisma-expert.md
    |   |   privacy-engineer.md
    |   |   project-analyst.md
    |   |   project-setup-wizard.md
    |   |   prompt-engineering-specialist.md
    |   |   python-data-scientist.md
    |   |   python-expert.md
    |   |   rag-architecture-expert.md
    |   |   rails-expert.md
    |   |   react-architect.md
    |   |   release-manager.md
    |   |   ruby-expert.md
    |   |   rust-expert.md
    |   |   scala-expert.md
    |   |   search-specialist.md
    |   |   security-audit-expert.md
    |   |   security-specialist.md
    |   |   session-manager.md
    |   |   slash-command-architect.md
    |   |   spring-boot-expert.md
    |   |   style-compliance.md
    |   |   subagent-architect.md
    |   |   swift-expert.md
    |   |   tailwind-css-expert.md
    |   |   team-configurator.md
    |   |   tech-lead-orchestrator.md
    |   |   technical-debt-analyst.md
    |   |   terraform-infrastructure-expert.md
    |   |   test-automation-specialist.md
    |   |   test-strategy-architect.md
    |   |   vibe-coding-coordinator.md
    |   |   vue-specialist.md
    |   |   _logic-reviewer.md
    |   |
    |   +---api-scaffolding
    |   |   +---agents
    |   |   |       backend-architect.md
    |   |   |       django-pro.md
    |   |   |       fastapi-pro.md
    |   |   |       graphql-architect.md
    |   |   |
    |   |   \---skills
    |   |       \---fastapi-templates
    |   |               SKILL.md
    |   |
    |   +---api-testing-observability
    |   |   +---agents
    |   |   |       api-documenter.md
    |   |   |
    |   |   \---commands
    |   |           api-mock.md
    |   |
    |   +---application-performance
    |   |   +---agents
    |   |   |       frontend-developer.md
    |   |   |       observability-engineer.md
    |   |   |       performance-engineer.md
    |   |   |
    |   |   \---commands
    |   |           performance-optimization.md
    |   |
    |   +---backend-api-security
    |   |   \---agents
    |   |           backend-architect.md
    |   |           backend-security-coder.md
    |   |
    |   +---backend-development
    |   |   +---agents
    |   |   |       backend-architect.md
    |   |   |       event-sourcing-architect.md
    |   |   |       graphql-architect.md
    |   |   |       tdd-orchestrator.md
    |   |   |       temporal-python-pro.md
    |   |   |
    |   |   +---commands
    |   |   |       feature-development.md
    |   |   |
    |   |   \---skills
    |   |       +---api-design-principles
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   +---assets
    |   |       |   |       api-design-checklist.md
    |   |       |   |       rest-api-template.py
    |   |       |   |
    |   |       |   \---references
    |   |       |           graphql-schema-design.md
    |   |       |           rest-best-practices.md
    |   |       |
    |   |       +---architecture-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---cqrs-implementation
    |   |       |       SKILL.md
    |   |       |
    |   |       +---event-store-design
    |   |       |       SKILL.md
    |   |       |
    |   |       +---microservices-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---projection-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---saga-orchestration
    |   |       |       SKILL.md
    |   |       |
    |   |       +---temporal-python-testing
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---resources
    |   |       |           integration-testing.md
    |   |       |           local-setup.md
    |   |       |           replay-testing.md
    |   |       |           unit-testing.md
    |   |       |
    |   |       \---workflow-orchestration-patterns
    |   |               SKILL.md
    |   |
    |   +---c4-architecture
    |   |   +---agents
    |   |   |       c4-code.md
    |   |   |       c4-component.md
    |   |   |       c4-container.md
    |   |   |       c4-context.md
    |   |   |
    |   |   \---commands
    |   |           c4-architecture.md
    |   |
    |   +---cicd-automation
    |   |   +---agents
    |   |   |       cloud-architect.md
    |   |   |       deployment-engineer.md
    |   |   |       devops-troubleshooter.md
    |   |   |       kubernetes-architect.md
    |   |   |       terraform-specialist.md
    |   |   |
    |   |   +---commands
    |   |   |       workflow-automate.md
    |   |   |
    |   |   \---skills
    |   |       +---deployment-pipeline-design
    |   |       |       SKILL.md
    |   |       |
    |   |       +---github-actions-templates
    |   |       |       SKILL.md
    |   |       |
    |   |       +---gitlab-ci-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---secrets-management
    |   |               SKILL.md
    |   |
    |   +---cloud-infrastructure
    |   |   +---agents
    |   |   |       cloud-architect.md
    |   |   |       deployment-engineer.md
    |   |   |       hybrid-cloud-architect.md
    |   |   |       kubernetes-architect.md
    |   |   |       network-engineer.md
    |   |   |       service-mesh-expert.md
    |   |   |       terraform-specialist.md
    |   |   |
    |   |   \---skills
    |   |       +---cost-optimization
    |   |       |       SKILL.md
    |   |       |
    |   |       +---hybrid-cloud-networking
    |   |       |       SKILL.md
    |   |       |
    |   |       +---istio-traffic-management
    |   |       |       SKILL.md
    |   |       |
    |   |       +---linkerd-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---mtls-configuration
    |   |       |       SKILL.md
    |   |       |
    |   |       +---multi-cloud-architecture
    |   |       |       SKILL.md
    |   |       |
    |   |       +---service-mesh-observability
    |   |       |       SKILL.md
    |   |       |
    |   |       \---terraform-module-library
    |   |           |   SKILL.md
    |   |           |
    |   |           \---references
    |   |                   aws-modules.md
    |   |
    |   +---data-validation-suite
    |   |   \---agents
    |   |           backend-security-coder.md
    |   |
    |   +---database-cloud-optimization
    |   |   +---agents
    |   |   |       backend-architect.md
    |   |   |       cloud-architect.md
    |   |   |       database-architect.md
    |   |   |       database-optimizer.md
    |   |   |
    |   |   \---commands
    |   |           cost-optimize.md
    |   |
    |   +---deployment-validation
    |   |   +---agents
    |   |   |       cloud-architect.md
    |   |   |
    |   |   \---commands
    |   |           config-validate.md
    |   |
    |   +---distributed-debugging
    |   |   +---agents
    |   |   |       devops-troubleshooter.md
    |   |   |       error-detective.md
    |   |   |
    |   |   \---commands
    |   |           debug-trace.md
    |   |
    |   +---django
    |   |       django-api-developer.md
    |   |       django-backend-expert.md
    |   |       django-orm-expert.md
    |   |
    |   +---error-debugging
    |   |   +---agents
    |   |   |       debugger.md
    |   |   |       error-detective.md
    |   |   |
    |   |   \---commands
    |   |           error-analysis.md
    |   |           error-trace.md
    |   |           multi-agent-review.md
    |   |
    |   +---error-diagnostics
    |   |   +---agents
    |   |   |       debugger.md
    |   |   |       error-detective.md
    |   |   |
    |   |   \---commands
    |   |           error-analysis.md
    |   |           error-trace.md
    |   |           smart-debug.md
    |   |
    |   +---framework-migration
    |   |   +---agents
    |   |   |       architect-review.md
    |   |   |       legacy-modernizer.md
    |   |   |
    |   |   +---commands
    |   |   |       code-migrate.md
    |   |   |       deps-upgrade.md
    |   |   |       legacy-modernize.md
    |   |   |
    |   |   \---skills
    |   |       +---angular-migration
    |   |       |       SKILL.md
    |   |       |
    |   |       +---database-migration
    |   |       |       SKILL.md
    |   |       |
    |   |       +---dependency-upgrade
    |   |       |       SKILL.md
    |   |       |
    |   |       \---react-modernization
    |   |               SKILL.md
    |   |
    |   +---full-stack-orchestration
    |   |   +---agents
    |   |   |       deployment-engineer.md
    |   |   |       performance-engineer.md
    |   |   |       security-auditor.md
    |   |   |       test-automator.md
    |   |   |
    |   |   \---commands
    |   |           full-stack-feature.md
    |   |
    |   +---functional-programming
    |   |   \---agents
    |   |           elixir-pro.md
    |   |           haskell-pro.md
    |   |
    |   +---game-development
    |   |   +---agents
    |   |   |       minecraft-bukkit-pro.md
    |   |   |       unity-developer.md
    |   |   |
    |   |   \---skills
    |   |       +---godot-gdscript-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---unity-ecs-patterns
    |   |               SKILL.md
    |   |
    |   +---julia-development
    |   |   \---agents
    |   |           julia-pro.md
    |   |
    |   +---jvm-languages
    |   |   \---agents
    |   |           csharp-pro.md
    |   |           java-pro.md
    |   |           scala-pro.md
    |   |
    |   +---kubernetes-operations
    |   |   +---agents
    |   |   |       kubernetes-architect.md
    |   |   |
    |   |   \---skills
    |   |       +---gitops-workflow
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---references
    |   |       |           argocd-setup.md
    |   |       |           sync-policies.md
    |   |       |
    |   |       +---helm-chart-scaffolding
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   +---assets
    |   |       |   |       Chart.yaml.template
    |   |       |   |       values.yaml.template
    |   |       |   |
    |   |       |   +---references
    |   |       |   |       chart-structure.md
    |   |       |   |
    |   |       |   \---scripts
    |   |       |           validate-chart.sh
    |   |       |
    |   |       +---k8s-manifest-generator
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   +---assets
    |   |       |   |       configmap-template.yaml
    |   |       |   |       deployment-template.yaml
    |   |       |   |       service-template.yaml
    |   |       |   |
    |   |       |   \---references
    |   |       |           deployment-spec.md
    |   |       |           service-spec.md
    |   |       |
    |   |       \---k8s-security-policies
    |   |           |   SKILL.md
    |   |           |
    |   |           +---assets
    |   |           |       network-policy-template.yaml
    |   |           |
    |   |           \---references
    |   |                   rbac-patterns.md
    |   |
    |   +---multi-platform-apps
    |   |   +---agents
    |   |   |       backend-architect.md
    |   |   |       flutter-expert.md
    |   |   |       frontend-developer.md
    |   |   |       ios-developer.md
    |   |   |       mobile-developer.md
    |   |   |       ui-ux-designer.md
    |   |   |
    |   |   \---commands
    |   |           multi-platform.md
    |   |
    |   +---orchestrators
    |   |       project-analyst.md
    |   |       task-master-initialization-specialist.md
    |   |       task-master-template-manager.md
    |   |       team-configurator.md
    |   |       tech-lead-orchestrator.md
    |   |
    |   +---performance-optimizers
    |   |       parallel-coordinator.md
    |   |       session-optimizer.md
    |   |       tool-batch-optimizer.md
    |   |
    |   +---performance-testing-review
    |   |   +---agents
    |   |   |       performance-engineer.md
    |   |   |       test-automator.md
    |   |   |
    |   |   \---commands
    |   |           ai-review.md
    |   |           multi-agent-review.md
    |   |
    |   +---personalities
    |   |       agent-evolution-system.md
    |   |       code-archaeologist-time-traveler.yaml
    |   |       code-reviewer-evil-corp.yaml
    |   |       code-reviewer.yaml
    |   |       quality-system-engineer-evil-corp.yaml
    |   |       rubber-duck-debugger.yaml
    |   |       software-engineering-expert.yaml
    |   |       technical-debt-collector.yaml
    |   |
    |   +---python
    |   |       devops-cicd-expert.md
    |   |       django-expert.md
    |   |       fastapi-expert.md
    |   |       ml-data-expert.md
    |   |       performance-expert.md
    |   |       python-expert.md
    |   |       security-expert.md
    |   |       testing-expert.md
    |   |       web-scraping-expert.md
    |   |
    |   +---python-development
    |   |   +---agents
    |   |   |       django-pro.md
    |   |   |       fastapi-pro.md
    |   |   |       python-pro.md
    |   |   |
    |   |   +---commands
    |   |   |       python-scaffold.md
    |   |   |
    |   |   \---skills
    |   |       +---async-python-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---python-packaging
    |   |       |       SKILL.md
    |   |       |
    |   |       +---python-performance-optimization
    |   |       |       SKILL.md
    |   |       |
    |   |       +---python-testing-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---uv-package-manager
    |   |               SKILL.md
    |   |
    |   +---react
    |   |       react-component-architect.md
    |   |       react-nextjs-expert.md
    |   |
    |   +---seo-analysis-monitoring
    |   |   \---agents
    |   |           seo-authority-builder.md
    |   |           seo-cannibalization-detector.md
    |   |           seo-content-refresher.md
    |   |
    |   +---seo-content-creation
    |   |   \---agents
    |   |           seo-content-auditor.md
    |   |           seo-content-planner.md
    |   |           seo-content-writer.md
    |   |
    |   +---seo-technical-optimization
    |   |   \---agents
    |   |           seo-keyword-strategist.md
    |   |           seo-meta-optimizer.md
    |   |           seo-snippet-hunter.md
    |   |           seo-structure-architect.md
    |   |
    |   +---tdd-workflows
    |   |   +---agents
    |   |   |       code-reviewer.md
    |   |   |       tdd-orchestrator.md
    |   |   |
    |   |   \---commands
    |   |           tdd-cycle.md
    |   |           tdd-green.md
    |   |           tdd-red.md
    |   |           tdd-refactor.md
    |   |
    |   +---unit-testing
    |   |   +---agents
    |   |   |       debugger.md
    |   |   |       test-automator.md
    |   |   |
    |   |   \---commands
    |   |           test-generate.md
    |   |
    |   +---_agent-orchestration
    |   |   +---agents
    |   |   |       context-manager.md
    |   |   |
    |   |   \---commands
    |   |           improve-agent.md
    |   |           multi-agent-optimize.md
    |   |
    |   +---_auto-agent
    |   |       activation-system.md
    |   |       agent-communication-protocol.md
    |   |       auto-detection-engine.md
    |   |       choreography-engine.md
    |   |       context-aware-activator.md
    |   |       enhanced-agent-template.md
    |   |       intelligent-agent-selector.md
    |   |       knowledge-graph-manager.md
    |   |       learning-system.md
    |   |       personality-engine.md
    |   |       predictive-orchestrator.md
    |   |       smart-agent-router.md
    |   |       success-pattern-learner.md
    |   |       workflow-coordinator.md
    |   |
    |   +---_code-documentation
    |   |   +---agents
    |   |   |       code-reviewer.md
    |   |   |       docs-architect.md
    |   |   |       tutorial-engineer.md
    |   |   |
    |   |   \---commands
    |   |           code-explain.md
    |   |           doc-generate.md
    |   |
    |   +---_code-refactoring
    |   |   +---agents
    |   |   |       code-reviewer.md
    |   |   |       legacy-modernizer.md
    |   |   |
    |   |   \---commands
    |   |           context-restore.md
    |   |           refactor-clean.md
    |   |           tech-debt.md
    |   |
    |   +---_code-review-ai
    |   |   +---agents
    |   |   |       architect-review.md
    |   |   |
    |   |   \---commands
    |   |           ai-review.md
    |   |
    |   +---_codebase-cleanup
    |   |   +---agents
    |   |   |       code-reviewer.md
    |   |   |       test-automator.md
    |   |   |
    |   |   \---commands
    |   |           deps-audit.md
    |   |           refactor-clean.md
    |   |           tech-debt.md
    |   |
    |   +---_comprehensive-review
    |   |   +---agents
    |   |   |       architect-review.md
    |   |   |       code-reviewer.md
    |   |   |       security-auditor.md
    |   |   |
    |   |   \---commands
    |   |           full-review.md
    |   |           pr-enhance.md
    |   |
    |   +---_context-management
    |   |   +---agents
    |   |   |       context-manager.md
    |   |   |
    |   |   \---commands
    |   |           context-restore.md
    |   |           context-save.md
    |   |
    |   +---_data-engineering
    |   |   +---agents
    |   |   |       backend-architect.md
    |   |   |       data-engineer.md
    |   |   |
    |   |   +---commands
    |   |   |       data-driven-feature.md
    |   |   |       data-pipeline.md
    |   |   |
    |   |   \---skills
    |   |       +---airflow-dag-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---data-quality-frameworks
    |   |       |       SKILL.md
    |   |       |
    |   |       +---dbt-transformation-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---spark-optimization
    |   |               SKILL.md
    |   |
    |   +---_database-design
    |   |   +---agents
    |   |   |       database-architect.md
    |   |   |       sql-pro.md
    |   |   |
    |   |   \---skills
    |   |       \---postgresql
    |   |               SKILL.md
    |   |
    |   +---_database-migrations
    |   |   +---agents
    |   |   |       database-admin.md
    |   |   |       database-optimizer.md
    |   |   |
    |   |   \---commands
    |   |           migration-observability.md
    |   |           sql-migrations.md
    |   |
    |   +---_debugging-toolkit
    |   |   +---agents
    |   |   |       debugger.md
    |   |   |       dx-optimizer.md
    |   |   |
    |   |   \---commands
    |   |           smart-debug.md
    |   |
    |   +---_deployment-strategies
    |   |   \---agents
    |   |           deployment-engineer.md
    |   |           terraform-specialist.md
    |   |
    |   +---_developer-essentials
    |   |   +---agents
    |   |   |       monorepo-architect.md
    |   |   |
    |   |   \---skills
    |   |       +---auth-implementation-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---bazel-build-optimization
    |   |       |       SKILL.md
    |   |       |
    |   |       +---code-review-excellence
    |   |       |       SKILL.md
    |   |       |
    |   |       +---debugging-strategies
    |   |       |       SKILL.md
    |   |       |
    |   |       +---e2e-testing-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---error-handling-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---git-advanced-workflows
    |   |       |       SKILL.md
    |   |       |
    |   |       +---monorepo-management
    |   |       |       SKILL.md
    |   |       |
    |   |       +---nx-workspace-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---sql-optimization-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---turborepo-caching
    |   |               SKILL.md
    |   |
    |   +---_documentation-generation
    |   |   +---agents
    |   |   |       api-documenter.md
    |   |   |       docs-architect.md
    |   |   |       mermaid-expert.md
    |   |   |       reference-builder.md
    |   |   |       tutorial-engineer.md
    |   |   |
    |   |   +---commands
    |   |   |       doc-generate.md
    |   |   |
    |   |   \---skills
    |   |       +---architecture-decision-records
    |   |       |       SKILL.md
    |   |       |
    |   |       +---changelog-automation
    |   |       |       SKILL.md
    |   |       |
    |   |       \---openapi-spec-generation
    |   |               SKILL.md
    |   |
    |   +---_javascript-typescript
    |   |   +---agents
    |   |   |       javascript-pro.md
    |   |   |       typescript-pro.md
    |   |   |
    |   |   +---commands
    |   |   |       typescript-scaffold.md
    |   |   |
    |   |   \---skills
    |   |       +---javascript-testing-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---modern-javascript-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---nodejs-backend-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---typescript-advanced-types
    |   |               SKILL.md
    |   |
    |   +---_llm-application-dev
    |   |   +---agents
    |   |   |       ai-engineer.md
    |   |   |       prompt-engineer.md
    |   |   |       vector-database-engineer.md
    |   |   |
    |   |   +---commands
    |   |   |       ai-assistant.md
    |   |   |       langchain-agent.md
    |   |   |       prompt-optimize.md
    |   |   |
    |   |   \---skills
    |   |       +---embedding-strategies
    |   |       |       SKILL.md
    |   |       |
    |   |       +---hybrid-search-implementation
    |   |       |       SKILL.md
    |   |       |
    |   |       +---langchain-architecture
    |   |       |       SKILL.md
    |   |       |
    |   |       +---llm-evaluation
    |   |       |       SKILL.md
    |   |       |
    |   |       +---prompt-engineering-patterns
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   +---assets
    |   |       |   |       few-shot-examples.json
    |   |       |   |       prompt-template-library.md
    |   |       |   |
    |   |       |   +---references
    |   |       |   |       chain-of-thought.md
    |   |       |   |       few-shot-learning.md
    |   |       |   |       prompt-optimization.md
    |   |       |   |       prompt-templates.md
    |   |       |   |       system-prompts.md
    |   |       |   |
    |   |       |   \---scripts
    |   |       |           optimize-prompt.py
    |   |       |
    |   |       +---rag-implementation
    |   |       |       SKILL.md
    |   |       |
    |   |       +---similarity-search-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---vector-index-tuning
    |   |               SKILL.md
    |   |
    |   +---_machine-learning-ops
    |   |   +---agents
    |   |   |       data-scientist.md
    |   |   |       ml-engineer.md
    |   |   |       mlops-engineer.md
    |   |   |
    |   |   +---commands
    |   |   |       ml-pipeline.md
    |   |   |
    |   |   \---skills
    |   |       \---ml-pipeline-workflow
    |   |               SKILL.md
    |   |
    |   +---_observability-monitoring
    |   |   +---agents
    |   |   |       database-optimizer.md
    |   |   |       network-engineer.md
    |   |   |       observability-engineer.md
    |   |   |       performance-engineer.md
    |   |   |
    |   |   +---commands
    |   |   |       monitor-setup.md
    |   |   |       slo-implement.md
    |   |   |
    |   |   \---skills
    |   |       +---distributed-tracing
    |   |       |       SKILL.md
    |   |       |
    |   |       +---grafana-dashboards
    |   |       |       SKILL.md
    |   |       |
    |   |       +---prometheus-configuration
    |   |       |       SKILL.md
    |   |       |
    |   |       \---slo-implementation
    |   |               SKILL.md
    |   |
    |   +---_security-compliance
    |   |   +---agents
    |   |   |       security-auditor.md
    |   |   |
    |   |   \---commands
    |   |           compliance-check.md
    |   |
    |   +---_security-scanning
    |   |   +---agents
    |   |   |       security-auditor.md
    |   |   |       threat-modeling-expert.md
    |   |   |
    |   |   +---commands
    |   |   |       security-dependencies.md
    |   |   |       security-hardening.md
    |   |   |       security-sast.md
    |   |   |
    |   |   \---skills
    |   |       +---attack-tree-construction
    |   |       |       SKILL.md
    |   |       |
    |   |       +---sast-configuration
    |   |       |       SKILL.md
    |   |       |
    |   |       +---security-requirement-extraction
    |   |       |       SKILL.md
    |   |       |
    |   |       +---stride-analysis-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---threat-mitigation-mapping
    |   |               SKILL.md
    |   |
    |   +---_shell-scripting
    |   |   +---agents
    |   |   |       bash-pro.md
    |   |   |       posix-shell-pro.md
    |   |   |
    |   |   \---skills
    |   |       +---bash-defensive-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---bats-testing-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---shellcheck-configuration
    |   |               SKILL.md
    |   |
    |   +---_systems-programming
    |   |   +---agents
    |   |   |       c-pro.md
    |   |   |       cpp-pro.md
    |   |   |       golang-pro.md
    |   |   |       rust-pro.md
    |   |   |
    |   |   +---commands
    |   |   |       rust-project.md
    |   |   |
    |   |   \---skills
    |   |       +---go-concurrency-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       +---memory-safety-patterns
    |   |       |       SKILL.md
    |   |       |
    |   |       \---rust-async-patterns
    |   |               SKILL.md
    |   |
    |   +---_web-scripting
    |   |   \---agents
    |   |           php-pro.md
    |   |           ruby-pro.md
    |   |
    |   +---__anthropic
    |   |   |   skill.json
    |   |   |   skill.md
    |   |   |
    |   |   +---claude-code
    |   |   |       skill.json
    |   |   |       skill.md
    |   |   |
    |   |   +---claude-command-builder
    |   |   |       skill.json
    |   |   |       skill.md
    |   |   |
    |   |   +---claude-hook-builder
    |   |   |       skill.json
    |   |   |       skill.md
    |   |   |
    |   |   +---claude-mcp-expert
    |   |   |       skill.json
    |   |   |       skill.md
    |   |   |
    |   |   +---claude-settings-expert
    |   |   |       skill.json
    |   |   |       skill.md
    |   |   |
    |   |   \---claude-skill-builder
    |   |           skill.json
    |   |           skill.md
    |   |
    |   +---__sub-agents
    |   |   +---01-core-development
    |   |   |       api-designer.md
    |   |   |       backend-developer.md
    |   |   |       electron-pro.md
    |   |   |       frontend-developer.md
    |   |   |       fullstack-developer.md
    |   |   |       graphql-architect.md
    |   |   |       microservices-architect.md
    |   |   |       mobile-developer.md
    |   |   |       README.md
    |   |   |       ui-designer.md
    |   |   |       websocket-engineer.md
    |   |   |
    |   |   +---02-language-specialists
    |   |   |       angular-architect.md
    |   |   |       cpp-pro.md
    |   |   |       csharp-developer.md
    |   |   |       django-developer.md
    |   |   |       dotnet-core-expert.md
    |   |   |       dotnet-framework-4.8-expert.md
    |   |   |       flutter-expert.md
    |   |   |       golang-pro.md
    |   |   |       java-architect.md
    |   |   |       javascript-pro.md
    |   |   |       kotlin-specialist.md
    |   |   |       laravel-specialist.md
    |   |   |       nextjs-developer.md
    |   |   |       php-pro.md
    |   |   |       powershell-5.1-expert.md
    |   |   |       powershell-7-expert.md
    |   |   |       python-pro.md
    |   |   |       rails-expert.md
    |   |   |       react-specialist.md
    |   |   |       README.md
    |   |   |       rust-engineer.md
    |   |   |       spring-boot-engineer.md
    |   |   |       sql-pro.md
    |   |   |       swift-expert.md
    |   |   |       typescript-pro.md
    |   |   |       vue-expert.md
    |   |   |
    |   |   +---03-infrastructure
    |   |   |       azure-infra-engineer.md
    |   |   |       cloud-architect.md
    |   |   |       database-administrator.md
    |   |   |       deployment-engineer.md
    |   |   |       devops-engineer.md
    |   |   |       devops-incident-responder.md
    |   |   |       incident-responder.md
    |   |   |       kubernetes-specialist.md
    |   |   |       network-engineer.md
    |   |   |       platform-engineer.md
    |   |   |       README.md
    |   |   |       security-engineer.md
    |   |   |       sre-engineer.md
    |   |   |       terraform-engineer.md
    |   |   |       windows-infra-admin.md
    |   |   |
    |   |   +---04-quality-security
    |   |   |       accessibility-tester.md
    |   |   |       ad-security-reviewer.md
    |   |   |       architect-reviewer.md
    |   |   |       chaos-engineer.md
    |   |   |       code-reviewer.md
    |   |   |       compliance-auditor.md
    |   |   |       debugger.md
    |   |   |       error-detective.md
    |   |   |       penetration-tester.md
    |   |   |       performance-engineer.md
    |   |   |       powershell-security-hardening.md
    |   |   |       qa-expert.md
    |   |   |       README.md
    |   |   |       security-auditor.md
    |   |   |       test-automator.md
    |   |   |
    |   |   +---05-data-ai
    |   |   |       ai-engineer.md
    |   |   |       data-analyst.md
    |   |   |       data-engineer.md
    |   |   |       data-scientist.md
    |   |   |       database-optimizer.md
    |   |   |       llm-architect.md
    |   |   |       machine-learning-engineer.md
    |   |   |       ml-engineer.md
    |   |   |       mlops-engineer.md
    |   |   |       nlp-engineer.md
    |   |   |       postgres-pro.md
    |   |   |       prompt-engineer.md
    |   |   |       README.md
    |   |   |
    |   |   +---06-developer-experience
    |   |   |       build-engineer.md
    |   |   |       cli-developer.md
    |   |   |       dependency-manager.md
    |   |   |       documentation-engineer.md
    |   |   |       dx-optimizer.md
    |   |   |       git-workflow-manager.md
    |   |   |       legacy-modernizer.md
    |   |   |       mcp-developer.md
    |   |   |       powershell-module-architect.md
    |   |   |       powershell-ui-architect.md
    |   |   |       README.md
    |   |   |       refactoring-specialist.md
    |   |   |       tooling-engineer.md
    |   |   |
    |   |   +---07-specialized-domains
    |   |   |       api-documenter.md
    |   |   |       blockchain-developer.md
    |   |   |       embedded-systems.md
    |   |   |       fintech-engineer.md
    |   |   |       game-developer.md
    |   |   |       iot-engineer.md
    |   |   |       m365-admin.md
    |   |   |       mobile-app-developer.md
    |   |   |       payment-integration.md
    |   |   |       quant-analyst.md
    |   |   |       README.md
    |   |   |       risk-manager.md
    |   |   |       seo-specialist.md
    |   |   |
    |   |   +---08-business-product
    |   |   |       business-analyst.md
    |   |   |       content-marketer.md
    |   |   |       customer-success-manager.md
    |   |   |       legal-advisor.md
    |   |   |       product-manager.md
    |   |   |       project-manager.md
    |   |   |       README.md
    |   |   |       sales-engineer.md
    |   |   |       scrum-master.md
    |   |   |       technical-writer.md
    |   |   |       ux-researcher.md
    |   |   |       wordpress-master.md
    |   |   |
    |   |   +---09-meta-orchestration
    |   |   |       agent-organizer.md
    |   |   |       context-manager.md
    |   |   |       error-coordinator.md
    |   |   |       it-ops-orchestrator.md
    |   |   |       knowledge-synthesizer.md
    |   |   |       multi-agent-coordinator.md
    |   |   |       performance-monitor.md
    |   |   |       README.md
    |   |   |       task-distributor.md
    |   |   |       workflow-orchestrator.md
    |   |   |
    |   |   \---10-research-analysis
    |   |           competitive-analyst.md
    |   |           data-researcher.md
    |   |           market-researcher.md
    |   |           README.md
    |   |           research-analyst.md
    |   |           search-specialist.md
    |   |           trend-analyst.md
    |   |
    |   \---___README
    |           advanced-agent-template.md
    |           agent-skills.md
    |           agent-template.md
    |           agents.md
    |           AGENT_DEVELOPMENT.md
    |           anti-duplication-protocol.md
    |           basic-agent-template.md
    |           best-practices.md
    |           creating-agents.md
    |           dependencies.md
    |           how-to-write-good-subagents.md
    |           plugins.md
    |           README.md
    |           usage.md
    |
    +---__claude.md-files
    |   +---AI-IntelliJ-Plugin
    |   |       CLAUDE.md
    |   |
    |   +---Anthropic-Quickstart
    |   |       CLAUDE.md
    |   |
    |   +---AVS-Vibe-Developer-Guide
    |   |       CLAUDE.md
    |   |
    |   +---AWS-MCP-Server
    |   |       CLAUDE.md
    |   |
    |   +---Basic-Memory
    |   |       CLAUDE.md
    |   |
    |   +---claude-code-mcp-enhanced
    |   |       CLAUDE.md
    |   |
    |   +---Comm
    |   |       CLAUDE.md
    |   |
    |   +---Course-Builder
    |   |       CLAUDE.md
    |   |
    |   +---Cursor-Tools
    |   |       CLAUDE.md
    |   |
    |   +---DroidconKotlin
    |   |       CLAUDE.md
    |   |
    |   +---EDSL
    |   |       CLAUDE.md
    |   |
    |   +---Giselle
    |   |       CLAUDE.md
    |   |
    |   +---Guitar
    |   |       CLAUDE.md
    |   |
    |   +---JSBeeb
    |   |       CLAUDE.md
    |   |
    |   +---Lamoom-Python
    |   |       CLAUDE.md
    |   |
    |   +---LangGraphJS
    |   |       CLAUDE.md
    |   |
    |   +---Network-Chronicles
    |   |       CLAUDE.md
    |   |
    |   +---Note-Companion
    |   |       CLAUDE.md
    |   |
    |   +---Pareto-Mac
    |   |       CLAUDE.md
    |   |
    |   +---Perplexity-MCP
    |   |       CLAUDE.md
    |   |
    |   +---SG-Cars-Trends-Backend
    |   |       CLAUDE.md
    |   |
    |   +---SPy
    |   |       CLAUDE.md
    |   |
    |   \---TPL
    |           CLAUDE.md
    |
    +---__commands
    |   |   act.md
    |   |   add-to-changelog.md
    |   |   brainstorm.md
    |   |   clean.md
    |   |   commit.md
    |   |   context-prime.md
    |   |   create-hook.md
    |   |   create-worktrees.md
    |   |   dependency-map.md
    |   |   execute-plan.md
    |   |   feature-prioritization.md
    |   |   fix-github-issue.md
    |   |   husky.md
    |   |   pr-review.md
    |   |   product-overview.md
    |   |   release-plan.md
    |   |   todo.md
    |   |   update-docs.md
    |   |   write-plan.md
    |   |
    |   +---linear
    |   |       epic-breakdown.md
    |   |       epic-prep.md
    |   |       refine-epic-lite.md
    |   |       refine-epic.md
    |   |       refine-feature.md
    |   |       refine-issue.md
    |   |       sprint-execute.md
    |   |       sprint-plan.md
    |   |       sprint-status.md
    |   |       tag-manager.md
    |   |
    |   \---__starter
    |           analyze-tokens.md
    |           convert-to-toon.md
    |           discover-skills.md
    |           install-skill.md
    |           toon-decode.md
    |           toon-encode.md
    |           toon-validate.md
    |
    +---__educational
    |   \---agent-notebooks
    |       +---assets
    |       |   \---repos_images
    |       |       |   ai_architecture_diagram.svg
    |       |       |   banner_repo.png
    |       |       |   subscribe-button.svg
    |       |       |   substack_image.png
    |       |       |   visit-site-badge.svg
    |       |       |
    |       |       \---sponsors_logos
    |       |           |   langchain.png
    |       |           |   qualifire.png
    |       |           |   Redis.png
    |       |           |   runpod.svg
    |       |           |   tavily.png
    |       |           |   xpander.png
    |       |           |
    |       |           \---trimmed_padded
    |       |                   coderabbit_Dark_Type_Mark.png
    |       |                   coderabbit_Light_Type_Mark_Orange.png
    |       |                   iGPT-logo-Black.png
    |       |                   iGPT-logo-white.png
    |       |                   trimmed_padded_anchorbroswer_light.png
    |       |                   trimmed_padded_anchorbrowser_dark.png
    |       |                   trimmed_padded_anchorbrowser_light.png
    |       |                   trimmed_padded_arcade_black.png
    |       |                   trimmed_padded_arcade_white_tight.png
    |       |                   trimmed_padded_brightdata.png
    |       |                   trimmed_padded_cognee.png
    |       |                   trimmed_padded_contextual_black.png
    |       |                   trimmed_padded_contextual_white.png
    |       |                   trimmed_padded_coral_black.png
    |       |                   trimmed_padded_coral_white.png
    |       |                   trimmed_padded_langchain.png
    |       |                   trimmed_padded_portia_black_tight.png
    |       |                   trimmed_padded_portia_white_tight.png
    |       |                   trimmed_padded_qualifire.png
    |       |                   trimmed_padded_Redis.png
    |       |                   trimmed_padded_runpod.png
    |       |                   trimmed_padded_runpod.svg
    |       |                   trimmed_padded_tavily.png
    |       |                   trimmed_padded_xpander.png
    |       |                   trimmed_padded_xpander_dark.png
    |       |                   trimmed_padded_xpander_light.png
    |       |
    |       \---tutorials
    |           +---a2a
    |           |       a2a_tutorial.ipynb
    |           |
    |           +---agent-evaluation-intellagent
    |           |       intellagent-evaluation-tutorial.ipynb
    |           |
    |           +---agent-memory-with-redis
    |           |   |   agent_memory_tutorial.ipynb
    |           |   |   README.md
    |           |   |
    |           |   \---assets
    |           |           long-term-memory.png
    |           |           memory-agents.png
    |           |           short-term-memory.png
    |           |
    |           +---agent-RAG-with-Contextual
    |           |       contextual_tutorial.ipynb
    |           |       README.md
    |           |       requirements.txt
    |           |
    |           +---agent-security-apex
    |           |       .gitignore
    |           |       agent-security-evaluation-tutorial.ipynb
    |           |       example_prompts.csv
    |           |       model_testing_tools.py
    |           |       prompt_manipulation_tools.py
    |           |       README.md
    |           |       requirements.txt
    |           |       system_prompt.txt
    |           |
    |           +---agent-security-with-llamafirewall
    |           |   |   hello-llama.ipynb
    |           |   |   input-guardrail.ipynb
    |           |   |   output-guardrail.ipynb
    |           |   |   README.md
    |           |   |   requirements.txt
    |           |   |   tools-security.ipynb
    |           |   |
    |           |   \---assets
    |           |           input-guardrail.png
    |           |           openai-trace.png
    |           |           output-guardrail.png
    |           |           tools-security.png
    |           |
    |           +---agent-with-brightdata
    |           |   |   langgraph_integration.ipynb
    |           |   |   README.md
    |           |   |   web_scraping_agent.ipynb
    |           |   |
    |           |   \---assets
    |           |           Settings.png
    |           |           Signup.png
    |           |
    |           +---agent-with-mcp
    |           |   |   mcp-tutorial.ipynb
    |           |   |
    |           |   \---assets
    |           |           Claude_Desktop_with_MCP.png
    |           |           customized_mcp_host.png
    |           |           mcp_architecture.png
    |           |           track_bitcoin_price_with_mcp.png
    |           |           track_crypto_market_data_with_mcp.png
    |           |
    |           +---agent-with-streamlit-ui
    |           |   |   app.py
    |           |   |   building-chatbot-notebook.ipynb
    |           |   |   requirements.txt
    |           |   |
    |           |   \---assets
    |           |           streamlit_chatbot.PNG
    |           |           streamlit_chatbot_video.mp4
    |           |
    |           +---agent-with-tavily-web-access
    |           |   |   hybrid-agent-tutorial.ipynb
    |           |   |   README.md
    |           |   |   requirements.txt
    |           |   |   search-extract-crawl.ipynb
    |           |   |   web-agent-tutorial.ipynb
    |           |   |
    |           |   +---assets
    |           |   |       api-key.png
    |           |   |       hybrid.svg
    |           |   |       sign-up.png
    |           |   |       web-agent.svg
    |           |   |
    |           |   \---supplemental
    |           |       |   vectorize_tutorial.ipynb
    |           |       |
    |           |       +---db
    |           |       |   |   chroma.sqlite3
    |           |       |   |
    |           |       |   \---21729269-38fb-4dfd-8869-770aca3a55f2
    |           |       |           data_level0.bin
    |           |       |           header.bin
    |           |       |           length.bin
    |           |       |           link_lists.bin
    |           |       |
    |           |       \---docs
    |           |               amazon.pdf
    |           |               apple.pdf
    |           |               google.pdf
    |           |               meta.pdf
    |           |               microsoft.pdf
    |           |               tesla.pdf
    |           |
    |           +---ai-memory-with-cognee
    |           |   |   .env.template
    |           |   |   cognee-ai-memory.ipynb
    |           |   |   guido_contributions.html
    |           |   |   README.md
    |           |   |   requirements.txt
    |           |   |
    |           |   \---data
    |           |           cognee_diagram.png
    |           |           copilot_conversations.json
    |           |           guido_contributions.json
    |           |           my_developer_rules.md
    |           |           pep_style_guide.md
    |           |           zen_principles.md
    |           |
    |           +---arcade-secure-tool-calling
    |           |       arcade-diagram.png
    |           |       multiuser-agent-arcade.ipynb
    |           |       README.md
    |           |
    |           +---aws_agentcore
    |           |   |   agentcore_tutorial.ipynb
    |           |   |
    |           |   \---assets
    |           |           agentcore-diagram.png
    |           |
    |           +---docker-intro
    |           |   |   README.md
    |           |   |
    |           |   +---assets
    |           |   |       docker layers 1.png
    |           |   |       docker layers 2.png
    |           |   |       docker-desktop.png
    |           |   |       docker-hub.png
    |           |   |       docker-layers.png
    |           |   |       docker-meme.jpg
    |           |   |       dockerfile to container.png
    |           |   |       reproducibility with Docker.png
    |           |   |       reproducibility without Docker.png
    |           |   |
    |           |   \---examples
    |           |       +---ex1
    |           |       |       Dockerfile
    |           |       |
    |           |       +---ex2
    |           |       |       Dockerfile
    |           |       |
    |           |       +---ex3
    |           |       |       Dockerfile
    |           |       |       hello-world.py
    |           |       |
    |           |       +---ex4
    |           |       |       Dockerfile
    |           |       |       simple_agent.py
    |           |       |
    |           |       \---ex5
    |           |               Dockerfile
    |           |               dynamic_agent.py
    |           |
    |           +---fastapi-agent
    |           |   |   fastapi-agent-tutorial.ipynb
    |           |   |   run_server.bat
    |           |   |   run_server.py
    |           |   |
    |           |   +---scripts
    |           |   |       fastapi_agent.py
    |           |   |
    |           |   \---tests
    |           |           test_fastapi_agent.py
    |           |
    |           +---fine-tuning-agents
    |           |       fine_tuning_agents_guide.ipynb
    |           |
    |           +---LangGraph-agent
    |           |       langgraph_tutorial.ipynb
    |           |
    |           +---on-prem-llm-ollama
    |           |   |   ollama_tutorial.ipynb
    |           |   |   requirements.txt
    |           |   |
    |           |   \---scripts
    |           |           basic_usage.ipynb
    |           |           langchain_agent.ipynb
    |           |
    |           +---runpod-gpu-deploy
    |           |   |   README.md
    |           |   |
    |           |   +---assets
    |           |   |       docker_image_selection.png
    |           |   |       docker_image_update.png
    |           |   |       docker_templates.png
    |           |   |       endpoint_creation_options.png
    |           |   |       endpoint_source_selection.png
    |           |   |       github_integration_update.png
    |           |   |       gpu_prioritization.png
    |           |   |       hardware_selection.png
    |           |   |       signup_add_money.png
    |           |   |       test_request_dashboard.png
    |           |   |       test_request_input.png
    |           |   |       test_request_output.png
    |           |   |       worker_allocation.png
    |           |   |
    |           |   \---crew-ai-ollama-runpod-tutorial
    |           |           Dockerfile
    |           |           handler.py
    |           |           README.md
    |           |           requirements.txt
    |           |           start.sh
    |           |
    |           \---tracing-with-langsmith
    |               |   langsmith_basics.ipynb
    |               |
    |               \---assets
    |                       1.png
    |                       2.png
    |                       3.png
    |                       wiki_agent_td.png
    |
    +---__hooks
    |   \---__starter
    |           file-size-monitor (1).sh
    |           file-size-monitor.sh
    |           markdown-formatter (1).sh
    |           markdown-formatter.sh
    |           README.md
    |           secret-scanner (1).sh
    |           secret-scanner.sh
    |           settings-backup (1).sh
    |           settings-backup.sh
    |           toon-validator (1).sh
    |           toon-validator.sh
    |
    +---__plugins
    |   +---agent-sdk-dev
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   +---agents
    |   |   |       agent-sdk-verifier-py.md
    |   |   |       agent-sdk-verifier-ts.md
    |   |   |
    |   |   \---commands
    |   |           new-sdk-app.md
    |   |
    |   +---ai-engineer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           ai-engineer.md
    |   |
    |   +---analytics-reporter
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           analytics-reporter.md
    |   |
    |   +---analyze-codebase
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           analyze-codebase.md
    |   |
    |   +---analyze-issue
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           analyze-issue.md
    |   |
    |   +---angelos-symbo
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           angelos-symbo.md
    |   |
    |   +---api-integration-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           api-integration-specialist.md
    |   |
    |   +---api-tester
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           api-tester.md
    |   |
    |   +---backend-architect
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           backend-architect.md
    |   |
    |   +---brand-guardian
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           brand-guardian.md
    |   |
    |   +---bug-detective
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           bug-detective.md
    |   |
    |   +---bug-fix
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           bug-fix.md
    |   |
    |   +---ceo-quality-controller-agent
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           ceo-quality-controller-agent.md
    |   |
    |   +---changelog-generator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           changelog-generator.md
    |   |
    |   +---claude-desktop-extension
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           claude-desktop-extension.md
    |   |
    |   +---code-architect
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           code-architect.md
    |   |
    |   +---code-operations-plugin
    |   |   |   README.md
    |   |   |
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---skills
    |   |       +---code-execution
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---examples
    |   |       |           bulk_refactor.py
    |   |       |           codebase_audit.py
    |   |       |           extract_functions.py
    |   |       |
    |   |       +---code-refactor
    |   |       |       SKILL.md
    |   |       |
    |   |       +---code-transfer
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---scripts
    |   |       |           line_insert.py
    |   |       |
    |   |       \---file-operations
    |   |               SKILL.md
    |   |
    |   +---code-review
    |   |   |   README.md
    |   |   |   usage-examples.md
    |   |   |
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           code-review.md
    |   |
    |   +---code-review-assistant
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           code-review-assistant.md
    |   |
    |   +---code-reviewer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           code-reviewer.md
    |   |
    |   +---codebase-documenter
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           codebase-documenter.md
    |   |
    |   +---commit
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           commit.md
    |   |
    |   +---commit-commands
    |   |   \---commands
    |   |           clean_gone.md
    |   |           commit-push-pr.md
    |   |           commit.md
    |   |
    |   +---compliance-automation-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           compliance-automation-specialist.md
    |   |
    |   +---content-creator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           content-creator.md
    |   |
    |   +---context7-docs-fetcher
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           context7-docs-fetcher.md
    |   |
    |   +---continuous-imporvement
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---create-pr
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           create-pr.md
    |   |
    |   +---create-pull-request
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           create-pull-request.md
    |   |
    |   +---create-worktrees
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           create-worktrees.md
    |   |
    |   +---customaize-claude-code
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---data-privacy-engineer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           data-privacy-engineer.md
    |   |
    |   +---data-scientist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           data-scientist.md
    |   |
    |   +---database-performance-optimizer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           database-performance-optimizer.md
    |   |
    |   +---debug-session
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           debug-session.md
    |   |
    |   +---debugger
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           debugger.md
    |   |
    |   +---deployment-engineer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           deployment-engineer.md
    |   |
    |   +---desktop-app-dev
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           desktop-app-dev.md
    |   |
    |   +---devops-automator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           devops-automator.md
    |   |
    |   +---discuss
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           discuss.md
    |   |
    |   +---documentation-generator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           documentation-generator.md
    |   |
    |   +---documentation-management
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---domain-driven-development
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---double-check
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           double-check.md
    |   |
    |   +---engineering-workflow-plugin
    |   |   |   README.md
    |   |   |
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   +---agents
    |   |   |       plan-implementer.md
    |   |   |
    |   |   +---commands
    |   |   |       pr.md
    |   |   |
    |   |   \---skills
    |   |       +---feature-planning
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---references
    |   |       |           planning-best-practices.md
    |   |       |
    |   |       +---git-pushing
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---scripts
    |   |       |           smart_commit.sh
    |   |       |
    |   |       +---review-implementing
    |   |       |       SKILL.md
    |   |       |
    |   |       \---test-fixing
    |   |               SKILL.md
    |   |
    |   +---enterprise-integrator-architect
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           enterprise-integrator-architect.md
    |   |
    |   +---enterprise-onboarding-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           enterprise-onboarding-specialist.md
    |   |
    |   +---enterprise-security-reviewer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           enterprise-security-reviewer.md
    |   |
    |   +---execution-runtime
    |   |   |   .env.example
    |   |   |   pyproject.toml
    |   |   |   README.md
    |   |   |   setup.sh
    |   |   |
    |   |   +---api
    |   |   |       code_analysis.py
    |   |   |       code_transform.py
    |   |   |       filesystem.py
    |   |   |       git_operations.py
    |   |   |       __init__.py
    |   |   |
    |   |   +---execution_runtime
    |   |   |   |   sessions.py
    |   |   |   |   skills.py
    |   |   |   |   __init__.py
    |   |   |   |
    |   |   |   \---security
    |   |   |           import_guard.py
    |   |   |           pii_detector.py
    |   |   |           __init__.py
    |   |   |
    |   |   \---mcp-server
    |   |       |   mcp_server.py
    |   |       |
    |   |       \---security
    |   |               pii_detector.py
    |   |               sandbox.py
    |   |
    |   +---explore
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           explore.md
    |   |
    |   +---feature-dev
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   +---agents
    |   |   |       code-architect.md
    |   |   |       code-explorer.md
    |   |   |       code-reviewer.md
    |   |   |
    |   |   \---commands
    |   |           feature-dev.md
    |   |
    |   +---feedback-synthesizer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           feedback-synthesizer.md
    |   |
    |   +---finance-tracker
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           finance-tracker.md
    |   |
    |   +---fix-github-issue
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           fix-github-issue.md
    |   |
    |   +---fix-issue
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           fix-issue.md
    |   |
    |   +---fix-pr
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           fix-pr.md
    |   |
    |   +---frontend-developer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           frontend-developer.md
    |   |
    |   +---generate-api-docs
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           generate-api-docs.md
    |   |
    |   +---git
    |   |       README.md
    |   |
    |   +---github-issue-fix
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           github-issue-fix.md
    |   |
    |   +---husky
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           husky.md
    |   |
    |   +---infrastructure-maintainer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           infrastructure-maintainer.md
    |   |
    |   +---legal-advisor
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           legal-advisor.md
    |   |
    |   +---lyra-prompt-optimizer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           lyra.md
    |   |
    |   +---mcp
    |   |       README.md
    |   |       recommended-mcp.md
    |   |       usage-examples.md
    |   |
    |   +---mobile-app-builder
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           mobile-app-builder.md
    |   |
    |   +---mobile-ux-optimizer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           mobile-ux-optimizer.md
    |   |
    |   +---model-context-protocol-mcp-expert
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           model-context-protocol-mcp-expert.md
    |   |
    |   +---monitoring-observability-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           monitoring-observability-specialist.md
    |   |
    |   +---n8n-workflow-builder
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           n8n-workflow-builder.md
    |   |
    |   +---onomastophes
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           onomastophes.md
    |   |
    |   +---openapi-expert
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           openapi-expert.md
    |   |
    |   +---optimize
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           optimize.md
    |   |
    |   +---performance-benchmarker
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           performance-benchmarker.md
    |   |
    |   +---plan
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           plan.md
    |   |
    |   +---planning-prd-agent
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           planning-prd-agent.md
    |   |
    |   +---pr-issue-resolve
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           pr-issue-resolve.md
    |   |
    |   +---pr-review
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           pr-review.md
    |   |
    |   +---pr-review-toolkit
    |   |   |   README.md
    |   |   |
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   +---agents
    |   |   |       code-reviewer.md
    |   |   |       code-simplifier.md
    |   |   |       comment-analyzer.md
    |   |   |       pr-test-analyzer.md
    |   |   |       silent-failure-hunter.md
    |   |   |       type-design-analyzer.md
    |   |   |
    |   |   \---commands
    |   |           review-pr.md
    |   |
    |   +---prd-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           prd-specialist.md
    |   |
    |   +---problem-solver-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           problem-solver-specialist.md
    |   |
    |   +---productivity-skills-plugin
    |   |   |   README.md
    |   |   |
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---skills
    |   |       +---code-auditor
    |   |       |       SKILL.md
    |   |       |
    |   |       +---codebase-documenter
    |   |       |       SKILL.md
    |   |       |
    |   |       +---conversation-analyzer
    |   |       |   |   SKILL.md
    |   |       |   |
    |   |       |   \---scripts
    |   |       |           analyze_history.py
    |   |       |
    |   |       \---project-bootstrapper
    |   |               SKILL.md
    |   |
    |   +---project-curator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           project-curator.md
    |   |
    |   +---python-expert
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           python-expert.md
    |   |
    |   +---rapid-prototyper
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           rapid-prototyper.md
    |   |
    |   +---react-native-dev
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           react-native-dev.md
    |   |
    |   +---reflexion
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---refractor
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           refractor.md
    |   |
    |   +---security-guidance
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---hooks
    |   |           hooks.json
    |   |           security_reminder_hook.py
    |   |
    |   +---spec-driven-development
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---sprint-prioritizer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           sprint-prioritizer.md
    |   |
    |   +---standardize-claude-code
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---studio-coach
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           studio-coach.md
    |   |
    |   +---studio-producer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           studio-producer.md
    |   |
    |   +---sub-agent-driven-development
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---support-responder
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           support-responder.md
    |   |
    |   +---test-driven-development
    |   |       README.md
    |   |       usage-examples.md
    |   |
    |   +---test-file
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           test-file.md
    |   |
    |   +---test-results-analyzer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           test-results-analyzer.md
    |   |
    |   +---test-writer-fixer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           test-writer-fixer.md
    |   |
    |   +---tool-evaluator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           tool-evaluator.md
    |   |
    |   +---trend-researcher
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           trend-researcher.md
    |   |
    |   +---ui-designer
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           ui-designer.md
    |   |
    |   +---unit-test-generator
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           unit-test-generator.md
    |   |
    |   +---update-branch-name
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           update-branch-name.md
    |   |
    |   +---update-claudemd
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---commands
    |   |           update-claudemd.md
    |   |
    |   +---ux-researcher
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           ux-researcher.md
    |   |
    |   +---vision-specialist
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           vision-specialist.md
    |   |
    |   +---visual-documentation-plugin
    |   |   |   EXAMPLES.md
    |   |   |   README.md
    |   |   |
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   +---skills
    |   |   |   +---architecture-diagram-creator
    |   |   |   |   |   SKILL.md
    |   |   |   |   |
    |   |   |   |   +---assets
    |   |   |   |   |   \---templates
    |   |   |   |   |           architecture_components.html
    |   |   |   |   |           base_template.html
    |   |   |   |   |
    |   |   |   |   \---references
    |   |   |   |           example_architecture.html
    |   |   |   |
    |   |   |   +---dashboard-creator
    |   |   |   |   |   SKILL.md
    |   |   |   |   |
    |   |   |   |   +---assets
    |   |   |   |   |   \---templates
    |   |   |   |   |           base_template.html
    |   |   |   |   |           dashboard_components.html
    |   |   |   |   |
    |   |   |   |   \---references
    |   |   |   |           design_patterns.md
    |   |   |   |           svg_library.md
    |   |   |   |
    |   |   |   +---flowchart-creator
    |   |   |   |   |   SKILL.md
    |   |   |   |   |
    |   |   |   |   +---assets
    |   |   |   |   |   \---templates
    |   |   |   |   |           base_template.html
    |   |   |   |   |           flowchart_components.html
    |   |   |   |   |
    |   |   |   |   \---references
    |   |   |   |           design_patterns.md
    |   |   |   |           svg_library.md
    |   |   |   |
    |   |   |   +---technical-doc-creator
    |   |   |   |   |   SKILL.md
    |   |   |   |   |
    |   |   |   |   +---assets
    |   |   |   |   |   \---templates
    |   |   |   |   |           base_template.html
    |   |   |   |   |
    |   |   |   |   \---references
    |   |   |   |           design_patterns.md
    |   |   |   |           svg_library.md
    |   |   |   |
    |   |   |   \---timeline-creator
    |   |   |       |   SKILL.md
    |   |   |       |
    |   |   |       +---assets
    |   |   |       |   \---templates
    |   |   |       |           base_template.html
    |   |   |       |           timeline_components.html
    |   |   |       |
    |   |   |       \---references
    |   |   |               design_patterns.md
    |   |   |               svg_library.md
    |   |   |
    |   |   \---test-outputs
    |   |           dashboard-test-monitoring.html
    |   |           flowchart-test-authentication.html
    |   |
    |   +---visual-storyteller
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           visual-storyteller.md
    |   |
    |   +---web-dev
    |   |   +---.claude-plugin
    |   |   |       plugin.json
    |   |   |
    |   |   \---agents
    |   |           web-dev.md
    |   |
    |   \---workflow-optimizer
    |       +---.claude-plugin
    |       |       plugin.json
    |       |
    |       \---agents
    |               workflow-optimizer.md
    |
    +---__resouce-lists
    |       awesome-ai-coding-tools.md
    |
    +---__scripts
    |       add_category.py
    |       add_removed_column.py
    |       add_resource.py
    |       badge_issue_notification.py
    |       badge_notification_core.py
    |       category_utils.py
    |       create_resource_pr.py
    |       download_resources.py
    |       fetch_repo_ticker_data.py
    |       generate_logo_svgs.py
    |       generate_readme.py
    |       generate_readme_bak.py
    |       generate_readme_bak_2.py
    |       generate_resource_id.py
    |       generate_ticker_svg.py
    |       git_utils.py
    |       manual_badge_notification.py
    |       parse_issue_form.py
    |       process_resources_to_csv.py
    |       quick_id.py
    |       resource_id.py
    |       sort_resources.py
    |       submit_resource.py
    |       validate_links.py
    |       validate_new_resource.py
    |       validate_single_resource.py
    |       __init__.py
    |
    +---__skills
    |   |   agentic-resouce-list.md
    |   |
    |   +---algorithmic-art
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   \---templates
    |   |           generator_template.js
    |   |           viewer.html
    |   |
    |   +---article-extractor
    |   |       SKILL.md
    |   |
    |   +---artifacts-builder
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   \---scripts
    |   |           bundle-artifact.sh
    |   |           init-artifact.sh
    |   |           shadcn-components.tar.gz
    |   |
    |   +---brainstorming-general
    |   |       SKILL.md
    |   |
    |   +---brainstrorming-domain-name
    |   |       SKILL.md
    |   |
    |   +---brand-guidelines
    |   |       LICENSE.txt
    |   |       SKILL.md
    |   |
    |   +---canvas-design
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   \---canvas-fonts
    |   |           ArsenalSC-OFL.txt
    |   |           ArsenalSC-Regular.ttf
    |   |           BigShoulders-Bold.ttf
    |   |           BigShoulders-OFL.txt
    |   |           BigShoulders-Regular.ttf
    |   |           Boldonse-OFL.txt
    |   |           Boldonse-Regular.ttf
    |   |           BricolageGrotesque-Bold.ttf
    |   |           BricolageGrotesque-OFL.txt
    |   |           BricolageGrotesque-Regular.ttf
    |   |           CrimsonPro-Bold.ttf
    |   |           CrimsonPro-Italic.ttf
    |   |           CrimsonPro-OFL.txt
    |   |           CrimsonPro-Regular.ttf
    |   |           DMMono-OFL.txt
    |   |           DMMono-Regular.ttf
    |   |           EricaOne-OFL.txt
    |   |           EricaOne-Regular.ttf
    |   |           GeistMono-Bold.ttf
    |   |           GeistMono-OFL.txt
    |   |           GeistMono-Regular.ttf
    |   |           Gloock-OFL.txt
    |   |           Gloock-Regular.ttf
    |   |           IBMPlexMono-Bold.ttf
    |   |           IBMPlexMono-OFL.txt
    |   |           IBMPlexMono-Regular.ttf
    |   |           IBMPlexSerif-Bold.ttf
    |   |           IBMPlexSerif-BoldItalic.ttf
    |   |           IBMPlexSerif-Italic.ttf
    |   |           IBMPlexSerif-Regular.ttf
    |   |           InstrumentSans-Bold.ttf
    |   |           InstrumentSans-BoldItalic.ttf
    |   |           InstrumentSans-Italic.ttf
    |   |           InstrumentSans-OFL.txt
    |   |           InstrumentSans-Regular.ttf
    |   |           InstrumentSerif-Italic.ttf
    |   |           InstrumentSerif-Regular.ttf
    |   |           Italiana-OFL.txt
    |   |           Italiana-Regular.ttf
    |   |           JetBrainsMono-Bold.ttf
    |   |           JetBrainsMono-OFL.txt
    |   |           JetBrainsMono-Regular.ttf
    |   |           Jura-Light.ttf
    |   |           Jura-Medium.ttf
    |   |           Jura-OFL.txt
    |   |           LibreBaskerville-OFL.txt
    |   |           LibreBaskerville-Regular.ttf
    |   |           Lora-Bold.ttf
    |   |           Lora-BoldItalic.ttf
    |   |           Lora-Italic.ttf
    |   |           Lora-OFL.txt
    |   |           Lora-Regular.ttf
    |   |           NationalPark-Bold.ttf
    |   |           NationalPark-OFL.txt
    |   |           NationalPark-Regular.ttf
    |   |           NothingYouCouldDo-OFL.txt
    |   |           NothingYouCouldDo-Regular.ttf
    |   |           Outfit-Bold.ttf
    |   |           Outfit-OFL.txt
    |   |           Outfit-Regular.ttf
    |   |           PixelifySans-Medium.ttf
    |   |           PixelifySans-OFL.txt
    |   |           PoiretOne-OFL.txt
    |   |           PoiretOne-Regular.ttf
    |   |           RedHatMono-Bold.ttf
    |   |           RedHatMono-OFL.txt
    |   |           RedHatMono-Regular.ttf
    |   |           Silkscreen-OFL.txt
    |   |           Silkscreen-Regular.ttf
    |   |           SmoochSans-Medium.ttf
    |   |           SmoochSans-OFL.txt
    |   |           Tektur-Medium.ttf
    |   |           Tektur-OFL.txt
    |   |           Tektur-Regular.ttf
    |   |           WorkSans-Bold.ttf
    |   |           WorkSans-BoldItalic.ttf
    |   |           WorkSans-Italic.ttf
    |   |           WorkSans-OFL.txt
    |   |           WorkSans-Regular.ttf
    |   |           YoungSerif-OFL.txt
    |   |           YoungSerif-Regular.ttf
    |   |
    |   +---changelog-generator
    |   |       SKILL.md
    |   |
    |   +---content-research-writer
    |   |       SKILL.md
    |   |
    |   +---d3.js Visualisation
    |   |   |   SKILL.md
    |   |   |
    |   |   +---assets
    |   |   |       chart-template.jsx
    |   |   |       interactive-template.jsx
    |   |   |       sample-data.json
    |   |   |
    |   |   \---references
    |   |           colour-schemes.md
    |   |           d3-patterns.md
    |   |           scale-reference.md
    |   |
    |   +---developer-growth-analysis
    |   |       SKILL.md
    |   |
    |   +---dispatching-parallel-agents
    |   |       SKILL.md
    |   |
    |   +---doc-coauthoring
    |   |       SKILL.md
    |   |
    |   +---docx
    |   |   |   docx-js.md
    |   |   |   LICENSE.txt
    |   |   |   ooxml.md
    |   |   |   SKILL.md
    |   |   |
    |   |   +---ooxml
    |   |   |   +---schemas
    |   |   |   |   +---ecma
    |   |   |   |   |   \---fouth-edition
    |   |   |   |   |           opc-contentTypes.xsd
    |   |   |   |   |           opc-coreProperties.xsd
    |   |   |   |   |           opc-digSig.xsd
    |   |   |   |   |           opc-relationships.xsd
    |   |   |   |   |
    |   |   |   |   +---ISO-IEC29500-4_2016
    |   |   |   |   |       dml-chart.xsd
    |   |   |   |   |       dml-chartDrawing.xsd
    |   |   |   |   |       dml-diagram.xsd
    |   |   |   |   |       dml-lockedCanvas.xsd
    |   |   |   |   |       dml-main.xsd
    |   |   |   |   |       dml-picture.xsd
    |   |   |   |   |       dml-spreadsheetDrawing.xsd
    |   |   |   |   |       dml-wordprocessingDrawing.xsd
    |   |   |   |   |       pml.xsd
    |   |   |   |   |       shared-additionalCharacteristics.xsd
    |   |   |   |   |       shared-bibliography.xsd
    |   |   |   |   |       shared-commonSimpleTypes.xsd
    |   |   |   |   |       shared-customXmlDataProperties.xsd
    |   |   |   |   |       shared-customXmlSchemaProperties.xsd
    |   |   |   |   |       shared-documentPropertiesCustom.xsd
    |   |   |   |   |       shared-documentPropertiesExtended.xsd
    |   |   |   |   |       shared-documentPropertiesVariantTypes.xsd
    |   |   |   |   |       shared-math.xsd
    |   |   |   |   |       shared-relationshipReference.xsd
    |   |   |   |   |       sml.xsd
    |   |   |   |   |       vml-main.xsd
    |   |   |   |   |       vml-officeDrawing.xsd
    |   |   |   |   |       vml-presentationDrawing.xsd
    |   |   |   |   |       vml-spreadsheetDrawing.xsd
    |   |   |   |   |       vml-wordprocessingDrawing.xsd
    |   |   |   |   |       wml.xsd
    |   |   |   |   |       xml.xsd
    |   |   |   |   |
    |   |   |   |   +---mce
    |   |   |   |   |       mc.xsd
    |   |   |   |   |
    |   |   |   |   \---microsoft
    |   |   |   |           wml-2010.xsd
    |   |   |   |           wml-2012.xsd
    |   |   |   |           wml-2018.xsd
    |   |   |   |           wml-cex-2018.xsd
    |   |   |   |           wml-cid-2016.xsd
    |   |   |   |           wml-sdtdatahash-2020.xsd
    |   |   |   |           wml-symex-2015.xsd
    |   |   |   |
    |   |   |   \---scripts
    |   |   |       |   pack.py
    |   |   |       |   unpack.py
    |   |   |       |   validate.py
    |   |   |       |
    |   |   |       \---validation
    |   |   |               base.py
    |   |   |               docx.py
    |   |   |               pptx.py
    |   |   |               redlining.py
    |   |   |               __init__.py
    |   |   |
    |   |   \---scripts
    |   |       |   document.py
    |   |       |   utilities.py
    |   |       |   __init__.py
    |   |       |
    |   |       \---templates
    |   |               comments.xml
    |   |               commentsExtended.xml
    |   |               commentsExtensible.xml
    |   |               commentsIds.xml
    |   |               people.xml
    |   |
    |   +---epub-conversion
    |   |   |   changelog-helper.py
    |   |   |   CHANGELOG.md
    |   |   |   CLAUDE.md
    |   |   |   publish.sh
    |   |   |   README.md
    |   |   |   test_document.md
    |   |   |   test_epub_skill.py
    |   |   |   test_output.epub
    |   |   |   test_tables.epub
    |   |   |   test_tables.md
    |   |   |
    |   |   \---markdown-to-epub
    |   |       |   REFERENCE.md
    |   |       |   requirements.txt
    |   |       |   SKILL.md
    |   |       |
    |   |       \---scripts
    |   |               epub_generator.py
    |   |               markdown_processor.py
    |   |
    |   +---executing-plans
    |   |       SKILL.md
    |   |
    |   +---ffuf-skill
    |   |   |   ffuf_helper.py
    |   |   |   SKILL.md
    |   |   |
    |   |   \---resources
    |   |           REQUEST_TEMPLATES.md
    |   |           WORDLISTS.md
    |   |
    |   +---file-organizer
    |   |       SKILL.md
    |   |
    |   +---finishing-a-development-branch
    |   |       SKILL.md
    |   |
    |   +---frontend-design
    |   |       LICENSE.txt
    |   |       SKILL.md
    |   |
    |   +---image-enhancer
    |   |       SKILL.md
    |   |
    |   +---internal-comms
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   \---examples
    |   |           3p-updates.md
    |   |           company-newsletter.md
    |   |           faq-answers.md
    |   |           general-comms.md
    |   |
    |   +---lead-research-assistant
    |   |       SKILL.md
    |   |
    |   +---mcp-builder
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   +---reference
    |   |   |       evaluation.md
    |   |   |       mcp_best_practices.md
    |   |   |       node_mcp_server.md
    |   |   |       python_mcp_server.md
    |   |   |
    |   |   \---scripts
    |   |           connections.py
    |   |           evaluation.py
    |   |           example_evaluation.xml
    |   |           requirements.txt
    |   |
    |   +---pdf
    |   |   |   forms.md
    |   |   |   LICENSE.txt
    |   |   |   reference.md
    |   |   |   SKILL.md
    |   |   |
    |   |   \---scripts
    |   |           check_bounding_boxes.py
    |   |           check_bounding_boxes_test.py
    |   |           check_fillable_fields.py
    |   |           convert_pdf_to_images.py
    |   |           create_validation_image.py
    |   |           extract_form_field_info.py
    |   |           fill_fillable_fields.py
    |   |           fill_pdf_form_with_annotations.py
    |   |
    |   +---pptx
    |   |   |   html2pptx.md
    |   |   |   LICENSE.txt
    |   |   |   ooxml.md
    |   |   |   SKILL.md
    |   |   |
    |   |   +---ooxml
    |   |   |   +---schemas
    |   |   |   |   +---ecma
    |   |   |   |   |   \---fouth-edition
    |   |   |   |   |           opc-contentTypes.xsd
    |   |   |   |   |           opc-coreProperties.xsd
    |   |   |   |   |           opc-digSig.xsd
    |   |   |   |   |           opc-relationships.xsd
    |   |   |   |   |
    |   |   |   |   +---ISO-IEC29500-4_2016
    |   |   |   |   |       dml-chart.xsd
    |   |   |   |   |       dml-chartDrawing.xsd
    |   |   |   |   |       dml-diagram.xsd
    |   |   |   |   |       dml-lockedCanvas.xsd
    |   |   |   |   |       dml-main.xsd
    |   |   |   |   |       dml-picture.xsd
    |   |   |   |   |       dml-spreadsheetDrawing.xsd
    |   |   |   |   |       dml-wordprocessingDrawing.xsd
    |   |   |   |   |       pml.xsd
    |   |   |   |   |       shared-additionalCharacteristics.xsd
    |   |   |   |   |       shared-bibliography.xsd
    |   |   |   |   |       shared-commonSimpleTypes.xsd
    |   |   |   |   |       shared-customXmlDataProperties.xsd
    |   |   |   |   |       shared-customXmlSchemaProperties.xsd
    |   |   |   |   |       shared-documentPropertiesCustom.xsd
    |   |   |   |   |       shared-documentPropertiesExtended.xsd
    |   |   |   |   |       shared-documentPropertiesVariantTypes.xsd
    |   |   |   |   |       shared-math.xsd
    |   |   |   |   |       shared-relationshipReference.xsd
    |   |   |   |   |       sml.xsd
    |   |   |   |   |       vml-main.xsd
    |   |   |   |   |       vml-officeDrawing.xsd
    |   |   |   |   |       vml-presentationDrawing.xsd
    |   |   |   |   |       vml-spreadsheetDrawing.xsd
    |   |   |   |   |       vml-wordprocessingDrawing.xsd
    |   |   |   |   |       wml.xsd
    |   |   |   |   |       xml.xsd
    |   |   |   |   |
    |   |   |   |   +---mce
    |   |   |   |   |       mc.xsd
    |   |   |   |   |
    |   |   |   |   \---microsoft
    |   |   |   |           wml-2010.xsd
    |   |   |   |           wml-2012.xsd
    |   |   |   |           wml-2018.xsd
    |   |   |   |           wml-cex-2018.xsd
    |   |   |   |           wml-cid-2016.xsd
    |   |   |   |           wml-sdtdatahash-2020.xsd
    |   |   |   |           wml-symex-2015.xsd
    |   |   |   |
    |   |   |   \---scripts
    |   |   |       |   pack.py
    |   |   |       |   unpack.py
    |   |   |       |   validate.py
    |   |   |       |
    |   |   |       \---validation
    |   |   |               base.py
    |   |   |               docx.py
    |   |   |               pptx.py
    |   |   |               redlining.py
    |   |   |               __init__.py
    |   |   |
    |   |   \---scripts
    |   |           html2pptx.js
    |   |           inventory.py
    |   |           rearrange.py
    |   |           replace.py
    |   |           thumbnail.py
    |   |
    |   +---prompt-engineering-patterns
    |   |       SKILL.md
    |   |
    |   +---receiving-code-review
    |   |       SKILL.md
    |   |
    |   +---requesting-code-review
    |   |       code-reviewer.md
    |   |       SKILL.md
    |   |
    |   +---ship-learn-next+action-planner
    |   |       SKILL.md
    |   |
    |   +---skill-creator
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   +---references
    |   |   |       output-patterns.md
    |   |   |       workflows.md
    |   |   |
    |   |   \---scripts
    |   |           init_skill.py
    |   |           package_skill.py
    |   |           quick_validate.py
    |   |
    |   +---slack-gif-creator
    |   |   |   LICENSE.txt
    |   |   |   requirements.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   \---core
    |   |           easing.py
    |   |           frame_composer.py
    |   |           gif_builder.py
    |   |           validators.py
    |   |
    |   +---subagent-driven-development
    |   |       code-quality-reviewer-prompt.md
    |   |       implementer-prompt.md
    |   |       SKILL.md
    |   |       spec-reviewer-prompt.md
    |   |
    |   +---systematic-debugging
    |   |       condition-based-waiting-example.ts
    |   |       condition-based-waiting.md
    |   |       CREATION-LOG.md
    |   |       defense-in-depth.md
    |   |       find-polluter.sh
    |   |       root-cause-tracing.md
    |   |       SKILL.md
    |   |       test-academic.md
    |   |       test-pressure-1.md
    |   |       test-pressure-2.md
    |   |       test-pressure-3.md
    |   |
    |   +---temp_extract
    |   |   \---terminal-title
    |   |       |   SKILL.md
    |   |       |
    |   |       \---scripts
    |   |               set_title.sh
    |   |
    |   +---test-driven-development
    |   |       SKILL.md
    |   |       testing-anti-patterns.md
    |   |
    |   +---theme-factory
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |   theme-showcase.pdf
    |   |   |
    |   |   \---themes
    |   |           arctic-frost.md
    |   |           botanical-garden.md
    |   |           desert-rose.md
    |   |           forest-canopy.md
    |   |           golden-hour.md
    |   |           midnight-galaxy.md
    |   |           modern-minimalist.md
    |   |           ocean-depths.md
    |   |           sunset-boulevard.md
    |   |           tech-innovation.md
    |   |
    |   +---unified-content-extraction-action-planning
    |   |       SKILL.md
    |   |
    |   +---using-git-worktrees
    |   |       SKILL.md
    |   |
    |   +---using-superpowers
    |   |       SKILL.md
    |   |
    |   +---verification-before-completion
    |   |       SKILL.md
    |   |
    |   +---video-downloader
    |   |       SKILL.md
    |   |
    |   +---web-artifacts-builder
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   \---scripts
    |   |           bundle-artifact.sh
    |   |           init-artifact.sh
    |   |           shadcn-components.tar.gz
    |   |
    |   +---webapp-testing
    |   |   |   LICENSE.txt
    |   |   |   SKILL.md
    |   |   |
    |   |   +---examples
    |   |   |       console_logging.py
    |   |   |       element_discovery.py
    |   |   |       static_html_automation.py
    |   |   |
    |   |   \---scripts
    |   |           with_server.py
    |   |
    |   +---writing-plans
    |   |       SKILL.md
    |   |
    |   +---writing-skills
    |   |   |   anthropic-best-practices.md
    |   |   |   graphviz-conventions.dot
    |   |   |   persuasion-principles.md
    |   |   |   render-graphs.js
    |   |   |   SKILL.md
    |   |   |   testing-skills-with-subagents.md
    |   |   |
    |   |   \---examples
    |   |           CLAUDE_MD_TESTING.md
    |   |
    |   +---xlsx
    |   |       LICENSE.txt
    |   |       recalc.py
    |   |       SKILL.md
    |   |
    |   +---youtube-transcript
    |   |       SKILL.md
    |   |
    |   +---__skill-template
    |   |       SKILL.md
    |   |
    |   \---__skills-anthropic-expert
    |       |   skill.json
    |       |   skill.md
    |       |
    |       +---claude-code
    |       |       skill.json
    |       |       skill.md
    |       |
    |       +---claude-command-builder
    |       |       skill.json
    |       |       skill.md
    |       |
    |       +---claude-hook-builder
    |       |       skill.json
    |       |       skill.md
    |       |
    |       +---claude-mcp-expert
    |       |       skill.json
    |       |       skill.md
    |       |
    |       +---claude-settings-expert
    |       |       skill.json
    |       |       skill.md
    |       |
    |       \---claude-skill-builder
    |               skill.json
    |               skill.md
    |
    \---___README
        |   best-practices.md
        |   claude-code-hooks-docs.md
        |   claude-code-settings-docs.md
        |   claude-code-slash-commands-docs.md
        |   claude-code-subagents-docs.md
        |   concepts.md
        |   my-linear-guide.md
        |   README (1).md
        |   README.md
        |   settings.json.example
        |
        \---__guidence-for-the-pkb-assistants
                anthropic-offical-claude-code-documents.md
                brainstorming-to-implementation.md
                bug-investigation.md
                ci-integration.md
                code-quality-improvement.md
                custom-extensions.md
                feature-development.md
                file-structure-context.md
                mcp-tooling-guide.md
                planning-instructions.md
                pr-review.md
                project-setup.md
                spec-driven-development.md
