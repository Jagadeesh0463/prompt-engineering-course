"""
Prompting Techniques
Assignment 15 — Controlling LLM Behavior

Use case:
An executive briefing assistant that communicates
in a structured, concise, and business-focused style.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Business update information
update_note = """
The company launched a new customer analytics dashboard this quarter.
User adoption increased by 25% within the first month.
Customer support tickets related to reporting issues dropped by 30%.
Some enterprise clients requested additional customization features.
The product team plans to release enhancements in the next quarter.
"""

# Prompt that controls model behavior
prompt = f"""
Role:
You are an executive briefing assistant.

Task:
Write a short executive-level business update based on the information below.

Behavior Controls:
1. Use a formal and professional tone.
2. Keep the response concise and to the point.
3. Focus only on key business impact, progress, and risks.
4. Avoid unnecessary technical details or jargon.
5. Maintain a neutral and factual style (no opinions).
6. Structure the response clearly for quick executive reading.
7. End with a single forward-looking statement.

Use this format:
Summary: ...
Key Impact: ...
Risks/Considerations: ...
Next Step: ...

Update Information:
{update_note}
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