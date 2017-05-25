n = raw_input()
a = []

while n != "end":
   n = int(n)
   a.append(n)
   n = raw_input()

i = 1
while i < len(a):
   v = a[i]
   p = i 
   while p > 0 and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   a[p] = v
   i += 1

j = 0
while j < len(a):
   print a[j]
   j += 1