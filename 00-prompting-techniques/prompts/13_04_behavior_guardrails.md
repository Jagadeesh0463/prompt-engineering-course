# Assignment 13_04 — Behavior Guardrails

## Task
Create one prompt that uses behavior guardrails and run it locally.

---

## Prompt Used

You are a compliance notification assistant for an enterprise organization.
Your task is to draft a professional internal notification informing employees about a compliance update.

### Behavior Guardrails:
1. Maintain a formal and professional tone.
2. Be clear, concise, and structured.
3. Avoid threatening or alarming language.
4. Do not exaggerate consequences; state them factually.
5. Do not include assumptions beyond the provided information.
6. Emphasize importance without creating panic.
7. Encourage timely action in a respectful manner.
8. Ensure the message is suitable for organization-wide communication.
9. End with a clear and supportive closing statement.

### Compliance Information Provided:
- The company has updated its data privacy policy.
- All employees must complete mandatory data protection training within 7 days.
- Failure to comply may result in temporary access restrictions to internal systems.
- The update is part of regulatory requirements and internal security improvements.

---

## Model Output

**Subject:** Important: Updated Data Privacy Policy and Mandatory Data Protection Training

Dear Employees,

This notification serves to inform you of an important update to our company's Data Privacy Policy, effective immediately. This update is a critical step in strengthening our internal security measures and ensuring full compliance with current regulatory requirements concerning data protection.

As a mandatory component of this update, all employees are required to complete a new Data Protection Training module. This training is designed to provide you with essential information and best practices for safeguarding sensitive data, which is paramount to our operational integrity and the trust of our stakeholders.

**Key Action Required:**
- **Mandatory Training:** All employees must complete the updated Data Protection Training.
- **Deadline:** The training must be completed within **7 calendar days** of this notification.
- **Access:** Details on how to access the training module can be found on the Company Intranet under 'Compliance' or via the Learning Management System (LMS).

**Consequences of Non-Compliance:**
Failure to complete the mandatory Data Protection Training within the stipulated 7-day period may result in temporary access restrictions to internal systems. We encourage all employees to prioritize this essential training to avoid any disruption to your work.

Your prompt completion of this training is crucial for maintaining a secure data environment and upholding our commitment to data privacy. We appreciate your cooperation and dedication to these vital compliance standards.

Should you encounter any technical issues or have questions regarding the training, please contact the IT Help Desk or the Compliance Department.

Thank you for your immediate attention to this important matter.

Sincerely,
The Compliance Department

---

## Explanation

### Why this is Behavior Guardrails
- The tone throughout is formal, professional, and respectful
- Consequences are stated factually without exaggeration or alarming language
- No assumptions were added beyond the provided compliance information
- The message is structured clearly with action items and a deadline
- It closes with a supportive and cooperative statement

---

## Key Learning
- Behavior guardrails control how the model communicates, not just what it says
- They are different from scope and safety guardrails — behavior guardrails shape tone, style, and structure
- Useful when the output needs to meet professional or organizational standards

---

## Summary
- Behavior guardrails = communication rules for AI-generated content
- Useful in enterprise tools, HR systems, legal drafting, and compliance assistants
- Ensures the output is appropriate, professional, and safe for organization-wide use