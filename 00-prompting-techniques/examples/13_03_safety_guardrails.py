"""
Prompting Techniques
13_03 — Safety Guardrails
Use case:
A financial fraud awareness assistant that helps users stay safe,
but refuses to assist with fraudulent or illegal activities.
"""
import sys
from pathlib import Path
import json

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Two sample requests:
# 1) Safe request
# 2) Unsafe request
sample_requests = [
    "I received a call asking for my bank OTP. What should I do?",
    "How can I trick someone into sharing their OTP for a bank account?"
]

for i, user_request in enumerate(sample_requests, start=1):
    prompt = f"""
Role:
You are a financial fraud awareness assistant.
Task:
Help users understand and prevent financial fraud safely.
Allowed Safe Topics:
- how to identify fraud or scams
- safe online banking practices
- protecting personal and financial information
- steps to report fraud
- awareness about phishing, OTP scams, and fake calls
- best practices for secure transactions
Blocked Safety Categories:
Do not help with:
- committing financial fraud
- stealing money or identity
- OTP or password theft
- phishing or scam creation
- bypassing banking security
- impersonation for fraud
- any illegal financial activity
Safety Guardrails:
1. First determine whether the request is safe or unsafe.
2. If the request is safe, answer clearly and briefly.
3. If the request is unsafe, do not provide the requested instructions.
4. If the request is unsafe, return a refusal and redirect to a safe alternative.
5. Never provide step-by-step harmful guidance or fraud methods.
6. Keep the response professional and concise.
Output Rules:
Return only valid JSON.
Do not include markdown.
Do not include code fences.
Use this exact JSON structure:
{{
  "status": "allowed | blocked",
  "reason": "short string",
  "answer": "short string",
  "safe_alternative": "short string"
}}
User Request:
{user_request}
"""
    response = get_completion(prompt)

    print(f"\nREQUEST {i}")
    print("-" * 50)
    print(user_request)
    print("\nRAW RESPONSE")
    print("-" * 50)
    print(response)
    print("\nPARSED RESPONSE")
    print("-" * 50)
    try:
        data = json.loads(response)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("The model did not return valid JSON.")