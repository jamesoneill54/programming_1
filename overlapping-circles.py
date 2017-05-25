x1 = 3
y1 = 5
r1 = 3

x2 = 14
y2 = 16
r2 = 2

if (x2 - x1) ** 2 + (y2 - y1) ** 2 > (r1 + r2) ** 2:
   print "Non-overlapping circles."
elif (x2 - x1) ** 2 + (y2 - y1) ** 2 < (r1 + r2) ** 2:
   print "Overlapping circles."

