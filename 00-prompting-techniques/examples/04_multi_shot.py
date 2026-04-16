"""
Module 04 — Multi-shot Prompting
Task: Tag cricket news headlines with a category label
Multi-shot = Many examples (5+) given so the model learns the full label space before the real task.
"""

import sys
from pathlib import Path

# Allows importing helper.py from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Tag each cricket headline with one label only:
Performance, Injury, Selection, Record, Controversy

Headline: Virat Kohli scores a brilliant century in the third Test match.
Label: Performance

Headline: Jasprit Bumrah ruled out of the series due to a back injury.
Label: Injury

Headline: BCCI announces squad for the upcoming T20 World Cup.
Label: Selection

Headline: Rohit Sharma becomes the highest run-scorer in T20 internationals.
Label: Record

Headline: Match referee penalises team for slow over rate during the final.
Label: Controversy

Headline: Hardik Pandya returns to the squad after recovering from ankle surgery.
Label: Selection

Headline: Shubman Gill hits three consecutive half-centuries in the ODI series.
Label: Performance

Now tag this:
Headline: Ravindra Jadeja breaks the record for most catches by a fielder in Tests.
Label:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)