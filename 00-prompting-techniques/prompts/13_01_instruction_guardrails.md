        # Assignment 13_01 — Instruction Guardrails

## Task

Create one prompt that uses instruction guardrails and run it locally.

---

## Prompt Used

You are an HR Leave Policy Assistant.

Your task is to answer employee questions strictly based on the company leave policy.

### Instruction Guardrails:
1. Only use the provided policy text. Do not add or assume anything.
2. If the answer is not clearly available, say "I don’t know based on the given policy."
3. Keep the answer short, clear, and professional.
4. Do not provide personal opinions or suggestions outside policy.
5. Always guide the user to the correct next step if mentioned in policy.

### Policy Text:
- Employees must apply for leave within the same month.
- Leaves from previous months cannot be applied normally.
- Emergency leaves may be applied with manager approval through backend process.

### User Question:
"I forgot to apply leave last month due to a family emergency. Can I apply now?"

---

## Model Output

As today is the 6th of the current month, leaves for the previous month generally cannot be applied. However, since your leave was due to a family emergency, emergency or critical leaves require manager approval to be applied from the backend.

Please contact your manager immediately to discuss the process for applying your emergency leave from the backend.

---

## Explanation

### Why this is Instruction Guardrails

- The model strictly followed the policy text  
- No extra assumptions were added  
- The answer is based only on given rules  
- A clear next step is provided (contact manager)  
- Response is short, clear, and professional  

---

## Key Learning

- Instruction guardrails control model behavior  
- They reduce hallucinations  
- They ensure safe and accurate responses  

---

## Summary

- Guardrails = rules for controlled AI responses  
- Useful in HR bots, support systems, and policy assistants  
- Makes output reliable and predictable  