"""Library tools for the custom ReAct scenario."""

BOOKS = {
    "AI Fundamentals": {
        "available": 3,
        "fine_per_day": 5
    },
    "Python Programming": {
        "available": 2,
        "fine_per_day": 4
    },
    "Database Systems": {
        "available": 0,
        "fine_per_day": 6
    }
}


def check_book_availability(book_name):
    """Check the number of available copies."""
    book = BOOKS.get(book_name)

    if book is None:
        return "Book not found."

    return f"{book['available']} copies available."


def get_fine_per_day(book_name):
    """Get the late-return fine per day."""
    book = BOOKS.get(book_name)

    if book is None:
        return "Book not found."

    return book["fine_per_day"]


def calculate_fine(fine_per_day, late_days):
    """Calculate the total late fine."""
    return fine_per_day * late_days