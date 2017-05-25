lines = raw_input()
a = []

while lines != "end":
   a.append(lines)
   lines = raw_input()

i = 0
while i < len(a):
   p = i 
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   temp = a[p]
   a[p] = a[i]
   a[i] = temp
   print a[i]
   i += 1