# Assignment 12 — Prompt Tuning vs Instruction Tuning

## Task
Compare Prompt Engineering, Prompt Tuning, and Instruction Tuning using a structured prompt
with a real-world analogy for a complete beginner.

## Why this is Prompt Tuning vs Instruction Tuning
The same structured prompt is sent to the model asking it to explain three related but distinct concepts.
The model's response proves how a well-structured prompt with format instructions
produces a clean, beginner-friendly breakdown.
This shows the difference between what we do as users (prompt engineering)
versus what happens during model training (prompt tuning and instruction tuning).

## Prompt Sent to the Model

```
Explain the difference between prompt engineering, prompt tuning, and instruction tuning
for a complete beginner.
Use this format:
1. Prompt Engineering
2. Prompt Tuning
3. Instruction Tuning
4. Real-World Analogy
5. Simple Comparison
Keep it short, simple, and beginner-friendly.
Include at least one real-world analogy to make it easy to understand.
```

## Model Explanation

### 1. Prompt Engineering
Imagine you have a super smart, well-trained dog that understands human language.
Prompt engineering is like figuring out the best possible way to phrase your commands
to that dog so it understands exactly what you want and does it perfectly every time.
You are not training the dog new tricks; you are just getting very good at talking to it
effectively using its existing skills.

### 2. Prompt Tuning
This is like giving that super smart dog a tiny, specialized scent sample for one specific
type of retrieval task. You train the dog once with this scent sample linked to that task.
Now, whenever you ask it to find something related to that task, it automatically uses that
learned scent sample to adjust its searching behavior, making it slightly better at just that
one thing without changing its core training.

### 3. Instruction Tuning
Instruction tuning is like sending that super smart dog to a special advanced command school.
In this school, the dog practices understanding and responding to a huge variety of new and
complex commands it has never heard before. This training fundamentally improves the dog's
ability to understand and correctly follow any new and unseen instruction it might receive.

### 4. Real-World Analogy
Think of an experienced barista at a coffee shop:

- **Prompt Engineering:** You carefully tell the barista your order — large, extra hot,
  non-fat latte with one pump of vanilla and no foam. You are being very specific to get
  exactly what you want from their existing skills.

- **Prompt Tuning:** You give the barista a tiny, special recipe tweak card that they always
  use when making your specific signature drink. They learned to apply that exact tiny tweak
  to perfectly suit your taste, without changing how they make coffee for other customers.

- **Instruction Tuning:** The barista goes to a special Coffee Arts Academy where they learn
  to understand and create a vast array of new and complex drink orders they have never seen
  before. Their fundamental ability to interpret any kind of beverage instruction vastly improves.

### 5. Simple Comparison

- **Prompt Engineering** — Smart instructions from you to the model.
- **Prompt Tuning** — A tiny learned helper that subtly tweaks the model for one specific task.
- **Instruction Tuning** — The model itself gets smarter at understanding and following any and all instructions.

## Important Note

```
Prompt engineering = writing better prompts as a user. No training needed.
Prompt tuning      = learnable soft tokens added at training time. Model weights stay frozen.
Instruction tuning = model is fine-tuned on many instruction-response pairs. Weights change.
So in normal API usage, we are doing prompt engineering, not prompt tuning or instruction tuning.
