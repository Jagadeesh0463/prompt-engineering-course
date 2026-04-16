# 🚀 Prompt Engineering Course — Foundation

A structured, hands-on repository to learn prompt engineering from basics to advanced guardrail-based workflows using Python and AI models.

This project is designed to help you understand how to design, control, and evaluate prompts for real-world applications.

---

## 📌 Overview

This repository demonstrates:

* Core prompting techniques (zero-shot to few-shot)
* Reasoning patterns (Chain-of-Thought)
* Structured prompting and role-based control
* Guardrails for safety, reliability, and control
* Real-world enterprise-style use cases

The examples progress from simple concepts to advanced prompt workflows used in production systems.

---

## 📚 Topics Covered

### Core Prompting Techniques

* Zero-shot prompting
* One-shot prompting
* Few-shot prompting
* Multi-shot prompting

### Reasoning Techniques

* Chain-of-Thought prompting
* Zero-shot Chain-of-Thought

### Structured Prompting

* System vs user role prompting
* Prompt structuring basics
* JSON and structured output prompting
* Prompt design patterns
* Prompt tuning vs instruction tuning

### Guardrails & Safety

* Instruction guardrails
* Scope guardrails
* Safety guardrails
* Behavior guardrails
* Output format guardrails
* Fallback handling
* Input guardrails
* Output validation
* Application-level guardrails
* Escalation handling
* Privacy protection
* Tool/action constraints

### Advanced Workflows

* Combined guardrail workflows
* Bias, fairness, and ethical risks
* Behavior control
* Safe prompt workflows with constraints

---

## 📁 Project Structure

```id="v8e7kw"
prompt-engineering-course/
│
├── examples/        # 01–17 structured examples (basic → advanced guardrails)
├── prompts/         # Concept explanations and prompt templates
├── assignments/     # Practical tasks and solutions
├── helper.py        # API interaction helper
├── requirements.txt # Project dependencies
├── .env             # Environment variables (not committed)
└── .gitignore       # Ignored files configuration
```

---

## 📈 Learning Progression

The repository follows a structured progression:

1. Basic prompting techniques
2. Reasoning and structured prompting
3. Guardrails and safety controls
4. Advanced workflows and enterprise use cases

This helps in building a strong foundation step-by-step.

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash id="6hp5x7"
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Install Dependencies

```bash id="v8s6v3"
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```id="h6k2jn"
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Do not commit this file to GitHub

---

### 4. Run Examples

Run any example file:

```bash id="yq2v91"
python examples/01_zero_shot.py
```

You can explore all examples sequentially to understand the progression.

---

## 🧪 Assignments

The `assignments/` folder contains practical exercises focused on:

* Guardrails implementation
* Bias and fairness handling
* Behavior control
* Structured outputs
* Enterprise-style use cases

These are designed to reinforce learning through real-world scenarios.

---

## 🔐 Security & Best Practices

* Never commit `.env` files (contains secrets)
* Use virtual environments for dependency isolation
* Keep `.gitignore` properly configured
* Avoid exposing sensitive data in prompts
* Validate model outputs in critical workflows

---

## 🧩 Notes

* Code is intentionally simple and readable
* Focus is on learning prompt design, not framework complexity
* Suitable for beginners and intermediate developers

---

## 📌 Future Improvements

* Add evaluation and benchmarking examples
* Support multiple LLM providers (Ollama, OpenAI, etc.)
* Add real-world production workflows

---

## 👨‍💻 Author

**Jagadeesh S**

---

## ⭐ Summary

This project provides a complete foundation in prompt engineering — from basic prompting techniques to advanced guardrail-based workflows.

It is designed to help developers build reliable, safe, and structured AI-powered applications.
