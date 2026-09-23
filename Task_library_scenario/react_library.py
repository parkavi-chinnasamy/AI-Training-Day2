"""ReAct demonstration using library tools."""

import sys
from pathlib import Path

# Allow Python to find modules in the current folder
# and config.py in the parent Day2 folder.
sys.path.append(str(Path(__file__).resolve().parent))
sys.path.append(str(Path(__file__).resolve().parent.parent))

from library_tools import (
    check_book_availability,
    get_fine_per_day,
    calculate_fine
)


BOOK = "AI Fundamentals"
LATE_DAYS = 2


QUESTION = (
    "Is AI Fundamentals available? "
    "If I borrow it for 7 days and return it 2 days late, "
    "how much late fine will I pay?"
)


print("=" * 60)
print("REACT LIBRARY SCENARIO")
print("=" * 60)

print("\nQUESTION:")
print(QUESTION)


# Step 1
print("\nThought: I need to check whether the book is available.")

availability = check_book_availability(BOOK)

print("Action: check_book_availability")
print("Observation:", availability)


# Step 2
print("\nThought: I need to find the fine charged per day.")

fine_per_day = get_fine_per_day(BOOK)

print("Action: get_fine_per_day")
print("Observation: ₹", fine_per_day)


# Step 3
print("\nThought: I know the late days and fine per day, so I can calculate the fine.")

fine = calculate_fine(fine_per_day, LATE_DAYS)

print("Action: calculate_fine")
print("Observation: ₹", fine)


# Final answer
print("\nFINAL ANSWER:")

print(
    f"Yes, {BOOK} is available. "
    f"There are {availability.split()[0]} copies available. "
    f"The fine is ₹{fine_per_day} per day. "
    f"For {LATE_DAYS} late days, the total late fine is ₹{fine}."
)