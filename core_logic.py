import calendar
from datetime import date

YEAR = 2026
TAGS = ["Religion", "Health", "Career", "Finance", "Relationships", "Personal Growth", "Values","Family", "Other"]

def get_iso_weeks_in_month(year, month):
    weeks = []
    days_in_month = calendar.monthrange(year, month)[1]
    for d in range(1, days_in_month + 1):
        dt = date(year, month, d)
        if dt.weekday() == 3:  # Thursday Rule
            weeks.append(dt.isocalendar()[1])
    return sorted(list(set(weeks)))

def iso_week_start(year, week):
    return date.fromisocalendar(year, week, 1)