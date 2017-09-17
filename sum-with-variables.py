import sys

variables = {}
total = 0

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   line = lines[i].strip().split()
   if len(line) == 1:
      if line[0].isdigit():
         total += int(line[0])
      else:
         total += variables[line[0]]
   else:
      var_name, n = line[0], int(line[-1])
      variables[var_name] = n
   i += 1

print total