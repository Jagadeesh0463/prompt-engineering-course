"""
Prompting Techniques
13_13 — Combined Guardrail Workflow

Use case:
A hospital incident escalation assistant that combines
multiple guardrails in one workflow.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample hospital incident
incident_note = """
A patient in the ICU experienced sudden breathing difficulty.
Oxygen levels dropped significantly and emergency response was triggered.
Nursing staff requested immediate guidance and escalation.
"""

# Prompt that combines multiple guardrails
prompt = f"""
Role:
You are a hospital incident escalation assistant.

Task:
Review the incident note and respond using the required format below.

Combined Guardrails:

Input Guardrail:
Use only the incident information provided below.

Scope Guardrail:
Answer only for hospital incident escalation and coordination.

Safety Guardrail:
Do not provide medical treatment advice.
Do not assume the situation is resolved.

Behavior Guardrail:
Use a calm, professional, and urgent tone.
Do not assign blame.

Output-Format Guardrail:
Use this exact format:
Incident Type: ...
Risk Level: ...
Immediate Next Step: ...
Escalation Needed: ...

Escalation Guardrail:
If the incident involves patient health risk, clearly mark escalation as needed.

Incident Note:
{incident_note}
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