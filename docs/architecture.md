# Project Atlas Architecture

## Purpose

Project Atlas is an AI-powered media production system designed to research, create, review, improve, export, and eventually publish YouTube content.

The system is built around specialised agents. Each agent has one clear responsibility and works on the shared `MasterContent` object.

---

## Core Principles

1. Each agent performs one job.
2. Agents receive only the information they need.
3. Outputs should be structured and predictable.
4. The CEO Agent coordinates work but does not create content.
5. The Editor Agent evaluates quality but does not rewrite content directly.
6. Every automated retry must have a limit.
7. Human approval remains available when Atlas cannot resolve an issue safely.
8. Prompts remain separate from Python code.
9. API providers remain replaceable.
10. Secrets must stay inside `.env`.

---

## Shared Content Model

The `MasterContent` object flows through the entire pipeline.

Current fields:

```python
topic
audience
objective
key_points
call_to_action
keywords
title
script
description
tags
thumbnail_prompt
voiceover_prompt