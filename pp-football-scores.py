import sys
total_score = int(sys.argv[1])

i = 0
while 3 * i <= total_score:
   print i, total_score - (i * 3)
   i = i + 1