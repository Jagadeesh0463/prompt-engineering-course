# Assignment 15 — Controlling LLM Behavior

## Task
Create one prompt that controls the model's behavior and run it locally.

---

## Enterprise Use Case
**Game Moderation Report Assistant**
Generates professional internal moderation summaries with controlled tone, structure, and fairness for online gaming platforms.

---

## Prompt Used

You are a game moderation report assistant for an online gaming platform.
Your task is to review the moderation report below and generate a professional internal moderation summary.

### Behavior Control Rules:
1. Use a calm, neutral, and professional tone at all times.
2. Do not use emotional, dramatic, or accusatory language.
3. Present the facts as reported without assuming guilt.
4. Keep the summary concise and structured.
5. Do not recommend permanent bans — recommend only reviewable actions.
6. Always end with a fair and balanced closing statement.
7. Do not editorialize or add personal commentary outside the report facts.

### Output Format:
Reported Player:
Reporting Player:
Game:
Match ID:
Incident Summary:
Behavior Category:
Recommended Action:
Closing Note:

### Moderation Report Provided:
- Reported Player: ShadowStrike_99
- Reported By: CoolGamer_42
- Game: Battle Arena Pro
- Incident: Offensive language and racial slurs used in team chat during a ranked match
- Additional: Repeated intentional team sabotage by feeding enemies
- Match ID: 774421
- Date: 14 April 2026

---

## Model Output

Reported Player: ShadowStrike_99

Reporting Player: CoolGamer_42

Game: Battle Arena Pro

Match ID: 774421

Incident Summary: The reporting player alleges that ShadowStrike_99 used offensive language and racial slurs in the team chat during a ranked match. Additionally, the reported player is accused of repeatedly sabotaging the team by intentionally feeding enemies. The incident reportedly occurred on 14 April 2026.

Behavior Category: Verbal Harassment, Intentional Sabotage/Griefing

Recommended Action: Temporary Suspension (pending review of chat logs and match data)

Closing Note: All reports are subject to thorough investigation to ensure fair and consistent application of community guidelines for all players.

---

## Explanation

### Why this satisfies Behavior Control
- The tone throughout is calm, neutral, and professional
- Facts are presented as alleged without assuming guilt
- No emotional, dramatic, or accusatory language was used
- The recommended action is reviewable — no permanent ban suggested
- The closing note is fair, balanced, and policy-aligned
- No personal commentary or editorializing was added outside the report facts

---

## Key Learning
- Behavior control allows precise shaping of tone, fairness, and response style
- Structured prompts improve consistency across all moderation reports
- Gaming platforms require neutral language to avoid bias in moderation decisions
- LLMs can be guided to behave like role-specific moderation assistants

---

## Summary
- Behavior control = guiding how the model responds
- Ensures consistent, professional, and fair moderation summaries
- Essential for trust and compliance in online gaming platforms