from collections import Counter
from datetime import datetime
from typing import List
import csv
import logging


def get_most_active_cookies(file_path: str, target_date: str) -> List[str]:
    """
    Returns the list of most active cookies for the given date from the log file.
    
    :param file_path: Path to the cookie log CSV file.
    :param target_date: Date string in 'YYYY-MM-DD' format (UTC).
    :return: List of most active cookies.
    """
    # parse target_date string into a date
    target_date = datetime.strptime(target_date, "%Y-%m-%d").date()
    cookies = []

    try:
        with open(file_path, mode='r', newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header 
            for row in reader:
                if len(row) != 2:
                    logging.warning(f"Skipping malformed row: {row}")
                    continue

                cookie, timestamp = row
                try:
                    #  timestamp to a date object
                    timestamp_date = datetime.fromisoformat(timestamp).date()
                    # check if the date matches the target date
                    if timestamp_date == target_date:
                        cookies.append(cookie)
                except ValueError:
                    logging.warning(f"Skipping row with invalid timestamp: {timestamp}")
                    continue

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

    if not cookies:
        return []

    # count the occurrences of each cookie on the target date
    cookie_counts = Counter(cookies)
    # find the maximum count of cookie occurrences
    max_count = max(cookie_counts.values())

   
    return [cookie for cookie, count in cookie_counts.items() if count == max_count]
