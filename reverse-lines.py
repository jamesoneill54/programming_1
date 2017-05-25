s = raw_input()
lines = []

while s != "end":
   lines.append(s)
   s = raw_input()

i = 0
while i < len(lines):
   print lines[len(lines) - i - 1]
   i += 1