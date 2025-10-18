from datetime import datetime, timedelta

def date_range(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return []

    if start > end:
        return []

    result = []
    current = start
    while current <= end:
        result.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)

    return result

print(date_range('2022-01-01', '2022-01-03'))
print(date_range('2022-01-03', '2022-01-01'))
print(date_range('2022-02-30', '2022-02-31'))

