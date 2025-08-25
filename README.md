# Email ETL and 5-Layer Archival System

A comprehensive email extraction, transformation, and archival pipeline designed for organizations with browser-only email access.

## 🚀 Quick Start

### Production Usage (Email Processing)
```bash
# One-command setup and execution
./run

# System automatically:
# - Installs UV package manager if needed
# - Sets up virtual environment with all dependencies
# - Detects Chrome browser and connects to Outlook PWA
# - Presents email conversion menu for immediate use
```

### Development Setup (Code Development)
```bash
# Install modern Python tooling (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup development environment
uv sync --dev                      # Install dev dependencies (ruff, mypy, pytest)
uv run playwright install chromium # Install browser for automation

### Keyword analysis (uv)

If you want to run the included keyword frequency utility (`run.py`) using the project's UV-managed environment:

```bash
# Ensure uv is installed (one time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies into the UV-managed environment
uv sync --dev

# Run the keyword analysis (from repository root)
uv run python run.py --input-dir ./data --output-csv keyword_frequency.csv --top 20
```
# Development workflow
uv run pytest tests/              # Run test suite
uv run ruff check --fix src/      # Auto-fix linting issues
uv run ruff format src/           # Format code
uv run mypy src/                  # Type checking
```

## 🎯 System Overview

The **Email ETL and 5-Layer Archival System** provides zero-configuration email processing:

1. **🚀 Run `./run`** - Automated environment setup
2. **🔍 Chrome Detection** - Connects to existing Outlook PWA or launches Chrome
3. **📧 Email Conversion** - Download and process emails in multiple formats
4. **🗂️ 5-Layer Archive** - Creates redundant archives for data preservation

## 📁 Repository Structure

```
email-etl-archival/
├── AGENTS.md              # Agent development guide
├── CLAUDE.md              # Claude-specific instructions
├── GEMINI.md              # Gemini-specific instructions
├── src/                   # Source code
│   ├── core/              # Main pipeline components
│   ├── discovery/         # Folder structure discovery
│   ├── processing/        # Email content processing
│   ├── archival/          # 5-layer archival system
│   ├── integration/       # Email client integrations
│   └── utils/             # Shared utilities
├── docs/                  # Documentation
├── config/                # Configuration files
├── scripts/               # Setup and utility scripts
├── tests/                 # Test suites
├── data/                  # Data storage
│   ├── downloads/         # Downloaded emails
│   ├── processed/         # Processed outputs
│   └── archive/           # Final archives
└── logs/                  # Application logs
```

## 🎯 Current Objectives

See [docs/FOLDER_DISCOVERY_OBJECTIVES.md](docs/FOLDER_DISCOVERY_OBJECTIVES.md) for today's priority tasks.

## 📖 Documentation

**PRIMARY SOURCE**: **[AGENTS.md](AGENTS.md)** - The definitive specification source for all development activities

Additional Documentation:
- **[Complete Documentation](docs/README.md)** - Comprehensive system guide
- **[Authentication Setup](docs/AUTHENTICATION.md)** - MFA and login configuration
- **[Outlook PWA Research](docs/Outlook-PWA-Email-Extraction.md)** - Implementation improvements based on research

## 🔄 5-Layer Archival System

1. **Organized Folders** - Business-categorized structure
2. **Evolution Integration** - Linux email client
3. **Thunderbird Integration** - Cross-platform client  
4. **PST Export** - Windows office PC compatibility
5. **Multi-Format Archives** - JSON, HTML, MD, Parquet, CSV

## ⚡ Key Features

- Browser automation for Outlook PWA
- Intelligent folder structure discovery
- Business-specific task extraction
- Cross-platform email client integration
- Comprehensive workflow document generation

## Local CI (offline-first)

This repository includes a local CI runner (`scripts/local_ci.sh`) and a
git pre-push hook template (`scripts/git-hooks/pre-push`) that runs local CI
before pushing. These are intentionally local-only to avoid network usage
and external CI costs.

To install the hooks locally (one-time):

```bash
# Ensure you have a .venv (run `uv sync --dev` once if you need to install deps)
./scripts/install-hooks.sh
```

The hooks will run `scripts/local_ci.sh` before each push. If you prefer not
to run hooks automatically, don't install them; you can run the local CI manually:

```bash
./scripts/local_ci.sh
```