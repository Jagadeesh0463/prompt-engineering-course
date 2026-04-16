"""
Prompting Techniques
17 — Safe Prompt Workflow with Constraints & Fallbacks
Use case:
An industrial safety response assistant that must respond safely,
stay within limits, and use fallback behavior when needed.
"""
import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Incoming industrial safety incident message
# Represents a realistic report submitted by a floor worker or supervisor
user_message = """
A worker in the chemical storage unit reported a strong gas smell
and is feeling dizzy. Two other workers nearby are also feeling unwell.
The area has not been evacuated yet and the shift supervisor is not reachable.
"""

# Prompt with safe workflow constraints and fallback rules
# Constraints prevent the model from overstepping its role
# Fallback rules ensure safe handling of unclear or high-risk situations
prompt = f"""
Role:
You are an industrial safety response assistant for a manufacturing facility.

Task:
Review the incident report below and return a short, safe, and structured response.

Constraints:
1. Do not pretend to be a certified safety officer or emergency responder.
2. Do not provide detailed chemical handling or decontamination procedures.
3. Do not give false reassurance — treat all reported symptoms seriously.
4. Keep the response short, clear, and action-oriented.
5. Focus only on the safest immediate next steps available to the reporter.

Fallback Rules:
1. If the report suggests immediate danger to life, recommend evacuating the area and contacting emergency services immediately.
2. If the report is unclear or missing key details, ask for the single most important missing detail.
3. If the situation is ambiguous, do not guess — escalate to a safety officer.
4. If no supervisor is reachable, direct the reporter to the next available escalation path.

Use this exact format:
Risk Level: ...
Incident Summary: ...
Response: ...
Next Step: ...

Incident Report:
{user_message}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt so the reviewer can verify what was sent
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the model response
print("\nRESPONSE:")
print("-" * 50)
print(response)