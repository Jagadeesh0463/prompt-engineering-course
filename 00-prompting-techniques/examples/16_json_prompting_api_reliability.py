"""
Prompting Techniques
15 — Controlling LLM Behavior
Use case:
A game moderation report assistant that controls model behavior
to ensure professional, unbiased, and structured moderation summaries.
"""
import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Sample moderation report input
# Represents a realistic abuse report submitted by a player
moderation_report = """
Player: ShadowStrike_99
Reported By: CoolGamer_42
Game: Battle Arena Pro
Incident: The reported player used offensive language and racial slurs
in the team chat during a ranked match.
They also repeatedly sabotaged the team by intentionally feeding enemies.
The incident occurred during match ID 774421 on 14 April 2026.
"""

# Prompt with behavior control rules
# These rules shape tone, structure, fairness, and response style
prompt = f"""
Role:
You are a game moderation report assistant for an online gaming platform.

Task:
Review the moderation report below and generate a professional internal moderation summary.

Behavior Control Rules:
1. Use a calm, neutral, and professional tone at all times.
2. Do not use emotional, dramatic, or accusatory language.
3. Present the facts as reported without assuming guilt.
4. Keep the summary concise and structured.
5. Do not recommend permanent bans — recommend only reviewable actions.
6. Always end with a fair and balanced closing statement.
7. Do not editorialize or add personal commentary outside the report facts.

Required Format:
Reported Player:
Reporting Player:
Game:
Match ID:
Incident Summary:
Behavior Category:
Recommended Action:
Closing Note:

Moderation Report:
{moderation_report}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt so the reviewer can verify what was sent
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the model response
print("\nRESPONSE:")
print("-" * 50)
print(response)