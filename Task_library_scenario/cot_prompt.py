"""Chain-of-Thought prompting for the library scenario."""

import sys
from pathlib import Path

# Allow Python to find config.py in the parent Day2 folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config import client, MODEL


QUESTION = """
Is AI Fundamentals available?
If I borrow it for 7 days and return it 2 days late,
how much late fine will I pay?
"""


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful library assistant. "
                "Solve the problem step by step. "
                "Clearly identify the available copies, "
                "fine per day, late days, and total fine. "
                "End your response with: Final Answer:"
            )
        },
        {
            "role": "user",
            "content": QUESTION
        }
    ],
    temperature=0
)


print("=" * 60)
print("CHAIN-OF-THOUGHT PROMPTING")
print("=" * 60)

print("\nQUESTION:")
print(QUESTION.strip())

print("\nANSWER:")
print(response.choices[0].message.content)