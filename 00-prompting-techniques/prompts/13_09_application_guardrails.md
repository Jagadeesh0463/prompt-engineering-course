# Assignment 13_09 — Application-Level Guardrails

## Task
Create one workflow that applies an application-level guardrail before the model call.

---

## Enterprise Use Case
Insurance Claim Intake Assistant  
Redacts sensitive customer information before sending claim details to the model for summarization.

---

## Prompt Used

You are an insurance claim processing assistant.

Your task is to summarize the following insurance claim into a short internal note.

### Rules:
1. Use only the sanitized claim below.
2. Keep the summary short and professional.
3. Do not include personal identifiable information.
4. Focus only on claim details and required action.

### Sanitized Claim:
Customer Name: [REDACTED]  
Phone: [REDACTED]  
Email: [REDACTED]  
Policy Number: [REDACTED]  
Vehicle Number: [REDACTED]  
Incident: Minor car accident due to rear-end collision in Bangalore.  
Damage: Rear bumper damaged and tail light broken.  
Estimated Cost: ₹25,000  

---

## Raw Input

Customer Name: Suresh Reddy  
Phone: 9123456789  
Email: suresh.reddy@gmail.com  
Policy Number: POL-99887766  
Vehicle Number: KA05MN1234  
Incident: Minor car accident due to rear-end collision in Bangalore.  
Damage: Rear bumper damaged and tail light broken.  
Estimated Cost: ₹25,000  

---

## Processed Input (After Guardrails)

Customer Name: [REDACTED]  
Phone: [REDACTED]  
Email: [REDACTED]  
Policy Number: [REDACTED]  
Vehicle Number: [REDACTED]  
Incident: Minor car accident due to rear-end collision in Bangalore.  
Damage: Rear bumper damaged and tail light broken.  
Estimated Cost: ₹25,000  

---

## Model Output

Internal Claim Note:

Policy: [REDACTED]  
Vehicle: [REDACTED]  

Incident: Minor rear-end collision in Bangalore.  
Damage: Rear bumper damaged and tail light broken.  
Estimated Cost: ₹25,000  

Action Required: Process claim for reported damages.

---

## Explanation

### Why this is Application-Level Guardrails
- Sensitive data (name, phone, email, policy number, vehicle number) was removed before the model call  
- The model only received sanitized input  
- Prevents exposure of personal identifiable information (PII)  
- Ensures compliance with privacy and security standards  

---

## Key Learning
- Application guardrails operate before the model is called  
- They modify or filter input data at the application layer  
- Critical for handling sensitive data in real-world systems  

---

## Summary
- Application guardrails = pre-processing layer before model call  
- Used for redaction, filtering, and transformation  
- Essential in domains like insurance, healthcare, banking, and support systems  