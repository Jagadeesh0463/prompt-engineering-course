"""
Assignment 08 — Prompt Structuring Basics
Task: Generate a beginner fitness routine using a structured prompt
Structured Prompting = Prompt is divided into clear sections (Role, Task, Context,
                       Constraints, Output Format) so the model knows exactly
                       what to do, for whom, and how to respond.
"""

import sys
from pathlib import Path

# Allows importing helper.py from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# All 5 required sections are explicitly labeled inside the prompt.
# This structure removes ambiguity — the model knows its role,
# the task, who the user is, what limits to follow, and how to format output.
prompt = """
Role:
You are a beginner-friendly certified fitness coach.

Task:
Create a 7-day beginner fitness routine for someone who has never exercised before.

Context:
The person is a 25-year-old office worker who sits for long hours.
They can spare only 1 hour per day for exercise.
They have no gym membership and will exercise at home.
Their goal is to improve energy levels and build a basic fitness habit.

Constraints:
- No gym equipment required
- Keep exercises simple and easy to follow
- Do not use fitness jargon
- Each day must fit within 30 minutes
- Include one rest day

Output Format:
Return the plan in this format:

Day 1: [Focus Area] — [List of exercises with duration]
Day 2: [Focus Area] — [List of exercises with duration]
Day 3: [Focus Area] — [List of exercises with duration]
Day 4: REST DAY — Light stretching or walking only
Day 5: [Focus Area] — [List of exercises with duration]
Day 6: [Focus Area] — [List of exercises with duration]
Day 7: [Focus Area] — [List of exercises with duration]
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)