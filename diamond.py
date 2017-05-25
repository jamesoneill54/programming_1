import sys
n = sys.argv[1]
n = int(n) 

i = 0 
while i * 2 < n:
   print " " * (n / 2 - i) + "*" * (i * 2 + 1) + " " * (n / 2 - i)
   i += 1

while i * 2 < n * 2:
   print " " 
   i += 1 