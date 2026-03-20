"""
Module 03 — Few-shot Prompting
Task: Classify cricket-related sentiment
"""
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Classify the sentiment of the cricket comment as Positive, Negative, or Neutral.

Comment: What an outstanding innings by the captain, pure class!
Sentiment: Positive

Comment: The team played very poorly today, disappointing performance.
Sentiment: Negative

Comment: The match will start at 7 PM IST.
Sentiment: Neutral

Comment: Rohit Sharma scored a brilliant century in the final over.
Sentiment: Positive

Comment: The batting was strong, but the bowling performance was disappointing.
Sentiment:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)