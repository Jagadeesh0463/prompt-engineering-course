# Assignment 13_11 — Privacy Guardrails

## Task
Create a workflow that applies privacy guardrails to protect sensitive information in model outputs.

---

## Enterprise Use Case
Banking Customer Support Summary Assistant  
Ensures sensitive customer information like account number and phone number is not exposed in summaries.

---

## Prompt Used

You are a banking customer support summary assistant.

Your task is to generate a short internal summary from the customer note.

### Privacy Guardrails:
1. Do not expose full account numbers (mask if needed).
2. Do not expose full phone numbers (mask if needed).
3. Avoid unnecessary personal details.
4. Focus only on the issue and next action.
5. Keep the output concise and professional.

### Output Format:
Customer: <First Name Only>  
Issue Summary: <Short description>  
Next Step: <Action required>  

### Customer Note:
Customer Name: Priya Sharma  
Account Number: ********0987  
Phone Number: ******3210  
Issue: The customer reported two unknown debit card transactions  
and requested that the fraud review team contact her urgently.  

---

## Raw Input

Customer Name: Priya Sharma  
Account Number: 458912340987  
Phone Number: 9876543210  
Issue: The customer reported two unknown debit card transactions  
and requested that the fraud review team contact her urgently.  

---

## Processed Input (Masked)

Customer Name: Priya Sharma  
Account Number: ********0987  
Phone Number: ******3210  
Issue: The customer reported two unknown debit card transactions  
and requested that the fraud review team contact her urgently.  

---

## Model Output

Customer: Priya  

Issue Summary: Two unknown debit card transactions reported.  

Next Step: Fraud review team to contact customer urgently.  

---

## Explanation

### Why this is Privacy Guardrails
- Sensitive data (account number, phone number) was masked before reaching the model  
- The output avoided exposing full personal information  
- Only necessary details (issue + action) were included  
- Ensures compliance with privacy and data protection practices  

---

## Key Learning
- Privacy guardrails minimize exposure of sensitive data  
- They can be applied before (masking) and during (prompt rules) model usage  
- Important for banking, healthcare, and customer support systems  

---

## Summary
- Privacy guardrails = data protection layer  
- Prevents leakage of personal and confidential information  
- Ensures safe and responsible AI outputs  