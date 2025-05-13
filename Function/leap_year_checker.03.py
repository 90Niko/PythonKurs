def is_year_leap(year):
    # LAB 4.3.1.6
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # LAB 4.3.1.7
    if month < 1 or month > 12:
        return None
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        month_lengths[1] = 29
    return month_lengths[month - 1]

def day_of_year(year, month, day):
    # New function
    if month < 1 or month > 12:
        return None

    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None

    total_days = 0
    for m in range(1, month):
        days = days_in_month(year, m)
        if days is None:
            return None
        total_days += days

    total_days += day
    return total_days


print(day_of_year(2009, 12, 31))