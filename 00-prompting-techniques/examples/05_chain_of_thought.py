"""
Module 05 — Chain-of-Thought Prompting
Task: Cricket tournament cost calculation and decision making
"""
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
A local cricket club is planning a 3-day tournament.
Here are the details:

- Number of teams: 8
- Registration fee per team: ₹5,000
- Ground booking cost per day: ₹8,000
- Umpire charges for the full tournament: ₹6,000
- Equipment and miscellaneous cost: ₹4,500
- Sponsorship received: ₹20,000

Think through the problem step by step and calculate:
1. Total income (registration fees + sponsorship)
2. Total expenses (ground + umpire + equipment)
3. Net profit or loss
4. If the club wants a minimum profit of ₹10,000, how much should they increase the registration fee per team?
5. One suggestion to reduce costs for the next tournament
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)
