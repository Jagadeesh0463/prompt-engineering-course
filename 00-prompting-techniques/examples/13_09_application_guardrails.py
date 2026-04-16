"""
Prompting Techniques
13_09 — Application-Level Guardrails

Use case:
An insurance claim intake assistant where the application
redacts sensitive details before sending text to the model.
"""

import sys
from pathlib import Path
import re

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Raw claim received by the application
raw_claim = """
Customer Name: Suresh Reddy
Phone: 9123456789
Email: suresh.reddy@gmail.com
Policy Number: POL-99887766
Vehicle Number: KA05MN1234
Incident: Minor car accident due to rear-end collision in Bangalore.
Damage: Rear bumper damaged and tail light broken.
Estimated Cost: ₹25,000
"""

# Application-level guardrail:
# redact sensitive fields before the model sees the claim
sanitized_claim = re.sub(r"Customer Name:.*", "Customer Name: [REDACTED]", raw_claim)
sanitized_claim = re.sub(r"Phone:.*", "Phone: [REDACTED]", sanitized_claim)
sanitized_claim = re.sub(r"Email:.*", "Email: [REDACTED]", sanitized_claim)
sanitized_claim = re.sub(r"Policy Number:.*", "Policy Number: [REDACTED]", sanitized_claim)
sanitized_claim = re.sub(r"Vehicle Number:.*", "Vehicle Number: [REDACTED]", sanitized_claim)

# Prompt built only from the sanitized claim
prompt = f"""
Role:
You are an insurance claim processing assistant.

Task:
Summarize the following insurance claim into a short internal note.

Rules:
1. Use only the sanitized claim below.
2. Keep the summary short and professional.
3. Do not include personal identifiable information.
4. Focus only on claim details and required action.

Sanitized Claim:
{sanitized_claim}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the original claim
print("RAW CLAIM:")
print("-" * 50)
print(raw_claim)

# Print the sanitized version used by the application
print("\nSANITIZED CLAIM:")
print("-" * 50)
print(sanitized_claim)

# Print the final response
print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)