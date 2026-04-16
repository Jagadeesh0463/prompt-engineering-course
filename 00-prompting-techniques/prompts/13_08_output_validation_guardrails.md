# Assignment 13_08 — Output Validation Guardrails

## Task
Create a workflow that validates the model output after generation.

---

## Enterprise Use Case
Cybersecurity Alert Summary Assistant  
Ensures that the generated alert summary strictly follows the required format before being accepted or used in downstream systems.

---

## Prompt Used

You are a cybersecurity alert summary assistant.

Your task is to create a short cybersecurity alert summary using the exact headings below.

### Required Format:
- Alert Type:
- Affected System:
- Threat Level:
- Attack Summary:
- Recommended Action:

### Rules:
1. Use the exact headings shown above.
2. Keep each section short and professional.
3. Do not add extra headings.
4. Do not add an introduction or conclusion.

### Alert Information:
An automated system detected unusual login activity on a corporate server.  
Multiple failed login attempts were recorded from an unrecognized IP address in a foreign region.  
The attempts occurred between 2:00 AM and 2:45 AM IST.  
One successful login was recorded at 2:47 AM using valid credentials.  
The affected system hosts internal HR and payroll data.  
The security operations team has been notified.

---

## Model Output

Alert Type: Account Compromise

Affected System: Corporate server hosting internal HR and payroll data

Threat Level: Critical

Attack Summary: Multiple brute-force login attempts from an unrecognized foreign IP address, followed by one successful login using valid credentials at 2:47 AM IST.

Recommended Action: Investigate successful login, isolate affected system, and reset compromised credentials immediately.

---

## Output Validation Result

Validation passed: all required sections are present.

---

## Explanation

### Why this is Output Guardrails
- The model output was checked after generation
- Validation ensured all required sections were present
- The format compliance was enforced before accepting the output
- Prevents malformed or incomplete responses from being used

---

## Key Learning
- Output guardrails validate model responses after generation
- They ensure structure, completeness, and correctness
- Useful in enterprise systems where format consistency is critical

---

## Summary
- Output guardrails = post-model validation layer  
- Helps detect missing fields, incorrect formats, or invalid outputs  
- Common in cybersecurity, reporting tools, compliance systems, and automation pipelines  