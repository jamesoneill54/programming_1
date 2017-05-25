n = raw_input()
a = []

while n != "end":
   n = int(n)
   a.append(n)
   n = raw_input()

i = input()
p = i  
while i < len(a):
   if a[i] < a[p]:
      p = i 
   i += 1

print p 