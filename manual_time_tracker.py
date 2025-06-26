"""
$ python manual_tracker.py
Enter times in 24-hour format (HH:MM)
Date (YYYY-MM-DD): 2025-06-25
Start AM: 08:45
Start Lunch: 12:30
End Lunch: 13:15
End PM: 17:30
Logged: 7.50 hours
Total this week (including today): 15.00 / 44.00
Entry saved.
"""

import csv
import os
from datetime import datetime, timedelta

LOG_FILE = "work_log.csv"
DATETIME_FORMAT = "%Y-%m-%d %H:%M"

def get_current_week():
    return datetime.now().isocalendar().week

def get_limits():
    week = get_current_week()
    is_even = (week % 2 == 0)
    if is_even:
        return 44.0, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    else:
        return 36.0, ['Monday', 'Tuesday', 'Wednesday', 'Thursday']

def calculate_duration(start_am, end_lunch, start_pm, end_pm):
    dur1 = end_lunch - start_am
    dur2 = end_pm - start_pm
    total = dur1 + dur2
    return round(total.total_seconds() / 3600.0, 2)

def read_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, newline='') as f:
        return list(csv.DictReader(f))

def write_log(entry):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "start_am", "end_lunch", "start_pm", "end_pm", "duration_hr"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)

def get_total_hours_this_week():
    logs = read_log()
    week_hours = 0.0
    allowed_days = get_limits()[1]
    now = datetime.now()
    this_week = now.isocalendar().week
    for entry in logs:
        try:
            date_obj = datetime.strptime(entry["date"], "%Y-%m-%d")
            if date_obj.isocalendar().week == this_week and date_obj.strftime("%A") in allowed_days:
                week_hours += float(entry["duration_hr"])
        except:
            continue
    return round(week_hours, 2)

def main():
    print("Enter times in 24-hour format (HH:MM)")

    date_str = input("Date (YYYY-MM-DD): ").strip()
    start_am_str = input("Start AM: ").strip()
    end_lunch_str = input("Start Lunch: ").strip()
    start_pm_str = input("End Lunch: ").strip()
    end_pm_str = input("End PM: ").strip()

    try:
        start_am = datetime.strptime(f"{date_str} {start_am_str}", DATETIME_FORMAT)
        end_lunch = datetime.strptime(f"{date_str} {end_lunch_str}", DATETIME_FORMAT)
        start_pm = datetime.strptime(f"{date_str} {start_pm_str}", DATETIME_FORMAT)
        end_pm = datetime.strptime(f"{date_str} {end_pm_str}", DATETIME_FORMAT)
    except ValueError as e:
        print(f"Error: {e}")
        return

    duration = calculate_duration(start_am, end_lunch, start_pm, end_pm)
    total_week = get_total_hours_this_week() + duration
    limit, _ = get_limits()

    print(f"Logged: {duration:.2f} hours")
    print(f"Total this week (including today): {total_week:.2f} / {limit:.2f}")

    if total_week > limit:
        print("WARNING: You are over the allowed weekly limit.")

    entry = {
        "date": date_str,
        "start_am": start_am_str,
        "end_lunch": end_lunch_str,
        "start_pm": start_pm_str,
        "end_pm": end_pm_str,
        "duration_hr": duration
    }
    write_log(entry)
    print("Entry saved.")

if __name__ == "__main__":
    main()