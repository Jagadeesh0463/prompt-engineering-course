# Module 05 — Chain-of-Thought Prompting

## Task
Cricket Tournament Cost Calculation

## Why this is Chain-of-Thought
This prompt explicitly asks the model to think step by step and explain its reasoning.

## Prompt
A local cricket club is planning a 3-day tournament.

- Number of teams: 8
- Registration fee per team: ₹5,000
- Ground booking cost per day: ₹8,000
- Umpire charges for the full tournament: ₹6,000
- Equipment and miscellaneous cost: ₹4,500
- Sponsorship received: ₹20,000

Think through the problem step by step and calculate:
1. Total income (registration fees + sponsorship)
2. Total expenses (ground + umpire + equipment)
3. Net profit or loss
4. If the club wants a minimum profit of ₹10,000, how much should they increase the registration fee per team?
5. One suggestion to reduce costs for the next tournament

## Model Response
Let's break down the tournament finances step by step:

**Given Details:**
*   Number of teams: 8
*   Registration fee per team: ₹5,000
*   Ground booking cost per day: ₹8,000
*   Tournament duration: 3 days
*   Umpire charges for the full tournament: ₹6,000
*   Equipment and miscellaneous cost: ₹4,500
*   Sponsorship received: ₹20,000

---

**1. Total Income (registration fees + sponsorship)**

*   **Income from Registration Fees:**
    8 teams * ₹5,000/team = ₹40,000
*   **Income from Sponsorship:**
    ₹20,000
*   **Total Income:**
    ₹40,000 (Registration) + ₹20,000 (Sponsorship) = **₹60,000**

---

**2. Total Expenses (ground + umpire + equipment)**

*   **Ground Booking Cost:**
    3 days * ₹8,000/day = ₹24,000
*   **Umpire Charges:**
    ₹6,000
*   **Equipment and Miscellaneous Cost:**
    ₹4,500
*   **Total Expenses:**
    ₹24,000 (Ground) + ₹6,000 (Umpire) + ₹4,500 (Equipment) = **₹34,500**

---

**3. Net Profit or Loss**

*   **Net Profit/Loss:** Total Income - Total Expenses
    ₹60,000 - ₹34,500 = **₹25,500 (Profit)**

---

**4. If the club wants a minimum profit of ₹10,000, how much should they increase the registration fee per team?**

The club currently has a profit of ₹25,500, which already **exceeds** the minimum desired profit of ₹10,000. Therefore, they do not *need* to increase the registration fee to meet this minimum.

However, if the question implies they want to achieve an *additional* ₹10,000 in profit *beyond* their current profit (i.e., a new total profit of ₹25,500 + ₹10,000 = ₹35,500), and this additional profit should come from registration fees:

*   **Additional profit desired:** ₹10,000
*   **Increase in total registration fees needed:** ₹10,000
*   **Increase per team (with 8 teams):** ₹10,000 / 8 teams = **₹1,250**

So, if they wanted to *increase their profit by an additional* ₹10,000 (on top of the current profit), they would need to increase the registration fee per team by ₹1,250.

---

**5. One suggestion to reduce costs for the next tournament**

The largest expense category is ground booking. A good suggestion would be:

*   **Negotiate a lower ground booking rate** with the venue for the 3-day period, or **explore alternative, cheaper grounds/venues** for the next tournament.
    (Another option could be to reduce the tournament duration from 3 days to 2, which would save ₹8,000 on ground costs, but this impacts the tournament structure.)
(venv) sjagadeesh@Ss-MacBook-Air examples % 