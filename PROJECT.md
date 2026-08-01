# 🚀 Project Atlas

## Vision

Project Atlas is an AI-powered media company designed to research, write, review, improve, export, and eventually publish high-quality YouTube content with minimal human intervention.

Rather than acting as a single chatbot, Atlas operates as a team of specialised AI agents coordinated by a CEO Agent.

---

# Current Version

**Version:** v0.4

Status:

✅ Functional AI content pipeline

---

# Current Sprint

## Sprint 1 – Quality Control (v0.5)

Goal:

Teach Atlas to evaluate and improve its own work before publishing.

Current Tasks:

- [ ] Quality Agent
- [ ] ReviewResult model
- [ ] CEO decision engine
- [ ] Retry system
- [ ] JSON quality reports

---

# Tech Stack

- Python 3.9+
- Claude (Anthropic API)
- Git
- Cursor
- Virtual Environment (.venv)

Future:

- FFmpeg
- OpenAI Whisper
- ElevenLabs
- YouTube API

---

# Architecture

See:

docs/architecture.md

---

# Current Agent Team

CEO Agent

Research Agent

Title Agent

Script Agent

Description Agent

Tags Agent

---

# Future Agent Team

Quality Agent

Thumbnail Agent

Memory Agent

Analytics Agent

Publishing Agent

Voiceover Agent

Video Assembly Agent

---

# Development Rules

Every feature follows this process:

1. Plan
2. Design
3. Build
4. Test
5. Commit
6. Document

Never skip architecture.

Never hardcode secrets.

Keep prompts separate from Python code.

Each agent has one responsibility.

---

# Current Milestone

Build Atlas v0.5

Focus:

Teach Atlas to think before it publishes.

---

# Long-Term Goal

Atlas v1.0

An autonomous AI media company capable of:

- Researching topics
- Creating content
- Reviewing quality
- Improving weak outputs
- Producing media assets
- Publishing videos
- Learning from analytics