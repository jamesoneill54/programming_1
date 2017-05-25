n = input ()

i = 0
previous = 0
current = 1
while i < n:
   print current
   temp = previous
   previous = current
   current = current + temp
   i = i + 1
