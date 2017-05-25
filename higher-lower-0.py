previous = input()

while previous != 0:
   current = input()
   if current != 0:
      if current > previous:
         print "higher"
      elif current < previous:
         print "lower"
      else: 
         print "equal"
   temp = current
   previous = temp
