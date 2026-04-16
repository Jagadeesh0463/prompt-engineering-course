"""
Prompting Techniques
13_11 — Privacy Guardrails

Use case:
A banking support assistant that summarizes customer issues
while masking sensitive information in the final output.
"""

import sys
from pathlib import Path
import re

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Raw customer note (contains sensitive data)
customer_note = """
Customer Name: Priya Sharma
Account Number: 458912340987
Phone Number: 9876543210
Issue: The customer reported two unknown debit card transactions
and requested that the fraud review team contact her urgently.
"""

# -------------------------------
# Privacy Pre-processing (Optional but better)
# Mask sensitive info before prompt
# -------------------------------
masked_note = customer_note
masked_note = re.sub(r"Account Number:\s*(\d{8})(\d+)", r"Account Number: ********\2", masked_note)
masked_note = re.sub(r"Phone Number:\s*\d{6}(\d+)", r"Phone Number: ******\1", masked_note)

# Prompt with privacy guardrails
prompt = f"""
Role:
You are a banking customer support summary assistant.

Task:
Generate a short internal summary from the customer note.

Privacy Guardrails:
1. Do not expose full account numbers (mask if needed).
2. Do not expose full phone numbers (mask if needed).
3. Avoid unnecessary personal details.
4. Focus only on the issue and next action.
5. Keep the output concise and professional.

Output Format:
Customer: <First Name Only>
Issue Summary: <Short description>
Next Step: <Action required>

Customer Note:
{masked_note}
"""

# Call model
response = get_completion(prompt)

# Print outputs
print("RAW INPUT:")
print("-" * 50)
print(customer_note)

print("\nMASKED INPUT:")
print("-" * 50)
print(masked_note)

print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)