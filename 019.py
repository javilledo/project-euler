
# You are given the following information, but you may prefer to do some research for yourself.
#   1 Jan 1900 was a Monday.
#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_quantity_normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_quantity_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

years = [x for x in range(1901, 2001)]
leap_years = [x for x in years if (x % 4 == 0)]

days_dictionary = {
    0: 'Monday', 
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thusday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

day_of_the_week = (0 + 365 % 7) % 7
count_isSunday = 0

for year in years:

    if year in leap_years:
        temp_days_quantity = days_quantity_leap_year
    else:
        temp_days_quantity = days_quantity_normal_year
    
    for month_quantity_days in temp_days_quantity:
        day_of_the_week = (day_of_the_week + month_quantity_days % 7) % 7
        if day_of_the_week == 6: count_isSunday += 1

print('PROBLEM 19: %d' % (count_isSunday))
