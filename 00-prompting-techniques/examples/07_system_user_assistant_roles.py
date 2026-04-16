"""
Assignment 07 — System, User & Assistant Roles
Task: Role-based prompting using a customer support agent persona
Role-based prompting = System instruction defines WHO the model is,
                       User message defines WHAT the customer asks.
"""

import sys
from pathlib import Path

# Allows importing from project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Defines the model's persona and behavior boundaries for the entire conversation.
# This is the SYSTEM role — it sets context before the user speaks.
system_instruction = """
You are a professional customer support agent for FreshCart, an online grocery delivery app.

Your behavior rules:
- Always greet the customer politely by name if provided.
- Be empathetic, calm, and solution-focused at all times.
- Never argue or blame the customer.
- If you cannot resolve an issue, escalate politely by saying:
  "I will raise this to our senior team and you will hear back within 24 hours."
- Keep responses concise — no longer than 5 sentences.
- Always end with: "Is there anything else I can help you with?"
"""

# The USER role — this is what the customer types into the support chat.
user_message = """
Hi, my name is Priya. I placed an order yesterday for vegetables and milk,
but I received someone else's order. The items are completely wrong.
I need this fixed immediately as I have guests coming tonight.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.4,   # lower = more consistent, professional tone
        top_p=0.90,
        max_output_tokens=300,
    ),
)

print("SYSTEM ROLE:")
print("-" * 50)
print(system_instruction)

print("\nUSER ROLE:")
print("-" * 50)
print(user_message)

print("\nASSISTANT / MODEL RESPONSE:")
print("-" * 50)
print(response.text)