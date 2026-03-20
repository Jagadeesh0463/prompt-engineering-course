"""
Module 01 — Zero-shot Prompting
Task: Generate creative ideas (Cricket domain)
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Zero-shot prompt (no examples, single clear task)
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