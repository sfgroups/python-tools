from datetime import datetime, timedelta, timezone

def generate_date_ranges(input_datetime):
    """
    Generate a dictionary mapping each date to its start and end datetime.

    If the input datetime is more than 2 days ago, generate ranges for full days
    (00:00:00 to 23:59:59). If it's within 2 days, go back 4 hours from the given
    datetime value and generate a single range. The last end datetime value will be the current system time.

    :param input_datetime: Input datetime as a string in 'YYYY-MM-DD HH:MM:SS' format.
    :return: Dictionary mapping each date to its start and end datetime.
    """
    # Parse input datetime
    try:
        given_datetime = datetime.strptime(input_datetime, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return "Invalid datetime format. Please use 'YYYY-MM-DD HH:MM:SS'."

    now = datetime.now(timezone.utc)
    days_difference = (now - given_datetime).days

    date_ranges = {}

    if days_difference > 2:
        # Generate full-day ranges for dates more than 2 days ago
        current_date = given_datetime.date()
        while current_date < now.date():
            start_time = datetime.combine(current_date, datetime.min.time(), tzinfo=timezone.utc)
            end_time = datetime.combine(current_date, datetime.max.time(), tzinfo=timezone.utc)
            date_ranges[current_date.strftime("%Y-%m-%d")] = {
                "start": start_time.strftime("%Y-%m-%d %H:%M:%S"),
                "end": end_time.strftime("%Y-%m-%d %H:%M:%S")
            }
            current_date += timedelta(days=1)

        # Add the current day's range
        start_time = datetime.combine(now.date(), datetime.min.time(), tzinfo=timezone.utc)
        end_time = now
        date_ranges[now.date().strftime("%Y-%m-%d")] = {
            "start": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end": end_time.strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        # For dates within 2 days, go back 4 hours
        start_time = given_datetime - timedelta(hours=4)
        end_time = now
        date_ranges[given_datetime.strftime("%Y-%m-%d")] = {
            "start": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end": end_time.strftime("%Y-%m-%d %H:%M:%S")
        }

    return date_ranges

# Example Usage
input_datetime = "2024-12-09 11:30:00"  # Replace with your desired datetime
result = generate_date_ranges(input_datetime)
print(result)



for d in result:
    print(result[d]['start'] )
    print(result[d]['end'] )
