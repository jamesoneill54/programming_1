n = raw_input()
a = []

while n != "end":
   n = int(n)
   a.append(n)
   n = raw_input()

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
   i += 1

print a[len(a) / 2]