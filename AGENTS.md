# AGENTS.md - Email ETL and 5-Layer Archival System

This document provides AI agents with project-specific instructions for developing and maintaining the **Email ETL and 5-Layer Archival System**. This serves as the **definitive specification source** following the [agents.md standard](https://agents.md/).

## Project Overview

This repository implements a **Complete Email Archival Solution** for organizations that can only access email through browser-based interfaces (Outlook PWA). The system creates **5 redundant archive layers** to ensure data preservation, accessibility, and workflow integration.

## 🎯 Context-Aware Command Reference
## Keyword Extraction Utility

This repository includes a utility script for **keyword extraction and frequency analysis** from text-based datasets. The script (`run.py`) scans all `.txt` files in a directory, extracts comma-separated keywords, counts their frequencies, and outputs both a CSV summary and a bar chart visualization of the top keywords.

**Purpose:** Supports rapid dataset analysis, metadata tagging, and downstream workflow automation by providing a clear overview of keyword distributions in training or archival data.

**Key Features:**
- Automated keyword extraction from all `.txt` files
- Frequency counting and CSV export
- Top keyword visualization (bar chart)
- No external configuration required; runs as a standalone analysis tool

To run this utility inside the project's UV-managed environment (recommended):

```bash
# Install UV (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies declared in pyproject.toml
uv sync --dev

# Run the utility
uv run python run.py --input-dir . --output-csv keyword_frequency.csv --top 20
```

**CRITICAL FOR AI AGENTS**: This project maintains strict separation between production and development tooling to ensure proper context usage.

### 🏭 Production Commands (End Users - Email Processing)
**Context**: Deployed system, actual email processing, production runs
```bash
./run                           # SINGLE ENTRY POINT for all production functionality
                               # - Automated environment setup (UV installation)
                               # - Chrome browser detection and connection  
                               # - Outlook PWA integration and email conversion
                               # - Zero-configuration user experience
```

### 🛠️ Development Commands (AI Agents - Code Development)
**Context**: Code development, testing, debugging, quality assurance
```bash
# Environment setup (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh  # Install UV package manager
uv sync --dev                   # Install all dev dependencies

# Code quality pipeline (use during development)
uv run ruff check --fix src/    # Auto-fix linting (10-100x faster than flake8)
uv run ruff format src/         # Format code (Black-compatible)
uv run mypy src/                # Type checking with strict mode
uv run bandit -r src/           # Security vulnerability scanning
uv run pytest tests/            # Comprehensive test execution

# Browser automation setup
uv run playwright install chromium  # Install browser for automation testing
```

### 📋 Context Guidelines for AI Agents

#### ✅ **DO - During Code Development:**
- Use `uv run` commands for all development tasks
- Always run `uv run ruff check --fix src/` before code commits
- Verify with `uv run pytest tests/` after making changes
- Use context7 to verify current best practices

#### ✅ **DO - During Production Testing:**
- Use `./run` to test end-user experience
- Test complete pipeline functionality as users would experience it

#### ❌ **DON'T - Never Mix Contexts:**
- Don't use `uv run` commands in production contexts
- Don't use `./run` when doing code development tasks
- Don't implement without context7 verification

### 🚀 Modern Python Tooling (2025 Standards)

#### UV Package Manager Benefits (vs pip/venv):
- **10-100x faster** dependency resolution and installation
- **Unified tooling** - Replaces pip, venv, pip-tools, virtualenv
- **Automatic virtual environments** - No manual activation needed
- **Universal lockfiles** - Reproducible builds across systems
- **Built-in Python management** - Version switching capabilities

#### Ruff Linter/Formatter Benefits (vs Black/Flake8/isort):
- **10-100x faster** than traditional tools (written in Rust)
- **800+ built-in rules** with automatic fixing capabilities
- **Single tool consolidation** - Replaces 4-5 traditional tools
- **Black-compatible formatting** - Seamless migration
- **Zero configuration** - Works out of the box

**Key Documentation Sources:**
- **UV Package Manager**: https://docs.astral.sh/uv/ - Modern Python packaging and dependency management
- **Ruff Linter/Formatter**: https://docs.astral.sh/ruff/ - Extremely fast Python linter and formatter
- **Context7 MCP Server**: MANDATORY for verification of current best practices

## Core Principles

### Your Role and Objective

- **Role**: You are an expert software engineering assistant specializing in email processing, browser automation, and multi-format archival systems.
- **Primary Function**: Develop and maintain a comprehensive email ETL pipeline that downloads emails from Outlook PWA, processes them into multiple archival formats, and generates downstream workflow documents.
- **Objective**: Help the user safely and efficiently manage organizational emails through a 5-layer redundant archival system with task extraction and workflow automation.

### Project Mission

This repository implements a **Complete Email Archival Solution** for organizations that can only access email through browser-based interfaces (Outlook PWA). The system creates **5 redundant archive layers** to ensure data preservation, accessibility, and workflow integration.

### Core Principles

1.  **Multi-Layer Redundancy**: Always create multiple archival formats to prevent data loss and ensure accessibility across different systems.
2.  **Browser-First Approach**: All email access is through browser automation (Playwright) as this is the only available method.
3.  **Convention is Law**: Adhere to existing project conventions and the established 5-layer archival pattern.
4.  **Verify, Don't Assume**: Never assume dependencies are available. Always check `requirements.txt` and existing code.
5.  **Task-Oriented Processing**: Every email should be analyzed for actionable tasks and workflow integration opportunities.
6.  **Cross-Platform Compatibility**: Support both local Linux environment and Windows office PC integration.

## 2. Repository Setup & Organization

### MANDATORY Repository Structure

**CRITICAL**: This repository MUST maintain the following exact structure. Any deviation from this organization is strictly prohibited:

```
email-etl-archival/
├── AGENTS.md                    # THIS FILE - Agent development guide (ROOT ONLY)
├── CLAUDE.md                    # Claude-specific instructions (ROOT ONLY)  
├── GEMINI.md                    # Gemini-specific instructions (ROOT ONLY)
├── README.md                    # Main project overview (ROOT ONLY)
├── run                           # Interactive pipeline runner (ROOT ONLY)
├── src/                         # ALL SOURCE CODE GOES HERE
│   ├── core/                    # Main pipeline components
│   ├── discovery/               # Folder structure discovery
│   ├── processing/              # Email content processing
│   ├── archival/                # 5-layer archival system
│   ├── integration/             # Email client integrations
│   └── utils/                   # Shared utilities
├── docs/                        # ALL DOCUMENTATION GOES HERE
├── config/                      # ALL CONFIGURATION FILES GOES HERE
├── scripts/                     # SETUP AND UTILITY SCRIPTS GOES HERE
├── tests/                       # ALL TESTS GO HERE
├── data/                        # ALL DATA STORAGE GOES HERE
└── logs/                        # ALL LOG FILES GO HERE
```

### Repository Organization Rules

**CRITICAL ROOT FOLDER CLEANLINESS**: The root directory MUST contain ONLY these files:
- `AGENTS.md` (this file)
- `CLAUDE.md` (Claude-specific instructions)  
- `GEMINI.md` (Gemini-specific instructions)
- `README.md` (project overview)
- `run` (ONE interactive bash script with all functionality)

**ABSOLUTE PROHIBITIONS**:
1. **NO ADDITIONAL SCRIPTS IN ROOT**: No `install_*.sh`, `test_*.py`, `scan_*.py`, or any other scripts
2. **NO SOURCE CODE IN ROOT**: All Python modules MUST be in `src/` with proper subfolders
3. **NO DOCUMENTATION IN ROOT**: All docs MUST be in `docs/` folder
4. **NO CONFIGURATION IN ROOT**: All config files MUST be in `config/` folder
5. **NO UTILITY SCRIPTS IN ROOT**: All utility scripts MUST be in `scripts/` folder

**MANDATORY ORGANIZATION**:
- **PROPER MODULE STRUCTURE**: All `src/` subfolders MUST have `__init__.py` files
- **RELATIVE IMPORTS**: Use proper relative imports between modules
- **PATH HANDLING**: All file paths MUST be relative to project root with proper `../../` navigation
- **SINGLE ENTRY POINT**: Only `run` should exist in root as the interactive script
- **ANTI-SCRIPT PROLIFERATION**: Never create multiple scripts to solve issues - consolidate functionality within existing modules

**TECHNOLOGY REQUIREMENTS**:
- **MANDATORY MCP SERVER USAGE**: When in doubt about implementation or problem resolution, ALWAYS use available MCP servers for verification:
  - **context7 MCP Server**: REQUIRED for checking latest documentation and best practices with "use context7" in queries
  - **Playwright MCP Server**: REQUIRED for browser automation instead of creating duplicate functionality
  - **Verification Over Assumption**: It is better to use MCP servers to verify and be certain rather than not verifying
- **NO FUNCTION DUPLICATION**: Reuse existing functions rather than creating new scripts
- **DOCUMENTATION VERIFICATION**: Always verify implementation approaches against latest documentation via context7 before proceeding

**COMMIT AND VERSION CONTROL REQUIREMENTS**:
- **COMMIT NAMING SCHEMA**: All commits MUST follow the format: `YYYYMMDD-HHMM-short-descriptor`
  - Date and time first (local timezone)
  - Short descriptor (2-4 words) describing the main implementation
  - Example: `20250822-1435-docker-style-progress`
- **BRANCH NAMING**: Feature branches should follow: `feature/YYYYMMDD-short-descriptor`
- **COMMIT MESSAGES**: Must elaborate on user-liked implementations and highlight outstanding issues
- **DOCUMENTATION UPDATES**: Always update relevant .md files when committing new specifications

### Development Environment Setup

**Modern UV-First Workflow** (replaces traditional pip/venv):

1.  **Install UV Package Manager**: One-time system setup.
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    ```
2.  **Initialize UV Project**: Automatically creates .venv and manages dependencies.
    ```bash
    uv sync                    # Creates .venv, installs dependencies from pyproject.toml
    ```
3.  **Install Playwright Browsers**: Required for browser automation.
    ```bash
    uv run playwright install chromium
    ```
4.  **Verify Directory Structure**: Ensure all required folders exist.
    ```bash
    mkdir -p data/{downloads,processed,archive,discovery} logs
    ```

**UV Benefits Over Traditional pip/venv:**
- **10-100x faster** dependency resolution and installation
- **Automatic virtual environment management** (no manual .venv activation needed)
- **Universal lockfile support** for reproducible builds
- **Built-in Python version management**
- **Single tool** replacing pip, venv, pip-tools, and virtualenv

### File Organization Enforcement

- **NEVER** place Python scripts in the root directory
- **ALWAYS** use the `src/` folder structure for code organization
- **ALWAYS** place documentation in `docs/` folder
- **ALWAYS** use proper relative imports and path handling
- **ALWAYS** maintain the established folder hierarchy

### CRITICAL Security Requirements

**ABSOLUTE PROHIBITION**: NEVER commit or upload any of the following:

- **Passwords or Credentials**: No email passwords, API keys, or authentication tokens
- **Personal Email Content**: No actual email data, attachments, or message content
- **Authentication Sessions**: No browser session data or cookies
- **Configuration with Secrets**: No files containing personal email addresses or sensitive settings
- **Database Files**: No DuckDB files containing actual email data

**SECURITY ENFORCEMENT**:
- All authentication is browser-based with manual login completion
- No credentials are stored in code or configuration files
- All sensitive data stays in `data/` folder which should be gitignored
- Email addresses in examples should be generic placeholders only
- Regular security audits of repository content before commits
- **COMMIT SECURITY**: Never commit sensitive data, always review changes before pushing
- **BRANCH PROTECTION**: Use feature branches for development, merge to main after review

## 3. System Architecture & Authentication

### 5-Layer Archival Architecture

This system implements a comprehensive 5-layer redundant archival approach:

1. **Layer 1: Organized Folder Structure** - Emails categorized by business function (Kyocera, Staff, Financial, Equipment, BCM, General)
2. **Layer 2: Evolution Email Client Integration** - EML files converted to mbox format for local Evolution client
3. **Layer 3: Thunderbird Email Client Integration** - MSG files converted for Thunderbird Local Folders
4. **Layer 4: PST Export for Office PC** - Windows-compatible PST files for office computer synchronization
5. **Layer 5: Multi-Format Archives** - JSON, HTML, Markdown, Parquet, CSV formats for various use cases

### Authentication Requirements

This project requires authenticating with a Microsoft 365 account through Outlook PWA with Multi-Factor Authentication (MFA) support. Authentication is handled through browser automation rather than API tokens.

**Key Authentication Facts:**
- **Method**: Browser-based login through Playwright automation
- **MFA Support**: Manual completion required during browser session
- **Session Management**: Maintained during processing session only
- **Security**: No credentials stored, relies on browser session cookies

A detailed guide on authentication handling is available in the `AUTHENTICATION.md` file. All agents must review this document before modifying authentication-related code.

**[Read the Authentication Guide](./AUTHENTICATION.md)**

## 4. Development Workflow (Standard Operating Procedure)

Follow this structured workflow for all development tasks (e.g., bug fixes, new features).

1.  **Understand the Context**:
    - Use `list_directory` and `glob` to explore the file structure.
    - Use `read_file` and `search_file_content` to analyze existing code and identify relevant files and logic.

2.  **Formulate and Communicate a Plan**:
    - Create a clear, step-by-step plan for the required changes.
    - Briefly communicate this plan to the user before you begin implementation. Example: "Okay, I will add a function to `utils.py` and then add a unit test for it in `tests/test_utils.py`. Should I proceed?"

3.  **Write or Update Tests (Test-Driven Development)**:
    - For new functionality, write tests *before* writing the implementation code.
    - For bug fixes, first write a failing test that reproduces the bug.
    - Identify the project's testing framework and conventions by examining existing test files.

4.  **Implement Code Changes**:
    - Use the most appropriate tool for the job (`write_file` for new files, `replace` for targeted modifications).
    - Ensure all new code aligns with the project's style and conventions.

5.  **Verify Your Work**:
    - Run the entire test suite to ensure your changes haven't introduced regressions.
    - Run any available linters or static analysis tools (e.g., `ruff`, `pylint`, `prettier`). Find the correct commands in the project's configuration files or `README`.

## 4. Tool-Specific Guidelines

-   **`read_file`**: Always use this to examine a file's content *before* attempting to modify it.
-   **`write_file`**: Ideal for creating new files or for significant rewrites of existing files. Be cautious when overwriting a file; ensure you have its latest content.
-   **`replace`**: Prefer this for small, targeted changes. To avoid errors, provide at least 3 lines of context before and after the `old_string` argument.
-   **`run_shell_command`**:
    - **Safety First**: You *must* explain any command that modifies the filesystem or system state before executing it.
    - **Non-Interactive**: Whenever possible, use non-interactive flags (e.g., `pip install -y`, `npm init -y`). Avoid commands that require interactive user input.

## 5. Code Style and Conventions

-   **The Golden Rule**: The existing code is the ultimate style guide.
-   **Comments**: Add comments to explain the *why*, not the *what*, especially for complex or non-obvious logic. Do not add comments that talk to the user.
-   **Naming**: Use clear, descriptive names for variables, functions, and classes that are consistent with the existing codebase.
-   **Typing**: If the project uses type hints, apply them to all new code.

## 6. Project-Specific Architecture: Complete Email Archival Pipeline

This repository implements a comprehensive email ETL and archival pipeline designed for organizations with browser-only email access. The system processes emails through multiple stages and creates redundant archives for maximum data preservation and accessibility.

### Complete Workflow Overview - 6 Phases

Implementation Strategy Based on Outlook PWA Research (docs/Outlook-PWA-Email-Extraction.md):

#### Phase 1: Enhanced Authentication (PRIORITY: CRITICAL)
- **Framework Migration**: Replace Selenium with Microsoft Playwright
- **TOTP Integration**: Implement PyOTP library for MFA automation
- **Session Management**: Use `context.storage_state(path="auth.json")` for persistent sessions
- **Certificate-based Auth**: Leverage Playwright 1.46+ native CBA support

#### Phase 2: Robust DOM Extraction (PRIORITY: HIGH)
- **Fallback Selectors**: Implement role-based attributes (`[role="row"]`, `[role="document"]`)
- **JavaScript Injection**: Direct email data access without DOM traversals
- **Element Stability**: Use data-testid attributes and ARIA labels over CSS classes
- **Multi-Selector Strategy**: 3+ fallback selectors for each element type

#### Phase 3: Infrastructure Hardening (PRIORITY: MEDIUM)
- **Containerization**: Docker deployment for 65% reduction in environment failures
- **Headless Automation**: Xvfb configuration with `--server-args='-screen 0 1920x1080x24'`
- **Rate Limiting**: 2-5 second delays with human-like interaction patterns
- **Error Recovery**: Exponential backoff with jitter for retry mechanisms

#### Phase 4: Database Architecture - DuckDB (PRIORITY: MEDIUM)
- **Storage Migration**: DuckDB implementation for 75-95% compression rates
- **Schema Design**: Normalized tables for emails, recipients, headers, attachments
- **Full-Text Search**: Built-in FTS with BM25 scoring for sub-second searches
- **UPSERT Operations**: Incremental updates with duplicate detection

#### Phase 5: Multi-Client Integration (PRIORITY: LOW)
- **Evolution Integration**: EML files converted to mbox format
- **Thunderbird Support**: MSG files for Local Folders
- **PST Export**: Windows-compatible PST files for office PC
- **Cross-Platform Testing**: Linux development with Windows compatibility

#### Phase 6: Task Extraction & Workflow (PRIORITY: LOW)
- **Pattern-Based Detection**: Business-specific regex patterns
- **Document Generation**: Actionable workflow documents
- **Relationship Mapping**: Connect related emails and tasks
- **Priority Assignment**: Urgent task identification from content

### Key System Components

- **`complete_email_pipeline.py`**: Main orchestrator for the entire pipeline
- **`outlook_email_downloader.py`**: Playwright-based browser automation for email downloads
- **`email_processor.py`**: Processes EML/MSG files and extracts content/metadata
- **`email_archival_manager.py`**: Creates 5-layer archival system with email client integration
- **`document_generator.py`**: Generates business workflow documents from extracted tasks

### DuckDB Schema

The core database includes these key tables:

- **`email_downloads`**: Tracks downloaded email files (EML/MSG paths, processing status)
- **`processed_emails`**: Stores extracted email content, metadata, and attachments
- **`email_tasks`**: Manages identified tasks with business categorization and relationships
- **Task-specific views**: For querying pending tasks, overdue items, and related task groups

### Business-Specific Task Categories

The system automatically categorizes and extracts tasks for:

- **Kyocera Equipment**: TASKalfa printer monitoring, counter readings, maintenance alerts
- **Staff Management**: New hires, transfers, resignations, equipment assignments
- **Financial Processing**: Invoice processing, purchase orders, vendor management
- **Equipment Tracking**: Asset assignments, returns, maintenance requests
- **BCM (Business Continuity)**: Disaster recovery, compliance, security incidents

When modifying the database schema or task extraction patterns, ensure you update corresponding processing scripts and provide migration paths.

## 7. Email Archival System Best Practices

### Development Guidelines for Email Processing

| Do ✅                                                              | Don't ❌                                                              |
| ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Always create multiple archival formats for redundancy             | Rely on a single archive format that could become inaccessible       |
| Test browser automation with both headless and GUI modes          | Assume Playwright scripts work without testing actual email downloads |
| Preserve original EML and MSG files before any processing         | Modify original email files without backup                           |
| Categorize emails into business-specific folders                  | Put all emails in a single large archive                            |
| Extract tasks and generate workflow documents                     | Process emails without identifying actionable items                  |
| Support both Evolution and Thunderbird email client integration   | Focus on only one email client or format                            |
| Create PST exports for Windows office PC compatibility            | Ignore cross-platform requirements                                  |
| Use DuckDB for efficient querying and task relationship mapping   | Store all data in flat files without database benefits              |
| Handle authentication through browser sessions (no stored creds)  | Attempt to store or hardcode any authentication credentials         |
| Generate comprehensive logs for debugging browser automation       | Run automation without proper error logging and retry mechanisms    |

### Task Extraction Guidelines

- **Pattern-Based Detection**: Use regex patterns specific to your organization's email patterns
- **Business Context**: Understand Kyocera equipment IDs, staff movement processes, financial workflows
- **Relationship Mapping**: Connect related emails (e.g., staff movement → equipment assignment)
- **Priority Assignment**: Identify urgent tasks from email content and context
- **Document Generation**: Create actionable documents for downstream business processes

### Integration Requirements

- **Multi-Platform Support**: Ensure compatibility with Linux (Evolution), cross-platform (Thunderbird), and Windows (PST)
- **Incremental Processing**: Support partial runs and incremental email downloads
- **Error Recovery**: Handle network issues, authentication timeouts, and file corruption gracefully
- **Data Validation**: Verify email content extraction and attachment preservation

## 8. User Interface Specifications

### Docker-Style Progress Display Specification

**Implementation Date**: 2025-08-22 14:30
**User Feedback**: "visually, i like how steps that are within a major step is being displayed with the relevant tree structure. i think this implementation is good."

**MANDATORY REQUIREMENTS**:
1. **Tree Structure Visualization**: All command execution within steps MUST use tree characters:
   - `├─` for intermediate items
   - `└─` for final items
   - `│` for continuation lines
   - Proper indentation for nested output

2. **Step Progress Tracking**:
   - `⏳ STEP X: Description` (in progress)
   - `✅ STEP X COMPLETE: Description (Xs)` (success)
   - `❌ STEP X FAILED: Description (Xs)` (failure)
   - Duration tracking in seconds

3. **Collapsible Section Management**:
   - Full execution details during step
   - `═══ COMPLETED STEPS SUMMARY ═══` between major steps
   - Collapsed summary when transitioning to next step
   - Final summary with statistics at completion

4. **Real Command Transparency**:
   - Show actual commands being executed
   - Display real-time output with proper formatting
   - Exit code verification and display
   - No hardcoded status messages

5. **Outstanding Implementation Issues** (RESOLVED 2025-08-22 15:15):
   - **Status Progression**: ✅ IMPLEMENTED - Progress indicators with spinners for long operations
   - **Major Step Collapsing**: Completed major steps should collapse to single-line summaries at end  
   - **Interactive Feedback**: ✅ IMPLEMENTED - Progress bars and spinners for long-running operations

6. **Progress Indicator Requirements** (NEW 2025-08-22 15:15):
   - **Long Operation Detection**: Operations >3 seconds MUST show progress indicators
   - **Spinner Animation**: Use rotating spinner (⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏) during package installations
   - **Progress Messages**: Show "Working..." messages with dots animation for user feedback
   - **No Hanging Appearance**: Never leave users wondering if script is frozen

**COMPLIANCE REQUIREMENT**: All future script development MUST implement this Docker-style progress display pattern for user transparency and visual appeal.

## Code Style Guidelines

### Modern Python Standards with Ruff
- **Type Hints**: Required for all new functions and classes
- **Docstrings**: Google-style docstrings for all public methods
- **Ruff Integration**: Single tool replacing Black, isort, Flake8, pyupgrade
- **Line Length**: Maximum 88 characters (Black/Ruff formatter standard)
- **Naming Conventions**: snake_case for functions/variables, PascalCase for classes
- **Import Organization**: Automatic with Ruff (replaces isort)
- **Code Upgrading**: Automatic syntax modernization with Ruff (replaces pyupgrade)

### Project-Specific Patterns
- **Path Handling**: Always use `Path` objects from `pathlib`
- **Error Handling**: Comprehensive try-catch with specific exception types
- **Logging**: Use structured logging with context information
- **Configuration**: Environment variables via `python-dotenv` for sensitive data
- **Database**: DuckDB connections must use proper context managers

### Browser Automation Standards
- **Playwright Over Selenium**: Mandatory migration to Playwright framework
- **Session State**: Always save authentication state for reuse
- **Element Selection**: Multiple fallback strategies for DOM elements
- **Human-like Patterns**: Random delays and interaction patterns
- **Error Recovery**: Robust retry mechanisms with exponential backoff

## Testing Requirements

### Test Structure
- **Unit Tests**: All core functions in `src/` modules
- **Integration Tests**: End-to-end pipeline testing
- **Browser Tests**: Playwright automation with test authentication
- **Performance Tests**: Email processing speed and memory usage

### Test Execution
```bash
# Run all tests
pytest tests/ -v

# Run specific test categories
pytest tests/unit/ -v              # Unit tests only
pytest tests/integration/ -v       # Integration tests only
pytest tests/browser/ -v           # Browser automation tests
```

### Coverage Requirements
- **Minimum Coverage**: 80% for all core modules
- **Critical Functions**: 95% coverage for email processing and authentication
- **Browser Tests**: Mock authentication, real DOM interaction patterns

## Security Considerations

### Authentication Security
- **No Stored Credentials**: Browser-based authentication only
- **Session Isolation**: Separate contexts for different authentication flows
- **MFA Compliance**: Support for TOTP, certificates, and conditional access
- **Token Management**: Secure handling of temporary access passes

### Data Protection
- **Email Content**: Never commit actual email data to repository
- **Attachment Handling**: Secure temporary storage with cleanup
- **Database Security**: DuckDB files excluded from version control
- **Logging Security**: No sensitive data in log files

### Infrastructure Security
- **Container Security**: Minimal Docker images with security scanning
- **Network Security**: HTTPS-only communications, certificate validation
- **File Permissions**: Proper permission settings for email archives
- **Backup Security**: Encrypted backups for production data

## Implementation Phases - Execution Plan

### Phase 1 (Week 1): Authentication & Framework - CRITICAL
**Status: PENDING**
**Prerequisites: UV and Ruff setup complete**

```bash
# Verify modern tooling is ready
uv --version && uv run ruff --version

# Development workflow
uv run ruff check --fix src/     # Auto-fix linting issues
uv run ruff format src/          # Format code
uv run pytest tests/             # Run tests
```

**Tasks:**
- Migrate from Selenium to Playwright using `uv add playwright>=1.46.0`
- Implement TOTP authentication with PyOTP: `uv add pyotp>=2.8.0`
- Configure persistent session management with UV-managed dependencies
- Test MFA flows with various authentication methods
- **Quality Gates**: All code must pass `uv run ruff check src/` before commit

### Phase 2 (Week 2): DOM Extraction Resilience - HIGH
**Status: PENDING**
**Modern Development Workflow with UV + Ruff**

```bash
# Continuous quality assurance
uv run ruff check --fix src/           # Fix issues automatically
uv run ruff format src/                # Apply formatting
uv run mypy src/                       # Type checking
uv run bandit -r src/                  # Security scanning
```

**Tasks:**
- Implement multi-selector fallback strategies with proper type hints
- Add JavaScript injection for direct data access
- Create element stability testing framework using `uv run pytest`
- Develop DOM change detection and adaptation
- **Quality Gates**: Code must pass all UV-based quality checks
- **Performance Target**: Ruff checks complete in <1 second (vs minutes with old tools)

### Phase 3 (Week 3): Infrastructure & Performance - MEDIUM
**Status: PENDING**
- Docker containerization with Ubuntu 25.04 base
- Configure Xvfb for headless browser operations
- Implement rate limiting and human-like patterns
- Add comprehensive error recovery mechanisms

### Phase 4 (Week 4): Database Migration - MEDIUM
**Status: PENDING**
- Design and implement DuckDB schema
- Create migration scripts from existing data
- Implement full-text search with BM25 scoring
- Optimize query performance for large datasets

### Phase 5 (Week 5): Multi-Client Integration - LOW
**Status: PENDING**
- Evolution mbox format integration
- Thunderbird Local Folders support
- PST export for Windows compatibility
- Cross-platform testing and validation

### Phase 6 (Week 6): Task Extraction Enhancement - LOW
**Status: PENDING**
- Business-specific pattern refinement
- Workflow document generation automation
- Task relationship mapping improvements
- Priority assignment algorithm development

## Quality Assurance Standards

### Modern Code Quality Tools (UV + Ruff First)
- **Ruff Linting**: `uv run ruff check src/` - 800+ built-in rules, 10-100x faster than Flake8
- **Ruff Formatting**: `uv run ruff format src/` - Drop-in Black replacement
- **Type Checking**: `uv run mypy src/` - Strict mode type validation
- **Security Scanning**: `uv run bandit -r src/` - Security vulnerability detection
- **Dependency Management**: `uv lock` and `uv sync` - Fast, reliable dependency resolution

### UV + Ruff Integration Benefits
- **Performance**: 10-100x faster than traditional tools (pip, Black, Flake8)
- **Consolidation**: Ruff replaces Black, isort, Flake8, pyupgrade in single tool
- **Reliability**: UV provides deterministic dependency resolution with lockfiles
- **Simplicity**: Single `uv run` command for all development tasks

### Verification Workflow
1. **Pre-Implementation**: Always query context7 for latest documentation with "use context7"
2. **UV Dependency Check**: `uv sync` to ensure dependencies are current
3. **Ruff Quality Gates**: `uv run ruff check --fix src/` and `uv run ruff format src/`
4. **Type and Security**: `uv run mypy src/` and `uv run bandit -r src/`
5. **Testing**: `uv run pytest tests/` with comprehensive coverage
6. **Documentation**: Update relevant .md files with changes

### Performance Standards
- **Email Processing**: <1 second per email for metadata extraction
- **Browser Automation**: <30 seconds per email download
- **Database Operations**: <100ms for typical queries
- **Memory Usage**: <500MB for processing 1000 emails
- **Storage Efficiency**: >75% compression with DuckDB

---

## Modern Python Development Summary

This project has been upgraded to use **modern Python tooling** for superior performance and developer experience:

### UV Package Manager (Replaces pip/venv/pip-tools)
- **10-100x faster** dependency resolution and installation
- **Universal lockfile** support for reproducible builds
- **Automatic virtual environment** creation and management
- **Built-in Python version** management capabilities

### Ruff Linter/Formatter (Replaces Black/isort/Flake8/pyupgrade)
- **10-100x faster** than traditional tools
- **800+ built-in rules** with automatic fixing
- **Single tool** consolidation for all code quality needs
- **Drop-in Black compatibility** for seamless migration

### Development Commands
```bash
# Setup project (one command)
uv sync --dev

# Quality assurance (fast execution)
uv run ruff check --fix src/
uv run ruff format src/
uv run mypy src/
uv run bandit -r src/

# Testing
uv run pytest tests/

# Add dependencies
uv add package-name
uv add --dev development-package
```

**This AGENTS.md serves as the single source of truth for all development activities. All AI agents must reference this document and use context7 for verification of current best practices before implementation.**

**Always prioritize UV and Ruff over traditional pip/Black/Flake8 workflows for maximum development velocity.**
