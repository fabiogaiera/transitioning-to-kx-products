from datetime import datetime

import pytz


def is_us_dst(date):
    """
    Returns True if the given date is during Daylight Saving Time in the U.S. (Eastern Time).

    Parameters:
        date (datetime): A timezone-aware or naive datetime object. Naive datetimes are assumed to be in UTC.

    Returns:
        bool: True if the date is in DST, False otherwise.
    """
    # Use US Eastern time zone as a reference
    eastern = pytz.timezone("US/Eastern")

    # If input is naive (no timezone), assume UTC and convert
    if date.tzinfo is None:
        date = pytz.utc.localize(date)

    # Convert to US Eastern time
    local_dt = date.astimezone(eastern)

    # Check if DST is in effect
    return bool(local_dt.dst())
