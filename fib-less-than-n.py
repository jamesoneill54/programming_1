n = input()

previous = 0
current = 1
while n > current:
   print current 
   temp = previous
   previous = current
   current = current + temp
