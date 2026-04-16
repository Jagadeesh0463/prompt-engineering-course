"""
Prompting Techniques
Assignment 14 — Bias, Fairness & Ethical Risks

Use case:
A scholarship screening support assistant that evaluates
a student application using fair and unbiased criteria.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Student application provided to the assistant
student_profile = """
Student Name: Ravi Kumar
Academic Performance: 85% in undergraduate degree (Computer Science)
Achievements: Participated in national-level coding competitions, volunteer teaching in rural schools
Skills: Python, Data Structures, Problem Solving
Financial Background: Comes from a low-income family
Additional Detail: Took a 1-year gap due to family responsibilities
"""

# Prompt with fairness and ethics guardrails
prompt = f"""
Role:
You are a scholarship screening support assistant.

Task:
Write a short evaluation summary for the student application below.

Fairness and Ethical Guardrails:
1. Evaluate only academic performance, achievements, skills, and relevant circumstances.
2. Do not make assumptions based on name, gender, religion, caste, ethnicity, or personal background.
3. Consider financial background only as supporting context, not as bias.
4. Do not treat the academic gap year as automatically negative.
5. Use a fair, neutral, and respectful tone.
6. Focus only on relevant evidence for scholarship decision-making.
7. Avoid any discriminatory or biased language.

Use this exact format:
Strengths: ...
Relevant Considerations: ...
Recommendation: ...

Student Profile:
{student_profile}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the response
print("\nRESPONSE:")
print("-" * 50)
print(response)