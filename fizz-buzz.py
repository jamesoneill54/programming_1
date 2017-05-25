n = input ()

i = 0 
while i < n:
   if (i % 3 == 2) and (i % 5 == 4):
      print "fizz-buzz"
   elif i % 3 == 2:
      print "fizz"
   elif i % 5 == 4:
      print "buzz"
   else:
      print i + 1
   i = i + 1
   
