"""
Module 01 — Zero-shot Prompting
Task: Generate concise summary (Cricket domain)
Zero-shot = No examples given to model, only instruction.
"""

import sys
from pathlib import Path

# Allows importing helper.py from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Summarize the following cricket match report into 4 simple bullet points:
India scored 285 runs batting first. Virat Kohli scored 120 runs.
Australia started strong but lost quick wickets in middle overs.
Indian bowlers maintained pressure and won the match by 35 runs.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)