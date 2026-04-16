"""
Prompting Techniques
13_10 — Escalation / Handoff Guardrails

Use case:
A military incident reporting assistant that must
escalate critical threats instead of handling them independently.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample incoming military incident
incident_message = """
Multiple unidentified drones detected near the restricted military base perimeter.
One drone appears to be attempting surveillance over ammunition storage.
No confirmation yet on origin or intent.
"""

# Prompt with escalation / handoff guardrails
prompt = f"""
Role:
You are a military incident reporting assistant.

Task:
Review the message below and respond using the required format.

Escalation / Handoff Guardrails:
1. If the message indicates a potential security threat, do not treat it as routine.
2. If there is any risk to national security, escalate immediately to higher command.
3. Do not speculate or assume unverified details.
4. Do not provide tactical or operational advice.
5. Keep the response short, clear, and strictly factual.
6. Clearly indicate when the case must be handed off.

Use this exact format:
Escalation Needed: ...
Reason: ...
Immediate Next Step: ...

Message:
{incident_message}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the response
print("\nRESPONSE:")
print("-" * 50)
print(response)