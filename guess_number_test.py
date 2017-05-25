n = 781

i = 500
j = i
p = 0
while i != n:
   j = j / 2
   print "guess", p
   print "i =", i 
   print "j =", j
   if j > 1 and i < n:
      i = i + j
   elif j > 1 and i > n:
      i = i - j
   elif j <= 1 and i < n:
      i += 1
   elif j <= 1 and i > n:
      i -= 1
   p += 1
print "correct"