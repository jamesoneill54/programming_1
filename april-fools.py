day = 17        # In the range 1 to 31.
month = 1       # In the range 1 to 12.

is_april_fools_day = (month == 4) and (day == 1)
is_st_patricks_day = (month == 3) and (day == 17)

print "It is April Fool's day:", is_april_fools_day
print "It is St Patrick's day:", is_st_patricks_day

# Take summer to be June, July and August, and take winter
# to be December, January and February.

is_summer = (month >= 6) and (month <= 8) and (day >= 1)
is_winter = (month == 12) and (day >= 1) or (month <= 2) and (day >= 1)

print "It is summer:", is_summer
print "It is winter:", is_winter
