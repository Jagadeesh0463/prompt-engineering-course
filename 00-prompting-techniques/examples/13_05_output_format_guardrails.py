"""
Prompting Techniques
13_05 — Output-Format Guardrails
Use case:
A procurement review assistant that must return output
in a fixed enterprise review format.
"""
import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))
from helper import get_completion

# Sample procurement request input
# Represents a realistic procurement submission an enterprise reviewer would receive
procurement_note = """
The vendor is proposing a 3-year software licensing contract worth ₹48,00,000.
The vendor has provided a signed NDA and a detailed product specification document.
Payment terms requested are 100% upfront before delivery.
The vendor has not submitted references from previous enterprise clients.
No SLA document has been shared yet regarding uptime guarantees or support response times.
The product has passed basic security screening by the IT team.
"""

# Prompt with strict output-format guardrails
# Guardrails ensure the model returns a consistent, parseable enterprise review format
# regardless of how the input varies — critical for automated procurement pipelines
prompt = f"""
Role:
You are a procurement review assistant for an enterprise organization.

Task:
Review the procurement note below and return the result using the exact format provided.
Do not deviate from the format under any circumstances.

Output-Format Guardrails:
1. Use exactly these five headings in this exact order:
   Procurement Summary:
   Strengths:
   Risks:
   Pending Requirements:
   Recommended Next Step:
2. Under Strengths, provide exactly 2 bullet points.
3. Under Risks, provide exactly 2 bullet points.
4. Under Pending Requirements, provide exactly 2 bullet points.
5. Keep each bullet point to one clear and concise sentence.
6. Do not return JSON or any other structured data format.
7. Do not add any introduction, conclusion, or extra headings outside the required format.
8. Do not number the headings.

Procurement Note:
{procurement_note}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt so the reviewer can verify what was sent
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the model response for review and validation
print("\nRESPONSE:")
print("-" * 50)
print(response)