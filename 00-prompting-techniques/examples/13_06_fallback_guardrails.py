"""
Prompting Techniques
13_06 — Fallback Guardrails
Use case:
A policy clarification assistant that must use fallback behavior
when the request is unclear, incomplete, or requires HR or legal review.
"""
import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Sample policy clarification request
# Represents a realistic employee query an HR assistant would receive
policy_note = """
An employee is asking whether they can work from a different country
for 3 months while on a personal visit.
The request does not mention their employment type, tax residency,
or whether their manager has approved the arrangement.
"""

# Prompt with fallback guardrails
# Fallback rules ensure the assistant does not give risky advice
# when the request is ambiguous or touches legal or HR boundaries
prompt = f"""
Role:
You are a company policy clarification assistant.

Task:
Review the employee request below and provide a safe and responsible response.

Fallback Guardrails:
1. If the request is clear and low-risk, provide a short and practical policy clarification.
2. If the request is missing key details, ask for the missing information before proceeding.
3. If the request involves legal, tax, or compliance risk, do not give a final approval or recommendation.
4. In high-risk or unclear cases, recommend escalation to the HR or legal team.
5. Do not assume or fabricate policy details that are not provided.
6. Keep the response short, professional, and action-oriented.

Use this exact format:
Decision: ...
Reason: ...
Next Step: ...

Employee Request:
{policy_note}
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