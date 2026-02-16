"""Calendar utilities for Self Study Session C.

C.8: create a module with leap year, weekday, week number (+ docstrings)
C.9: extend module for EU/US parsing and combined dictionary output
"""

from datetime import date, datetime


# C.8 requirement: leap year check
def is_leap_year(year: int) -> bool:
    """Return True if `year` is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# C.8 requirement: weekday for a given date
def day_of_week(day: int, month: int, year: int) -> str:
    """Return weekday name (e.g. Monday) for a given date."""
    return date(year, month, day).strftime("%A")


# C.8 requirement: week number for a given date
def week_number(day: int, month: int, year: int) -> int:
    """Return ISO week number for a given date."""
    return date(year, month, day).isocalendar().week


# C.9 requirement: handle EU and US date formats
def parse_date(date_str: str, style: str = "EU") -> tuple[int, int, int]:
    """Parse date string and return (day, month, year).

    style='EU' expects dd/mm/yyyy, style='US' expects mm/dd/yyyy.
    """
    if style.upper() == "EU":
        d = datetime.strptime(date_str, "%d/%m/%Y")
    elif style.upper() == "US":
        d = datetime.strptime(date_str, "%m/%d/%Y")
    else:
        raise ValueError("style must be 'EU' or 'US'")
    return d.day, d.month, d.year


# C.9 requirement: return all requested info in one dictionary
def date_info(date_str: str, style: str = "EU") -> dict:
    """Return dictionary with keys: leapyear, weekday, week."""
    day, month, year = parse_date(date_str, style)
    return {
        "leapyear": is_leap_year(year),
        "weekday": day_of_week(day, month, year),
        "week": week_number(day, month, year),
    }
