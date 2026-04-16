"""
Assignment 10 — JSON Prompting for Structured Outputs
Task: Get book recommendations in valid JSON format
JSON Prompting = Model is instructed to return ONLY valid JSON with a clearly
                 defined structure — no extra text, no markdown, no code fences.
"""

import sys
from pathlib import Path
import json

# Allows importing helper.py from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Generate book recommendations for a beginner who wants to learn about Artificial Intelligence.
Return only valid JSON.
Do not include markdown.
Do not include code fences.
Do not add any explanation before or after the JSON.

Use this exact structure:
{
  "topic": "string",
  "audience": "string",
  "total_books": 0,
  "books": [
    {
      "rank": 1,
      "title": "string",
      "author": "string",
      "genre": "string",
      "why_read": "string",
      "difficulty": "Beginner | Intermediate | Advanced",
      "estimated_read_days": 0
    }
  ]
}

Rules:
- Recommend exactly 5 books
- Keep difficulty at Beginner or Intermediate only
- Keep why_read to one simple sentence
- Make sure estimated_read_days is a realistic number
- Focus only on AI-related books suitable for a first-time learner
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nRaw Response:")
print("-" * 50)
print(response)

print("\nParsed JSON:")
print("-" * 50)

# json.loads() converts the raw string response into a Python dictionary.
# If the model returned anything other than clean JSON, this will fail —
# that is intentional, it validates the model followed the instruction.
try:
    data = json.loads(response)
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print("The response was not valid JSON.")