"""
Module 06 — Zero-shot Chain-of-Thought Prompting
Task: Cricket academy savings and planning problem
"""
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# I want the model to reason on its own without any examples
# Just giving it a real-life situation and asking it to think step by step
prompt = """
Ravi is a cricket coach running a small academy in Hyderabad.
He earns ₹95,000 per month from coaching fees.
His monthly expenses are:
- Ground rent: ₹15,000
- Equipment maintenance: ₹8,000
- Staff salary: ₹22,000
- Personal expenses: ₹18,000

He wants to save enough money to buy a professional bowling machine
that costs ₹2,40,000.

Solve this step by step and tell:
1. Total monthly expenses
2. Monthly savings after expenses
3. How many months will it take to buy the bowling machine
4. If he gets one extra batch of 10 students at ₹2,000 per student per month,
   how many months will it take now?
5. One practical suggestion to reach the goal even faster
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)
