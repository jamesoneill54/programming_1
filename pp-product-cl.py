import sys
cmd_line = sys.argv[1]
total = 1

i = 0 
while i < len(cmd_line):
   total = total * int(cmd_line[i]) 
   i = i + 1
print total