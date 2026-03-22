# Module 06 — Zero-shot Chain-of-Thought Prompting

## Task
Cricket Academy Financial Planning

## Why this is Zero-shot Chain-of-Thought
This prompt does not provide examples but encourages reasoning by asking the model to solve the problem step by step.

## Prompt
Ravi is a cricket coach running a small academy in Hyderabad.

He earns ₹95,000 per month.

Expenses:
- Ground rent: ₹15,000
- Equipment maintenance: ₹8,000
- Staff salary: ₹22,000
- Personal expenses: ₹18,000

He wants to save ₹2,40,000 for a bowling machine.

Solve step by step:
1. Total monthly expenses
2. Monthly savings
3. Time required to reach the goal
4. Time required with extra 10 students paying ₹2,000 each
5. One suggestion to achieve the goal faster

## Model Response

Response:
--------------------------------------------------
Let's break down Ravi's finances step by step:

**Ravi's Financial Situation:**
*   **Monthly Income:** ₹95,000
*   **Target Savings Goal (Bowling Machine):** ₹2,40,000

**Monthly Expenses:**
*   Ground rent: ₹15,000
*   Equipment maintenance: ₹8,000
*   Staff salary: ₹22,000
*   Personal expenses: ₹18,000

---

**1. Total monthly expenses**
*   Ground rent + Equipment maintenance + Staff salary + Personal expenses
*   ₹15,000 + ₹8,000 + ₹22,000 + ₹18,000 = **₹63,000**

**2. Monthly savings after expenses**
*   Monthly Income - Total Monthly Expenses
*   ₹95,000 - ₹63,000 = **₹32,000**

**3. How many months will it take to buy the bowling machine**
*   Cost of Bowling Machine / Monthly Savings
*   ₹2,40,000 / ₹32,000 = **7.5 months**

---

**4. If he gets one extra batch of 10 students at ₹2,000 per student per month, how many months will it take now?**

*   **New additional income:** 10 students * ₹2,000/student = ₹20,000 per month
*   **New total monthly income:** Original income + Additional income
    *   ₹95,000 + ₹20,000 = ₹1,15,000
*   **New total monthly expenses:** (Assuming expenses like ground rent, equipment, staff salary don't significantly increase for one extra batch, and personal expenses remain the same)
    *   Still ₹63,000
*   **New monthly savings:** New total monthly income - Total monthly expenses
    *   ₹1,15,000 - ₹63,000 = ₹52,000
*   **New time to buy the bowling machine:** Cost of Bowling Machine / New Monthly Savings
    *   ₹2,40,000 / ₹52,000 = **approximately 4.62 months** (or 4 months and about 19 days)

---

**5. One practical suggestion to reach the goal even faster**

A practical suggestion would be to **offer specialized weekend workshops or short-term intensive camps** during school holidays. This leverages his existing infrastructure and staff for additional, concentrated income without permanently increasing his monthly operational costs as much as adding a full new batch might entail in the long run. He could charge a premium for these specialized programs, targeting specific skill development (e.g., fast bowling techniques, spin bowling mastery).