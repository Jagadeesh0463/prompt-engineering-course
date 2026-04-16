"""
Prompting Techniques
13_02 — Scope Guardrails
Use case:
A travel expense policy assistant that must answer only in-scope questions.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

travel_policy = """
Travel Expense Policy:
- Employees can claim reimbursement for flight, train, taxi, and hotel expenses for approved business travel.
- Meal reimbursement is allowed up to ₹1,200 per day during business trips.
- All receipts must be submitted along with the claim form.
- Personal shopping, entertainment, and tourist activities are not reimbursable.
- Alcohol and personal care items are strictly not reimbursable.
- All claims must be submitted within 10 days after the trip ends.
- Late submissions beyond 10 days will not be processed without manager approval.
"""

sample_questions = [
    "I took a cab from the airport to the client office. Can I claim it?",
    "Can I get reimbursed for the new laptop bag I bought for the trip?"
]

for i, user_question in enumerate(sample_questions, start=1):
    prompt = f"""
Role:
You are a company travel expense support assistant.
Task:
Answer the employee question only if it falls within the allowed scope below.
Allowed Scope:
You may only answer questions related to:
- business travel reimbursement
- flight, train, taxi, and hotel expense claims
- meal allowance during business trips
- receipt and claim submission rules and deadlines
Out-of-Scope Topics:
Do not answer questions related to:
- salary or payroll
- leave policy
- laptop, hardware, or personal accessories
- performance review
- recruitment or onboarding
- any general HR topic not related to travel expenses
Scope Guardrails:
1. First decide whether the question is in scope or out of scope.
2. If it is in scope, answer using only the travel policy provided below.
3. If it is out of scope, do not attempt to answer the question.
4. If it is out of scope, reply exactly with:
   "This question is outside the scope of the travel expense assistant. Please contact the appropriate support team."
5. Do not make up any rules that are not in the policy.
6. Keep the answer short, clear, and professional.
Travel Policy:
{travel_policy}
Employee Question:
{user_question}
"""
    response = get_completion(prompt)
    print(f"QUESTION {i}: {user_question}")
    print("-" * 50)
    print(response)