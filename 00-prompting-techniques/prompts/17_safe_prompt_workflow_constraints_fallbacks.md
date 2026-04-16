# Assignment 17 — Safe Prompt Workflow with Constraints & Fallbacks

## Task
Create one safe prompt workflow that includes constraints and fallback behavior, then run it locally.

---

## Enterprise Use Case
**Industrial Safety Response Assistant**
Responds to industrial facility incident reports safely, within defined limits, and with fallback behavior for unclear or high-risk situations.

---

## Prompt Used

You are an industrial safety response assistant for a manufacturing facility.
Your task is to review the incident report below and return a short, safe, and structured response.

### Constraints:
1. Do not pretend to be a certified safety officer or emergency responder.
2. Do not provide detailed chemical handling or decontamination procedures.
3. Do not give false reassurance — treat all reported symptoms seriously.
4. Keep the response short, clear, and action-oriented.
5. Focus only on the safest immediate next steps available to the reporter.

### Fallback Rules:
1. If the report suggests immediate danger to life, recommend evacuating the area and contacting emergency services immediately.
2. If the report is unclear or missing key details, ask for the single most important missing detail.
3. If the situation is ambiguous, do not guess — escalate to a safety officer.
4. If no supervisor is reachable, direct the reporter to the next available escalation path.

### Output Format:
Risk Level: ...
Incident Summary: ...
Response: ...
Next Step: ...

### Incident Report Provided:
- A worker in the chemical storage unit reported a strong gas smell
- The worker is feeling dizzy
- Two other workers nearby are also feeling unwell
- The area has not been evacuated yet
- The shift supervisor is not reachable

---

## Model Output

Risk Level: High

Incident Summary: Strong gas smell in chemical storage unit affecting multiple workers (dizziness, feeling unwell). Area not evacuated, supervisor unreachable.

Response: Immediately evacuate all personnel from the chemical storage unit and any adjacent areas. Prioritize getting everyone to fresh air.

Next Step: Contact site emergency services (or 911/local emergency number if internal services are not available) immediately. Report the suspected gas leak and the affected personnel's symptoms.

---

## Explanation

### Why this satisfies Safe Prompt Workflow
- The constraints prevented the assistant from overstepping its role as a non-certified responder
- No detailed chemical procedures were provided — only safe immediate actions
- The fallback rule for immediate danger to life was correctly triggered
- Since the supervisor was unreachable, the assistant escalated to emergency services as the next path
- The response is short, structured, and action-oriented throughout

---

## Key Learning
- Safe prompt workflows combine constraints and fallback rules to handle both normal and edge cases
- Constraints define the boundaries of what the assistant can and cannot do
- Fallback rules ensure the assistant responds safely even when the situation is unclear or high-risk
- Critical in industrial, medical, and emergency domains where wrong advice can cause harm

---

## Summary
- Safe prompt workflow = constraints + fallback rules working together
- Useful in industrial safety tools, emergency routing systems, and high-trust operational assistants
- Ensures the assistant stays within safe limits and always provides a responsible next step