import sys

with open('input.txt', 'w') as f:
   n = 10
   f.write(str(n))
   i = 1
   while i < n:
      f.write(',' + str(n - i))
      i += 1