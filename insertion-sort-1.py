n = raw_input()
a = []

while n != "end":
   n = int(n)
   a.append(n)
   n = raw_input()

n = input()
p = len(a)
while p > 0 and n < a[p - 1]:
   p -= 1
print p 