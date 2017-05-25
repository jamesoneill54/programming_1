n = raw_input()
a = []

while n != "end":
   n = int(n)
   a.append(n)
   n = raw_input()

n = input()
a.append(n)
i = 0
while i < len(a):
   v = a[i]
   p = i
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   i += 1
a[p] = v
print a 