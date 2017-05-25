n = raw_input()
prefix = []
prev = 0

while n != "end":
   n = int(n)
   if n >= prev:
      prefix.append(n)
      prev = n
   n = raw_input()

i = 0 
while i < len(prefix):
   print prefix[len(prefix) - i - 1]
   i += 1