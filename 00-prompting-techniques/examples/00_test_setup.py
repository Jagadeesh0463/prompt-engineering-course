import sys
from pathlib import Path
from helper import get_completion

# Allows importing helper.py from the project root,
# regardless of where this script is run from
sys.path.append(str(Path(__file__).resolve().parent.parent))

prompt = """
Summarize the following in one simple sentence:
Rohit Sharma is one of India's greatest opening batsmen who holds the record 
for the highest individual score in ODI cricket, has led the Indian team to 
multiple tournament victories, and is known for his elegant batting style 
and ability to perform under pressure in big matches.
"""

response = get_completion(prompt)
print(response)