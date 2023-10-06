import calendar

def display_calendar(year, month):
    """Display the calendar for a specific month and year."""
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    print(f"\n{month_name} {year}")
    print(" Mo Tu We Th Fr Sa Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("  
