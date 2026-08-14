# Project Atlas

Project Atlas is an AI-powered content production system designed to research, create, review, and prepare high-quality educational YouTube content.

Atlas uses a modular multi-agent architecture where specialised AI agents handle different stages of the content production process.

## Vision

Build an AI-powered media company that can research, create, review, optimise, and eventually publish world-class educational content at scale.

## Mission

Build assets, not just income.

## Current Version

**Project Atlas v0.8.0**

Atlas currently supports an end-to-end AI content production workflow with automated editorial review, targeted retries, and publishing decisions.

## Architecture

```text
CEO Agent
    |
    v
Research Agent
    |
    v
Title Agent
    |
    v
Script Agent
    |
    v
Description Agent
    |
    v
Tags Agent
    |
    v
Editorial Board
    |
    +-- SEO Review
    +-- Script Review
    +-- Audience Review
    +-- Brand Review
    +-- Copy Review
    |
    v
Editorial Review
    |
    v
Decision Engine
    |
    +-- PUBLISH
    +-- RETRY
    +-- HUMAN REVIEW
```

## Core Features

- AI-powered topic research
- YouTube title generation
- Long-form script generation
- Video description generation
- SEO tag generation
- Multi-perspective Editorial Board review
- Structured editorial scoring
- Automated publishing decisions
- Targeted content retries
- Configurable retry limits
- Content export
- Development and production modes
- Graceful API error handling
- Automated test suite

## Editorial Board

Every completed content package is evaluated from five perspectives:

- SEO
- Script
- Audience
- Brand
- Copy

The Editorial Board returns structured scores, feedback, an overall score, and a recommended next action.

If the content fails review, Atlas can selectively rerun the relevant production agent instead of regenerating the entire content package.

## Installation

Clone the repository:

```bash
git clone https://github.com/EricKevin-bot/Project-Atlas.git
cd Project-Atlas
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```text
ANTHROPIC_API_KEY=your_api_key_here
```

Never commit your `.env` file or API key to Git.

## Running Atlas

Start Atlas with:

```bash
python main.py
```

Atlas will:

1. Research a potential video topic.
2. Ask for topic approval.
3. Generate the content package.
4. Run the Editorial Board.
5. Retry a targeted component when required.
6. Make a final publishing decision.
7. Export approved content.

Approved content is saved in the `output/` directory.

## Testing

Run the complete automated test suite:

```bash
pytest -q
```

Current automated coverage includes:

- Decision Engine
- Retry Manager
- File Manager

## Project Structure

```text
Project-Atlas/
├── agents/
├── automation/
├── content/
├── data/
├── docs/
├── models/
├── output/
├── prompts/
├── scripts/
├── services/
├── tests/
├── utils/
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

## Development Roadmap

### v0.8
Editorial intelligence and decision architecture.

### v0.9
Application reliability, testing, documentation, and release preparation.

### v1.0
First production-ready release.

Future development may include:

- YouTube publishing integration
- Thumbnail generation
- Content analytics
- Performance feedback loops
- Content memory
- Multi-channel support
- Automated scheduling

## Founder

Eric Kevin