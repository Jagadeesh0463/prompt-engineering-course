# 🚀 Prompting Techniques Foundation

This project contains simple, beginner-friendly examples to learn core prompting techniques using Python and AI APIs.

It demonstrates how different prompting styles (zero-shot, one-shot, few-shot, etc.) help control and improve AI responses.

---

## 📚 Topics Covered

* Zero-shot prompting
* One-shot prompting
* Few-shot prompting
* Multi-shot prompting
* Chain-of-Thought prompting
* Zero-shot Chain-of-Thought prompting

---

## 📁 Project Structure

prompt-engineering-course/

│
├── examples/               # Runnable Python files
├── prompts/                # Concept explanation files
├── assignments/            # Assignment instructions
├── helper.py               # API helper function
├── requirements.txt        # Required Python libraries
├── .env                    # API key (not pushed to GitHub)
└── .gitignore              # Ignored files

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

python3 -m venv venv

Activate it:

source venv/bin/activate

---

### 2️⃣ Install Dependencies

Install all required Python libraries using:

pip install -r requirements.txt

---

## 📦 requirements.txt Explained

The `requirements.txt` file contains all the Python packages needed to run this project.

### Why it is important

* Ensures all users install the same dependencies
* Makes project setup quick and easy
* Avoids compatibility issues

### Example packages used

* python-dotenv → to load environment variables
* openai / google-generativeai → to interact with AI models

---

### 3️⃣ Create .env File

Create a file named `.env` in the root folder and add:

GEMINI_API_KEY=your_api_key_here

---

### 4️⃣ Run the Code

Run any example file:

python examples/01_zero_shot.py

You can also try:

python examples/02_one_shot.py
python examples/03_few_shot.py
python examples/04_multi_shot.py
python examples/05_chain_of_thought.py
python examples/06_zero_shot_cot.py

---

## 📦 .gitignore Explained

The `.gitignore` file is used to prevent unnecessary or sensitive files from being uploaded to GitHub.

### Ignored Files:

* `.venv/` or `venv/` → Virtual environment
* `.env` → Contains API keys (keep private 🔒)
* `__pycache__/` → Python cache files
* `*.pyc` → Compiled Python files
* `.DS_Store` → macOS system file
* `teacher_notes.md` → Personal notes

👉 This keeps the repository clean and secure.

---

## 🧠 What You Will Learn

* How to write effective prompts
* Difference between zero-shot, one-shot, and few-shot
* How examples influence AI output
* How to guide reasoning using chain-of-thought
* Real-world use cases using cricket-based examples

---

## 🏏 Special Note

This project uses cricket-based examples to make learning more engaging and relatable.

---

## ⚠️ Important Notes

* Do NOT upload your `.env` file to GitHub
* Always activate virtual environment before running code
* Ensure your API key is valid

---

## 🙌 Conclusion

This project helps beginners understand how prompting works in AI systems and how to control outputs effectively using structured instructions.

---

## 👨‍💻 Author

Jagadeesh S
