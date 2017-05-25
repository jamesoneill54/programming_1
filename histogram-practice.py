n = raw_input()
a = [0] * 10

while n != "end":
   n = int(n)
   a[n] = a[n] + 1
   n = raw_input()

i = 0
while i < len(a):
   print i, "*" * a[i]
   i += 1 