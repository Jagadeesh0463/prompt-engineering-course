# Assignment 14 — Bias, Fairness & Ethical Risks

## Task

Create one prompt that includes fairness and ethics guardrails and run it locally.

---

## Enterprise Use Case

Scholarship Screening Support Assistant
Evaluates student applications for scholarship eligibility using fair and unbiased criteria.

---

## Prompt Used

You are a scholarship screening support assistant.

Your task is to write a short evaluation summary for the student application below.

### Fairness and Ethical Guardrails:

1. Evaluate only academic performance, achievements, skills, and relevant circumstances.
2. Do not make assumptions based on name, gender, religion, caste, ethnicity, or personal background.
3. Consider financial background only as supporting context, not as bias.
4. Do not treat the academic gap year as automatically negative.
5. Use a fair, neutral, and respectful tone.
6. Focus only on relevant evidence for scholarship decision-making.
7. Avoid any discriminatory or biased language.

### Output Format Guardrail:

Use this exact format:

Strengths: ...
Relevant Considerations: ...
Recommendation: ...

### Student Profile:

Student Name: Ravi Kumar
Academic Performance: 85% in undergraduate degree (Computer Science)
Achievements: Participated in national-level coding competitions, volunteer teaching in rural schools
Skills: Python, Data Structures, Problem Solving
Financial Background: Comes from a low-income family
Additional Detail: Took a 1-year gap due to family responsibilities

---

## Model Output

Strengths: Ravi Kumar demonstrates strong academic performance with an 85% in Computer Science. He possesses relevant technical skills including Python, Data Structures, and Problem Solving, further validated by participation in national-level coding competitions. His involvement in volunteer teaching in rural schools highlights a commitment to community engagement.

Relevant Considerations: Ravi comes from a low-income family, indicating potential financial need. A one-year academic gap was taken due to family responsibilities, which provides a clear reason for this period.

Recommendation: Recommended for strong consideration based on a robust academic record, demonstrated technical aptitude and extracurricular achievements, with a reasonable explanation for the academic gap, all supported by an indicated financial need.

---

## Explanation

### Why this satisfies Fairness and Ethics Guardrails

* The assistant evaluates only job-relevant academic and skill-based criteria
* No assumptions are made about personal identity (gender, caste, religion, etc.)
* Financial background is used as contextual support, not bias
* The academic gap is handled neutrally with explanation
* Language remains respectful, neutral, and professional
* Output focuses strictly on relevant evidence

---

## Key Learning

* Fairness guardrails help prevent bias in decision-support systems
* Ethical prompting ensures inclusive and unbiased AI behavior
* Structured outputs improve clarity and consistency
* Real-world applications require careful handling of sensitive attributes

---

## Summary

* Fairness + Ethics guardrails = unbiased decision support
* Ensures responsible AI usage in sensitive domains like scholarships
* Improves trust, transparency, and reliability of AI systems
