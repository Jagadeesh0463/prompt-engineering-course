# Assignment 13_06 — Fallback Guardrails

## Task
Create one prompt that uses fallback guardrails and run it locally.

---

## Enterprise Use Case
**Policy Clarification Assistant**
Reviews employee policy requests and uses fallback behavior when the request is unclear, incomplete, or involves legal, tax, or compliance risk.

---

## Prompt Used

You are a company policy clarification assistant.
Your task is to review the employee request below and provide a safe and responsible response.

### Fallback Guardrails:
1. If the request is clear and low-risk, provide a short and practical policy clarification.
2. If the request is missing key details, ask for the missing information before proceeding.
3. If the request involves legal, tax, or compliance risk, do not give a final approval or recommendation.
4. In high-risk or unclear cases, recommend escalation to the HR or legal team.
5. Do not assume or fabricate policy details that are not provided.
6. Keep the response short, professional, and action-oriented.

### Output Format:
Decision: ...
Reason: ...
Next Step: ...

### Employee Request Provided:
- Employee is asking whether they can work from a different country for 3 months
- Request is during a personal visit
- Employment type not mentioned
- Tax residency not mentioned
- Manager approval status not mentioned

---

## Model Output

Decision: Cannot provide an immediate approval or definitive answer.

Reason: Working from a different country introduces significant legal, tax, and compliance complexities for both the employee and the company, which require a detailed review by specialized departments. Key information such as your specific employment type, tax residency, the destination country, and manager approval is missing.

Next Step: Please submit a formal request to your HR Business Partner, ensuring you include the specific country, proposed dates, your employment type, and confirmation of your manager's preliminary approval. HR will then coordinate with relevant departments (e.g., Legal, Tax) to assess the feasibility and implications of your request.

---

## Explanation

### Why this is Fallback Guardrails
- The request was incomplete and touched legal and tax risk areas
- The model correctly triggered the fallback path instead of giving a direct answer
- No policy details were assumed or fabricated
- The response escalated to HR and Legal as instructed by the guardrail rules
- The fixed format (Decision / Reason / Next Step) was followed precisely

---

## Key Learning
- Fallback guardrails define what the model should do when it cannot safely answer
- They are different from scope, safety, and behavior guardrails — fallback guardrails handle edge cases and uncertainty
- Critical in HR, legal, and compliance tools where a wrong answer carries real risk

---

## Summary
- Fallback guardrails = safe exit paths for ambiguous or high-risk requests
- Useful in policy assistants, contract review tools, HR bots, and legal intake systems
- Prevents the model from guessing or hallucinating when important details are missing