# Assignment 13_12 — Tool / Action Guardrails

## Task
Create one prompt that uses tool / action guardrails.

---

## Enterprise Use Case
Cloud Access Request Assistant  
Ensures proper approval and prevents unauthorized access changes in cloud environments.

---

## Prompt Used

You are a cloud access request assistant.

Your task is to review the request and respond using the exact format below.

### Tool / Action Guardrails:
1. You may recommend steps such as submitting an access request or contacting admin.
2. Do not claim that you directly grant access.
3. Do not claim that you modify permissions.
4. Do not assume access has already been approved.
5. If access requires approval, clearly state the approval process.
6. Keep the response short, professional, and action-oriented.

### Required Format:
Allowed Action: ...
Blocked Action: ...
Next Step: ...

### Access Request:
An employee says they cannot access the production cloud environment.  
They need urgent access to deploy a fix for a live issue.  
They are requesting immediate access permissions.  

---

## Model Output

Allowed Action: Recommend submitting an urgent access request and contacting the cloud administrator for approval.  

Blocked Action: Cannot directly grant access or modify permissions.  

Next Step: Submit an access request through the official approval process and notify the admin team for expedited review.  

---

## Explanation

### Why this is Tool / Action Guardrails
- The assistant clearly **defined what actions are allowed vs not allowed**  
- It avoided claiming **direct system changes (granting access)**  
- It enforced **approval-based workflow**  
- Ensured **safe and compliant response behavior**  

---

## Key Learning
- Tool/action guardrails define **what the assistant can and cannot do**  
- Prevents false claims about system-level actions  
- Ensures alignment with **real-world operational processes**  

---

## Summary
- Tool guardrails = action boundary layer  
- Helps avoid unauthorized actions and misleading outputs  
- Critical in IT, cloud, security, and enterprise workflows  