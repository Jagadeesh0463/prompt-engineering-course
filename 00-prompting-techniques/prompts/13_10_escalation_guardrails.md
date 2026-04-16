# Assignment 13_10 — Escalation / Handoff Guardrails

## Task
Create one prompt that uses escalation or handoff guardrails.

---

## Enterprise Use Case
Military Incident Reporting Assistant  
Detects potential threats and escalates critical incidents to higher command instead of handling them independently.

---

## Prompt Used

You are a military incident reporting assistant.

Your task is to review the message below and respond using the required format.

### Escalation / Handoff Guardrails:
1. If the message indicates a potential security threat, do not treat it as routine.
2. If there is any risk to national security, escalate immediately to higher command.
3. Do not speculate or assume unverified details.
4. Do not provide tactical or operational advice.
5. Keep the response short, clear, and strictly factual.
6. Clearly indicate when the case must be handed off.

### Required Format:
Escalation Needed: ...
Reason: ...
Immediate Next Step: ...

### Message:
Multiple unidentified drones detected near the restricted military base perimeter.  
One drone appears to be attempting surveillance over ammunition storage.  
No confirmation yet on origin or intent.  

---

## Model Output

Escalation Needed: Yes  

Reason: Unidentified drones near a restricted military base with possible surveillance over ammunition storage indicate a potential security threat.  

Immediate Next Step: Immediately escalate to higher command and initiate base security protocols for threat assessment.  

---

## Explanation

### Why this is Escalation Guardrails
- The system identified a **potential national security threat**
- Instead of handling it normally, it **triggered escalation**
- The response avoided assumptions and stayed factual
- A clear **handoff to higher command** was provided

---

## Key Learning
- Escalation guardrails detect **high-risk or critical scenarios**
- They prevent the model from handling dangerous situations alone
- They enforce **handoff to humans or higher authority**

---

## Summary
- Escalation guardrails = decision layer for critical cases  
- Used in military, healthcare, aviation, and emergency systems  
- Ensures safe handling of high-risk situations  