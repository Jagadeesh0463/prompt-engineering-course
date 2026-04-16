"""
Prompting Techniques
Example: Prompt Tuning vs Instruction Tuning
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

simple_prompt = """
Explain the difference between prompt engineering, prompt tuning, and instruction tuning
for a complete beginner.

Use this format:
1. Prompt Engineering
2. Prompt Tuning
3. Instruction Tuning
4. Real-World Analogy
5. Simple Comparison

Keep it short, simple, and beginner-friendly.
Include at least one real-world analogy to make it easy to understand.
"""

response = get_completion(simple_prompt)

print("PROMPT:")
print("-" * 50)
print(simple_prompt)

print("\nMODEL EXPLANATION:")
print("-" * 50)
print(response)

print("\n" + "=" * 70)
print("IMPORTANT NOTE")
print("-" * 50)
print("Prompt engineering = writing better prompts as a user. No training needed.")
print("Prompt tuning      = learnable soft tokens added at training time. Model weights stay frozen.")
print("Instruction tuning = model is fine-tuned on many instruction-response pairs. Weights change.")
print("So in normal API usage, we are doing prompt engineering, not prompt tuning or instruction tuning.")