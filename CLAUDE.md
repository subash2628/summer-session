# CLAUDE.md
Behavioral guidelines to reduce common LLM coding mistakes, merged with project-specific instructions for this module's teaching materials.
**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## Project Context
This repo contains teaching/workshop materials for the module **"From Data to Deployment: Python, APIs & ML"** (BSc Computing with AI, Year 2, Islington College). It covers one end-to-end pipeline:

```
Titanic dataset → Pandas preprocessing → Decision Tree model → model.pkl
→ FastAPI (/predict) → HTML frontend (form + Predict button) → Docker
→ Docker Compose → Nginx → AWS EC2
```

Audience: **students**, delivered across 2×1hr Tutorials + 2×2hr Workshops in one week. Code produced here is meant to be:
- Read and understood by Year 2 students in a single workshop sitting.
- Easy to adapt, not a production ML system.
- A faithful, minimal reference implementation of each pipeline stage — not a showcase of advanced patterns.

When in doubt, prefer the version a student could explain back in one sentence over the version an engineer would ship.

---

## 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

Project-specific: if a request could be solved either "the simple way a student would do it" or "the robust way a production system would do it," default to the simple way and say so — don't silently pick the production version.

## 2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

Project-specific:
- No extra ML features beyond the 7 Titanic columns specified (Pclass, Sex, Age, SibSp, Parch, Fare, Embarked). No feature engineering, ensembling, or hyperparameter search frameworks unless explicitly asked.
- No auth, rate-limiting, logging frameworks, or config management in the FastAPI app unless asked — this is a single `/predict` endpoint for a workshop.
- No CSS frameworks or build tooling for the frontend — plain HTML/CSS/JS in one file is the target.
- No multi-stage Docker builds, health checks, or orchestration beyond what's needed to run API + Nginx via Compose, unless asked.

## 3. Surgical Changes
**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: every changed line should trace directly to the user's request.

Project-specific: when editing the session plan, notebook, or boilerplate files, preserve existing timings/structure unless the change explicitly calls for re-timing a session.

## 4. Goal-Driven Execution
**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

Project-specific verification, by pipeline stage:
- **Preprocessing:** no nulls remain in `Age`/`Embarked`; categorical columns are numeric; train/test split shapes printed.
- **Model:** accuracy/confusion matrix printed on the test set; `model.pkl` saved and reloads without error.
- **FastAPI:** `/docs` loads; a sample POST to `/predict` returns a valid prediction.
- **Frontend:** submitting the form with sample data displays a result without a page reload.
- **Docker/Compose:** `docker compose up` brings up API + Nginx; hitting the Nginx port returns the frontend and a working `/predict`.
- **EC2:** the public IP/port serves the frontend and returns a prediction.

---
**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
