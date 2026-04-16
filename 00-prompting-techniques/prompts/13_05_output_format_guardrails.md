# Assignment 13_05 — Output-Format Guardrails

## Task
Create one prompt that uses output-format guardrails and run it locally.

---

## Enterprise Use Case
**Procurement Review Assistant**
Reviews vendor procurement submissions and returns output in a fixed, consistent enterprise format suitable for approval pipelines.

---

## Prompt Used

You are a procurement review assistant for an enterprise organization.
Your task is to review the procurement note and return the result using the exact format provided.
Do not deviate from the format under any circumstances.

### Output-Format Guardrails:
1. Use exactly these five headings in this exact order:
   - Procurement Summary:
   - Strengths:
   - Risks:
   - Pending Requirements:
   - Recommended Next Step:
2. Under Strengths, provide exactly 2 bullet points.
3. Under Risks, provide exactly 2 bullet points.
4. Under Pending Requirements, provide exactly 2 bullet points.
5. Keep each bullet point to one clear and concise sentence.
6. Do not return JSON or any other structured data format.
7. Do not add any introduction, conclusion, or extra headings outside the required format.
8. Do not number the headings.

### Procurement Note Provided:
- 3-year software licensing contract worth ₹48,00,000
- Signed NDA and product specification document submitted
- Payment terms requested: 100% upfront before delivery
- No references from previous enterprise clients submitted
- No SLA document shared for uptime or support response times
- Product has passed basic IT security screening

---

## Model Output

Procurement Summary:
Review of a ₹48,00,000, 3-year software licensing contract proposal.

Strengths:
- The vendor has provided a signed Non-Disclosure Agreement and detailed product specifications.
- Basic security screening of the product has been successfully completed by the IT team.

Risks:
- The requested 100% upfront payment terms present a significant financial risk to the organization.
- The absence of client references and a Service Level Agreement introduces performance and support uncertainties.

Pending Requirements:
- The vendor must submit verifiable references from their previous enterprise clients.
- A comprehensive Service Level Agreement detailing uptime guarantees and support response times is required.

Recommended Next Step:
Engage in further negotiation to address payment terms, acquire client references, and finalize the Service Level Agreement.

---

## Explanation

### Why this is Output-Format Guardrails
- The model returned exactly 5 headings in the correct order
- Exactly 2 bullet points appear under each required section
- No extra headings, JSON, introduction, or conclusion were added
- The output is consistent and predictable — ready for automated parsing or approval workflows

---

## Key Learning
- Output-format guardrails control the structure of the model's response
- They are different from safety, scope, and behavior guardrails — format guardrails enforce layout and structure
- Critical in enterprise systems where downstream tools depend on consistent output format

---

## Summary
- Output-format guardrails = structural rules for AI-generated content
- Useful in procurement tools, audit systems, risk dashboards, and compliance pipelines
- Ensures the response is machine-readable, reviewable, and consistent across all inputs