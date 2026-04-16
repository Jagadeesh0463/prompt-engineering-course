"""
Prompting Techniques
13_01 — Instruction Guardrails
Use case:
A leave policy assistant that must follow clear instructions.
"""

import sys
from pathlib import Path

# allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# sample leave policy text that the model is allowed to use
leave_policy = """
Leave Policy:
- Leaves for the previous month must be applied before the 5th of the current month.
- After the 5th of the current month, previous month leaves cannot be applied.
- Emergency or critical leaves require manager approval to be applied from the backend.
- Casual leaves must be applied at least 1 day in advance.
- More than 3 consecutive days of leave requires HR notification.
- Leaves without approval will be marked as Loss of Pay (LOP).
"""

# sample employee question
employee_question = """
I was on leave from 28th to 31st of last month due to a family emergency at home.
Today is the 6th of the current month.
Can I still apply for those leaves?
"""

# prompt with instruction guardrails
# these rules tell the model exactly how it should behave
prompt = f"""
Role:
You are an HR leave policy assistant for a company.

Task:
Answer the employee question using only the leave policy provided below.

Instruction Guardrails:
1. Use only the information from the leave policy text. Do not add any outside rules.
2. Do not invent or assume any company rules that are not mentioned in the policy.
3. If the policy does not clearly answer the question, say:
   "Please contact HR or your manager for clarification."
4. Keep the answer short, clear, and to the point.
5. Use a polite and professional tone at all times.
6. If the situation involves an emergency, mention the manager approval process.
7. End with one practical next-step suggestion for the employee.

Leave Policy:
{leave_policy}

Employee Question:
{employee_question}
"""

# send the prompt to the model
response = get_completion(prompt)

# print the model response
print(response)