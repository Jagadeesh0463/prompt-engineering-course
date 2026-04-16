"""
Prompting Techniques
13_07 — Input Guardrails
Use case:
A gaming abuse report intake assistant that checks input
before sending it to the model.
"""
import sys
from pathlib import Path

# Allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Sample input — change reported_by to "" to test the blocked case
reporter_username = "PlayerOne_99"
reported_username = "ToxicGamer_007"
game_title = "Battle Arena Pro"
abuse_type = "harassment"
incident_description = "The reported player sent repeated offensive messages and racial slurs in the team chat during a ranked match."

# Input guardrails:
# We validate all required fields and allowed values before calling the model.
# The model is never called if any guardrail check fails.

if not reporter_username.strip():
    print("Blocked: reporter_username is required.")
elif not reported_username.strip():
    print("Blocked: reported_username is required.")
elif not game_title.strip():
    print("Blocked: game_title is required.")
elif not incident_description.strip():
    print("Blocked: incident_description is required.")
elif abuse_type.lower() not in ["harassment", "cheating", "hate speech", "spam", "threats"]:
    print("Blocked: abuse_type must be harassment, cheating, hate speech, spam, or threats.")
else:
    # Build the prompt only if all input fields pass validation
    prompt = f"""
Role:
You are a gaming abuse report intake assistant.

Task:
Convert the abuse report details below into a short internal moderation summary.

Rules:
1. Use only the details provided.
2. Keep the summary short and professional.
3. Do not make assumptions about intent beyond what is described.
4. Recommend the moderation action based on the abuse type.

Use this exact format:
Reporter: ...
Reported Player: ...
Game: ...
Abuse Type: ...
Incident Summary: ...
Recommended Action: ...

Validated Intake Details:
Reporter Username: {reporter_username}
Reported Username: {reported_username}
Game Title: {game_title}
Abuse Type: {abuse_type}
Incident Description: {incident_description}
"""

    response = get_completion(prompt)

    # Print the prompt so the reviewer can verify what was sent
    print("PROMPT:")
    print("-" * 50)
    print(prompt)

    # Print the model response
    print("\nRESPONSE:")
    print("-" * 50)
    print(response)