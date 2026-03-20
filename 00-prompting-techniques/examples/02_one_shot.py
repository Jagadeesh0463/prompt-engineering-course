"""
Assignment 02 — One-shot Prompting
Task: Convert cricket commentary into professional tone
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Convert the cricket commentary into a professional and formal tone.

Example:
Input: What a crazy six! The batsman is destroying the bowlers!
Output: That was an exceptional shot. The batsman is performing remarkably well against the bowlers.

Now do the same for:
Input: This bowler is getting smashed everywhere, no control at all!
Output:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)