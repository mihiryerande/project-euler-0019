# Problem 19:
#     Counting Sundays
#
# Description:
#     You are given the following information, but you may prefer to do some research for yourself.
#
#       * 1 Jan 1900 was a Monday.
#       * Thirty days has September,
#         April, June and November.
#         All the rest have thirty-one,
#         Saving February alone,
#         Which has twenty-eight, rain or shine.
#         And on leap years, twenty-nine.
#       * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#     How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Number of days in month given by index,
#   not accounting for extra day in February on leap years
MONTH_DAY_COUNTS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(m, y):
    """
    Returns the number of days in month `m`, during year `y`.

    Args:
        m (int): Natural number in range [0, 11]
        y (int): Natural number representing year in Gregorian calendar

    Returns:
        (int): Number of days in month `m`, during year `y`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(m) == int and 0 <= m < 12
    assert type(y) == int and y > 0

    global MONTH_DAY_COUNTS
    return MONTH_DAY_COUNTS[m] + int(m == 1 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))


def main():
    """
    Returns the number of Sundays falling on the 1st of the month
      during the 20th century (1 Jan 1901 to 31 Dec 2000).

    Returns:
        (int): Number of first Sundays in 20th century
    """
    # Jan 1, 1901 was a Tuesday
    year = 1901
    month = 0
    weekday = 2

    # Iterate through the 1sts of each month,
    #   counting how many are Sundays
    count = 0
    while year < 2001:
        # Check if current weekday is a Sunday
        count += int(weekday == 0)

        # Step to next 1st of month
        days = days_in_month(month, year)
        weekday = (weekday + days) % 7
        year_step, month = divmod(month + 1, 12)
        year += year_step

    return count


if __name__ == '__main__':
    first_sundays = main()
    print('Number of Sundays falling on 1st of the month during the 20th century:')
    print('  {}'.format(first_sundays))
