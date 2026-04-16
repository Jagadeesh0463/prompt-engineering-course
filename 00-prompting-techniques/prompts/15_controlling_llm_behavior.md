# Assignment 15 — Controlling LLM Behavior

## Task

Create one prompt that controls the model’s behavior and run it locally.

---

## Enterprise Use Case

Executive Briefing Assistant
Communicates business updates in a concise, structured, and professional manner for leadership.

---

## Prompt Used

You are an executive briefing assistant.

Your task is to write a short executive-level business update based on the information below.

### Behavior Controls:

1. Use a formal and professional tone.
2. Keep the response concise and to the point.
3. Focus only on key business impact, progress, and risks.
4. Avoid unnecessary technical details or jargon.
5. Maintain a neutral and factual style (no opinions).
6. Structure the response clearly for quick executive reading.
7. End with a single forward-looking statement.

### Output Format Guardrail:

Use this format:

Summary: ...
Key Impact: ...
Risks/Considerations: ...
Next Step: ...

### Update Information:

The company launched a new customer analytics dashboard this quarter.
User adoption increased by 25% within the first month.
Customer support tickets related to reporting issues dropped by 30%.
Some enterprise clients requested additional customization features.
The product team plans to release enhancements in the next quarter.

---

## Model Output

Summary: The new customer analytics dashboard launched this quarter has demonstrated strong initial user adoption and operational efficiencies.

Key Impact: User adoption increased by 25% within the first month, and customer support tickets related to reporting issues dropped by 30%.

Risks/Considerations: Some enterprise clients have requested additional customization features, highlighting potential future development needs to meet diverse client requirements.

Next Step: The product team plans to release further enhancements to the dashboard in the next quarter.

---

## Explanation

### Why this satisfies Behavior Control

* The assistant strictly follows a formal and professional tone
* The response is concise and avoids unnecessary detail
* Focus is maintained on business impact, progress, and risks
* No casual or conversational language is used
* Output is structured for quick executive readability
* A clear forward-looking statement is included

---

## Key Learning

* Behavior control allows precise shaping of tone, structure, and style
* Structured prompts improve consistency in outputs
* Business use cases require clarity, neutrality, and brevity
* LLMs can be guided to behave like role-specific assistants

---

## Summary

* Behavior control = guiding how the model responds
* Ensures consistent, professional, and business-ready outputs
* Essential for enterprise communication systems
