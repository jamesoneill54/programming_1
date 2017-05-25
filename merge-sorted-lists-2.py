n = raw_input()
a = []

while n != 'end':
   a.append(int(n))
   n = raw_input()

n = raw_input()

while n != 'end':
   a.append(int(n))
   n = raw_input()

i = 0
while i < len(a):
   p = i 
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j 
      mergej += 1
   temp = a[p]
   a[p] = a[i]
   a[i] = temp
   print a[i]
   i += 1