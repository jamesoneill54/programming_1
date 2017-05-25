n = raw_input()
ints = []
total = 0

while n != "end":
   n = int(n)
   total = n + total
   ints.append(n)
   n = raw_input()

if ints:
   average = float(total / len(ints))
else: 
   average = 0.0

print average

i = 0
while i < len(ints):
   if ints[i] > average:
      print ints[i]
   i += 1