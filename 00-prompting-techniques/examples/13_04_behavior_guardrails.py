"""
Prompting Techniques
13_04 — Behavior Guardrails

Use case:
A compliance notification assistant that communicates policy updates
in a clear, professional, and non-alarming manner.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Compliance context provided to the assistant
compliance_context = """
The company has updated its data privacy policy.
All employees must complete mandatory data protection training within 7 days.
Failure to comply may result in temporary access restrictions to internal systems.
The update is part of regulatory requirements and internal security improvements.
"""

# Prompt with behavior guardrails
prompt = f"""
Role:
You are a compliance notification assistant for an enterprise organization.

Task:
Draft a professional internal notification informing employees about a compliance update.

Behavior Guardrails:
1. Maintain a formal and professional tone.
2. Be clear, concise, and structured.
3. Avoid threatening or alarming language.
4. Do not exaggerate consequences; state them factually.
5. Do not include assumptions beyond the provided information.
6. Emphasize importance without creating panic.
7. Encourage timely action in a respectful manner.
8. Ensure the message is suitable for organization-wide communication.
9. End with a clear and supportive closing statement.

Compliance Information:
{compliance_context}
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