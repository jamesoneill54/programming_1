import sys

stack = []

for line in sys.stdin:
   line = line.strip()
   if line != '-':
      stack.append(line)
   else:
      stack.pop()

for n in stack:
   print n 