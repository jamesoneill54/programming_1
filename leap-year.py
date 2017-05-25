year = 2016

is_leap_year = (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0) 

print year, "is a leap year:", is_leap_year

# years divisible by 400 are leap years
# otherwise, a year is a leap year if it is divisible by 4 but not divisible by 100.

