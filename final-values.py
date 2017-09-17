import sys

variables = {}

for line in sys.stdin:
   line = line.strip().split()
   var, n = line[0], line[-1]
   variables[var] = int(n)

i = 0
while i < len(variables):
   var_pos_i = sorted(variables)[i]
   print var_pos_i, variables[var_pos_i]
   i += 1