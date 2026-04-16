# Assignment 13_07 — Input Guardrails

## Task
Create one workflow that checks the input before calling the model.

---

## Enterprise Use Case
**Gaming Abuse Report Intake Assistant**
Validates all required report fields before passing the abuse report to the model for moderation summary generation.

---

## Prompt Used

You are a gaming abuse report intake assistant.
Your task is to convert the abuse report details below into a short internal moderation summary.

### Input Guardrails:
1. `reporter_username` must not be empty.
2. `reported_username` must not be empty.
3. `game_title` must not be empty.
4. `incident_description` must not be empty.
5. `abuse_type` must be one of: harassment, cheating, hate speech, spam, or threats.
6. If any field fails validation, print a blocked message and do not call the model.
7. Only call the model when all fields pass validation.

### Rules:
1. Use only the details provided.
2. Keep the summary short and professional.
3. Do not make assumptions about intent beyond what is described.
4. Recommend the moderation action based on the abuse type.

### Input Provided:
- Reporter Username: PlayerOne_99
- Reported Username: ToxicGamer_007
- Game Title: Battle Arena Pro
- Abuse Type: harassment
- Incident Description: The reported player sent repeated offensive messages and racial slurs in the team chat during a ranked match.

---

## Model Output

Reporter: PlayerOne_99

Reported Player: ToxicGamer_007

Game: Battle Arena Pro

Abuse Type: Harassment

Incident Summary: The reported player sent repeated offensive messages and racial slurs in the team chat during a ranked match.

Recommended Action: Temporary Ban (e.g., 3-7 days) with Chat Restriction.

---

## Explanation

### Why this is Input Guardrails
- All 5 required fields were validated before the model was called
- The model was only invoked after the input fully passed all guardrail checks
- An invalid or empty field prints a blocked message and stops execution
- The allowed value check on `abuse_type` prevents unsupported categories from reaching the model

---

## Key Learning
- Input guardrails validate data before it reaches the model
- They are different from other guardrails — input guardrails protect the pipeline at the entry point
- Prevents garbage-in garbage-out situations in enterprise AI workflows

---

## Summary
- Input guardrails = pre-model validation layer
- Useful in abuse reporting tools, HR intake systems, support portals, and form-based AI workflows
- Ensures the model only processes clean, complete, and valid input