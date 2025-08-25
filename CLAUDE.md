# Development Guide for Claude

Welcome to the **Email ETL and 5-Layer Archival System** repository. This system provides comprehensive email processing, archival, and workflow automation for organizations with browser-only email access.

**Your primary source of truth for all development tasks is `AGENTS.md`.**

**MANDATORY CONTEXT7 USAGE**: Before implementing any features or resolving problems, you MUST use the context7 MCP server with "use context7" in your queries to verify current documentation and best practices.

## 🎯 Context-Aware Command Selection

### 🏭 Production Environment (End Users - Email Processing)
**When to use**: Deployed system, actual email processing, production runs
```bash
./run                           # Complete production pipeline
                               # - Auto-installs UV if needed
                               # - Sets up environment automatically  
                               # - Connects to Chrome/Outlook PWA
                               # - Presents email conversion menu
```

### 🛠️ Development Environment (Claude Code - Code Development)
**When to use**: Code development, testing, debugging, quality assurance in Claude Code
```bash
# Environment setup
uv sync --dev                   # Install development dependencies

# Code quality (use these during development in Claude Code)
uv run ruff check --fix src/    # Auto-fix linting issues (10-100x faster than flake8)
uv run ruff format src/         # Format code (Black-compatible, 10-100x faster)
uv run mypy src/                # Type checking
uv run bandit -r src/           # Security scanning

# Testing
uv run pytest tests/            # Run test suite

# Development utilities
uv run playwright install chromium  # Install browser for automation
```

### 📋 Context-Specific Guidelines for Claude

#### During Code Development:
- **Always use `uv run` commands** for quality assurance
- **Run `uv run ruff check --fix src/` before committing** code changes
- **Use `uv run pytest tests/`** to verify functionality
- **Leverage context7** to verify current best practices

#### During Production Setup/Testing:
- **Use `./run` for end-user operations** and testing production flow
- **Never mix development and production commands** in same context

#### Never Do:
- Don't use development commands (`uv run`) in production contexts
- Don't use production commands (`./run`) when doing code development
- Don't implement features without first using context7 for verification

## Key Topics Covered in AGENTS.md

- **System Architecture**: Complete 5-layer redundant archival approach
- **Browser Automation**: Playwright-based email downloads from Outlook PWA
- **Multi-Client Integration**: Evolution, Thunderbird, and PST export support
- **Task Extraction**: Business-specific pattern recognition and workflow generation
- **Cross-Platform Requirements**: Linux development with Windows office PC compatibility
- **Authentication Handling**: Browser-based MFA-compatible login processes
- **Database Schema**: DuckDB tables for emails, tasks, and relationships
- **Development Workflow**: Testing, validation, and deployment procedures

## System Components Overview

This repository implements:

### Keyword Frequency Analysis Script

The codebase includes a simple script (`run.py`) for **keyword extraction and frequency analysis**. This tool processes all `.txt` files in a directory, extracts keywords, counts their occurrences, and generates both a CSV and a bar chart of the most frequent keywords.

**Objective:** Enable quick analysis of dataset composition, support metadata generation, and facilitate downstream processing tasks.

**Development Notes:**
- The script is standalone and does not require additional configuration.
- Output files (`keyword_frequency.csv`, `top_keywords_bar_chart.png`) are generated in the working directory.
- Use this utility for initial dataset exploration or to inform further ETL pipeline development.

Running with UV (recommended):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync --dev
uv run python run.py --input-dir ./ --output-csv keyword_frequency.csv
```

Local CI preference: this repository provides an offline local CI runner
(`scripts/local_ci.sh`) and git hook template to run checks before push.
These are optional and must be installed manually via
`./scripts/install-hooks.sh`. No remote CI is configured by default.

## Quick Start Reference

Before developing, ensure you understand:
1. The 5-layer archival architecture
2. Business-specific task patterns (Kyocera, Staff, Financial, Equipment, BCM)
3. Multi-platform integration requirements
4. Browser automation constraints and capabilities

[**📖 Read the Complete Agent Development Guide (AGENTS.md)**](./AGENTS.md)

---

**Important**: This system is designed for organizations that can only access email through web browsers. All development must support browser-based workflows and create multiple redundant archives.

## Commit and Version Control Guidelines

**MANDATORY COMMIT NAMING SCHEMA**: All commits must follow `YYYYMMDD-HHMM-short-descriptor` format
- Date and time first (local timezone)
- Short descriptor (2-4 words) describing main implementation
- Example: `20250822-1435-docker-style-progress`

**BRANCH NAMING**: Use `feature/YYYYMMDD-short-descriptor` for feature branches

**COMMIT MESSAGES**: Must include:
- Detailed description of user-appreciated implementations
- Outstanding issues that need immediate attention
- Reference to specification updates in AGENTS.md

**DOCUMENTATION UPDATES**: Always update AGENTS.md with new specifications when implementing user-requested features.

**MANDATORY MCP SERVER VERIFICATION**: When resolving problems or implementing features:
- **ALWAYS** use context7 MCP server to check latest documentation and best practices with "use context7" in queries
- **ALWAYS** use Playwright MCP server instead of creating duplicate browser automation
- **VERIFY BEFORE IMPLEMENT**: It is better to use MCP servers to verify and be certain rather than assume or guess
- **UP-TO-DATE COMPLIANCE**: Ensure implementation follows current standards by checking via MCP servers
- **NO SCRIPT PROLIFERATION**: Never create multiple scripts to solve single issues - consolidate functionality within existing modules

## Implementation Strategy - Outlook PWA Improvements

**CRITICAL PRIORITY PHASES** (Based on docs/Outlook-PWA-Email-Extraction.md):

### Phase 1: Authentication & Framework Migration (WEEK 1)
- Replace Selenium with Microsoft Playwright for 80% reliability improvement
- Implement TOTP authentication using PyOTP library
- Configure persistent session management with `context.storage_state()`
- Add certificate-based authentication support

### Phase 2: DOM Extraction Resilience (WEEK 2)
- Implement multiple fallback selectors using role-based attributes
- Add JavaScript injection for direct email data access
- Create element stability testing framework
- Use data-testid and ARIA labels over CSS classes

### Phase 3: Infrastructure Hardening (WEEK 3)
- Docker containerization for 65% reduction in environment failures
- Configure Xvfb for headless automation
- Implement human-like interaction patterns with 2-5 second delays
- Add exponential backoff retry mechanisms

### Phase 4: DuckDB Migration (WEEK 4)
- Implement DuckDB for 75-95% compression rates
- Create normalized schema for emails, recipients, headers, attachments
- Add full-text search with BM25 scoring
- Optimize for sub-second query performance

### Phase 5-6: Integration & Task Extraction (WEEKS 5-6)
- Multi-client support (Evolution, Thunderbird, PST)
- Enhanced business-specific task pattern recognition
- Workflow document generation automation

## Code Quality Requirements

**MANDATORY VERIFICATION WORKFLOW**:
1. Query context7 with "use context7" before implementing
2. Run `ruff check src/` and `ruff format src/` before commits
3. Execute `pytest tests/` for comprehensive testing
4. Use `mypy src/` for type checking
5. Run `bandit src/` for security scanning

**ANTI-SCRIPT PROLIFERATION**: Consolidate all functionality within existing modules. Never create multiple scripts to solve single issues.

# Important Instruction Reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
ALWAYS use context7 MCP server to verify current best practices before implementation.
