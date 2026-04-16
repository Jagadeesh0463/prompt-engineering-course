# Assignment 09 — Prompt Reuse & Versioning

## Task
Cloud Kitchen Business Ideas for a First-time Entrepreneur in Hyderabad

## Why this is Prompt Reuse & Versioning
The same task is written in two versions using shared variables.
Version 1 is a basic prompt with no structure.
Version 2 is improved with Role, Context, Constraints, and Output Format.
The shared variables (business_type, location, budget, audience) are reused in both versions —
changing one variable automatically updates both prompts without rewriting anything.

## Shared Variables
- business_type: cloud kitchen
- location: a mid-sized city in India like Hyderabad
- budget: a low budget of ₹50,000 to ₹1,00,000
- audience: a first-time entrepreneur with no prior restaurant experience

## Prompt Version 1 (Basic)

Give me business ideas for a cloud kitchen.

## Response Version 1

Response:
--------------------------------------------------
Cloud kitchens offer incredible flexibility and lower overheads compared to traditional
restaurants, making them perfect for experimenting with diverse food concepts.
Here are some business ideas:

1. The Plant-Based Powerhouse — Wholly vegan comfort food targeting health-conscious customers.
2. Keto & Low-Carb Kitchen — Dedicated keto-friendly meals for diet-committed customers.
3. Gourmet Breakfast & Brunch Delivery — Elevated breakfast items beyond the typical.
4. Late-Night Munchies & Dessert Hub — Comfort food and desserts for late-night cravings.
5. Subscription Meal Prep Service — Weekly pre-cooked healthy meals for busy professionals.
6. Ghost Restaurant Empire — Multiple virtual brands running from one physical kitchen.
7. Office Catering & Corporate Lunches — Bento boxes and healthy lunches for businesses.

======================================================================

## Prompt Version 2 (Structured & Improved)

Role:
You are a practical business advisor who specializes in food startups and cloud kitchens.

Task:
Generate 5 cloud kitchen business ideas for a first-time entrepreneur with no prior
restaurant experience.

Context:
The person wants to start a cloud kitchen in a mid-sized city in India like Hyderabad.
They have a low budget of ₹50,000 to ₹1,00,000 to invest.
They want ideas that are low-risk, easy to start, and have good demand.

Constraints:
- Keep the language simple and beginner-friendly
- Each idea must be realistic for a small budget
- Do not suggest ideas that need a large team or complex equipment
- Focus on ideas with high demand in Indian cities

Output Format:
Idea 1: [Name] — [What it is] — [Why it will work]
Idea 2: [Name] — [What it is] — [Why it will work]
Idea 3: [Name] — [What it is] — [Why it will work]
Idea 4: [Name] — [What it is] — [Why it will work]
Idea 5: [Name] — [What it is] — [Why it will work]

## Response Version 2

Response:
--------------------------------------------------
Idea 1: The Wholesome Tiffin — Simple home-style meals (Roti, Dal, Sabzi) delivered daily
through online platforms — High demand among bachelors and working professionals in Hyderabad
who want healthy, affordable home-cooked food. Uses basic kitchen equipment and everyday
ingredients, keeping costs low.

Idea 2: Chai & Comfort Bites — Hot Indian chai with popular snacks like Samosas,
Pakoras, and Sandwiches — Chai is a daily ritual for millions. Both chai and fried snacks
have excellent profit margins and require minimal equipment.

Idea 3: South Indian Breakfast Express — Classic breakfast items like soft Idli, crispy Vada,
Upma, and Poha with sambar and chutney — Breakfast staples in Hyderabad with consistent
daily demand. Batter can be prepared in batches making service efficient and low-cost.

Idea 4: Biryani Bowl Blitz — 1-2 types of well-made Biryani (Veg or Egg) served in
single-serve bowls with raita — Biryani is king in Hyderabad. A focused quality offering
with simplified menu reduces complexity and ingredient costs while ensuring steady demand.

Idea 5: Paratha Power-Up — Stuffed parathas (Aloo, Gobi, Paneer) served with curd,
pickle, and dal — Versatile meal for breakfast, lunch, or dinner. Ingredients are basic
and affordable, equipment is minimal, and parathas are universally loved comfort food.

## What Improved from V1 to V2

Version 1 gave generic global ideas with no relevance to India, budget, or experience level.
Version 2 gave 5 specific, realistic, budget-friendly ideas tailored to Hyderabad,
each explained in a clear Name — What — Why format.

The only thing that changed was the prompt structure.
The task remained exactly the same.