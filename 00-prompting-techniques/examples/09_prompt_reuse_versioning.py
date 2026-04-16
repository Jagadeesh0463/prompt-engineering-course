"""
Assignment 09 — Prompt Reuse & Versioning
Task: Generate cloud kitchen business ideas in two prompt versions
Prompt Versioning = Same task, same variables, but V1 is basic and V2 is structured.
                    This shows how prompt quality directly improves output quality.
"""

import sys
from pathlib import Path

# Allows importing helper.py from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Shared variables — reused in both versions without repeating values.
# This is the "reuse" part of Prompt Reuse & Versioning.
business_type = "cloud kitchen"
location = "a mid-sized city in India like Hyderabad"
budget = "a low budget of ₹50,000 to ₹1,00,000"
audience = "a first-time entrepreneur with no prior restaurant experience"

# Version 1: simple, no structure — just a basic instruction.
# Shows what an unguided prompt produces.
prompt_v1 = f"""
Give me business ideas for a {business_type}.
"""

# Version 2: fully structured prompt using all 5 sections.
# Same task as V1 but with Role, Context, Constraints and Output Format added.
# Shows how structure produces a more useful, tailored response.
prompt_v2 = f"""
Role:
You are a practical business advisor who specializes in food startups and cloud kitchens.

Task:
Generate 5 cloud kitchen business ideas for {audience}.

Context:
The person wants to start a {business_type} in {location}.
They have {budget} to invest.
They want ideas that are low-risk, easy to start, and have good demand.

Constraints:
- Keep the language simple and beginner-friendly
- Each idea must be realistic for a small budget
- Do not suggest ideas that need a large team or complex equipment
- Focus on ideas with high demand in Indian cities

Output Format:
Idea 1: [Name] — [What it is] — [Why it will work]
Idea 2: [Name] — [What it is] — [Why it will work]
Idea 3: [Name] — [What it is] — [Why it will work]
Idea 4: [Name] — [What it is] — [Why it will work]
Idea 5: [Name] — [What it is] — [Why it will work]
"""

response_v1 = get_completion(prompt_v1)
response_v2 = get_completion(prompt_v2)

print("PROMPT VERSION 1")
print("-" * 50)
print(prompt_v1)

print("\nRESPONSE VERSION 1")
print("-" * 50)
print(response_v1)

print("\n" + "=" * 70 + "\n")

print("PROMPT VERSION 2")
print("-" * 50)
print(prompt_v2)

print("\nRESPONSE VERSION 2")
print("-" * 50)
print(response_v2)