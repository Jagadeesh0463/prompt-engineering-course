"""
Prompting Techniques
13_08 — Output Validation Guardrails
Use case:
A cybersecurity alert summary assistant that must return
a response in a required structure, and the output is validated after generation.
"""
import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Cybersecurity alert information provided to the assistant
# Represents a realistic security alert an analyst would receive
alert_note = """
An automated system detected unusual login activity on a corporate server.
Multiple failed login attempts were recorded from an unrecognized IP address in a foreign region.
The attempts occurred between 2:00 AM and 2:45 AM IST.
One successful login was recorded at 2:47 AM using valid credentials.
The affected system hosts internal HR and payroll data.
The security operations team has been notified.
"""

# Prompt with required structure
# Output-format rules are embedded so the model returns a consistent, validatable response
prompt = f"""
Role:
You are a cybersecurity alert summary assistant.

Task:
Create a short cybersecurity alert summary using the exact headings below.

Required Format:
Alert Type:
Affected System:
Threat Level:
Attack Summary:
Recommended Action:

Rules:
1. Use the exact headings shown above.
2. Keep each section short and professional.
3. Do not add extra headings.
4. Do not add an introduction or conclusion.

Alert Information:
{alert_note}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt so the reviewer can verify what was sent
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the raw model response
print("\nRESPONSE:")
print("-" * 50)
print(response)

# Output validation guardrail:
# After the model responds, we check whether all required sections are present.
# This ensures the model did not skip or rename any required heading.
required_sections = [
    "Alert Type:",
    "Affected System:",
    "Threat Level:",
    "Attack Summary:",
    "Recommended Action:"
]

missing_sections = [
    section for section in required_sections if section not in response
]

print("\nOUTPUT VALIDATION RESULT:")
print("-" * 50)
if not missing_sections:
    print("Validation passed: all required sections are present.")
else:
    print("Validation failed: missing sections found.")
    print("Missing:", ", ".join(missing_sections))