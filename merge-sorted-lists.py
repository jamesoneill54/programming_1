n = raw_input()
a = []

while n != "end":
   n = int(n)
   a.append(n)
   n = raw_input()

n = raw_input()
b = []

while n != "end":
   n = int(n)
   b.append(n)
   n = raw_input()

i = 0
j = 0 
while i < len(a) and j < len(b):
   if a[i] >= b[j]:
      print b[j]
      j += 1
   else:
      print a[i]
      i += 1
while i < len(a) or j < len(b):
   if i < len(a):
      print a[i]
      i += 1
   elif j < len(b):
      print b[j]
      j += 1