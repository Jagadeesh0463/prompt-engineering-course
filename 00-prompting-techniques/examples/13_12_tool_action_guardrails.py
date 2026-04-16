"""
Prompting Techniques
13_12 — Tool / Action Guardrails

Use case:
A cloud access request assistant that must follow
strict action boundaries before recommending access changes.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample cloud access request
access_request = """
An employee says they cannot access the production cloud environment.
They need urgent access to deploy a fix for a live issue.
They are requesting immediate access permissions.
"""

# Prompt with tool / action guardrails
prompt = f"""
Role:
You are a cloud access request assistant.

Task:
Review the request and respond using the exact format below.

Tool / Action Guardrails:
1. You may recommend steps such as submitting an access request or contacting admin.
2. Do not claim that you directly grant access.
3. Do not claim that you modify permissions.
4. Do not assume access has already been approved.
5. If access requires approval, clearly state the approval process.
6. Keep the response short, professional, and action-oriented.

Use this exact format:
Allowed Action: ...
Blocked Action: ...
Next Step: ...

Access Request:
{access_request}
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