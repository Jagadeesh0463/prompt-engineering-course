"""
Assignment 11 — Prompt Design Patterns
Task: Apply 4 prompt design patterns to a cricket coaching feedback note
Prompt Design Patterns = Different ways to instruct the model on the same input text.
                         Same input, different pattern = completely different output.
"""

import sys
from pathlib import Path

# Allows importing helper.py from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Same input text used across all 4 patterns — this is the core rule of this assignment.
# Changing the pattern changes the output, not the input.
feedback_text = """
Ravi has been training at our cricket academy for the past three months.
His batting technique has improved significantly and he shows great focus during practice.
However, his fielding needs more work, especially in catching high balls.
His fitness levels are average and he should work on building stamina.
Overall, Ravi is a dedicated student and shows good potential for the upcoming trials.
"""

# Pattern 1: Classification — model assigns a category or label to the input
classification_prompt = f"""
Classify the overall performance of the student in the following feedback note
as Excellent, Good, Average, or Poor.
Feedback:
{feedback_text}
"""

# Pattern 2: Extraction — model pulls specific structured information from the input
extraction_prompt = f"""
Extract the following details from the feedback note.
Return the answer in this format:
- Student Name:
- Strong Areas:
- Areas to Improve:
- Fitness Level:
- Overall Potential:
Feedback:
{feedback_text}
"""

# Pattern 3: Transformation — model rewrites the same content in a different style or tone
transformation_prompt = f"""
Rewrite the following student feedback note in a formal tone
suitable for an official academy progress report.
Feedback:
{feedback_text}
"""

# Pattern 4: Generation — model creates new content based on the input
generation_prompt = f"""
Based on the following feedback note, generate a short motivational message
from the coach to encourage the student before the upcoming trials.
Feedback:
{feedback_text}
"""

classification_response  = get_completion(classification_prompt)
extraction_response      = get_completion(extraction_prompt)
transformation_response  = get_completion(transformation_prompt)
generation_response      = get_completion(generation_prompt)

print("PATTERN 1 — CLASSIFICATION")
print("-" * 50)
print(classification_response)

print("\nPATTERN 2 — EXTRACTION")
print("-" * 50)
print(extraction_response)

print("\nPATTERN 3 — TRANSFORMATION")
print("-" * 50)
print(transformation_response)

print("\nPATTERN 4 — GENERATION")
print("-" * 50)
print(generation_response)