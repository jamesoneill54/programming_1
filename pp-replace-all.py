import sys
pattern = sys.argv[1]
replacement = sys.argv[2]
line = raw_input()

while line != "end":
   length = len(line)
   i = 0
   while i < length:
      if line[i:i + len(pattern)] == pattern:
         line = line[:i] + replacement + line[i+len(pattern):]
      i = i + 1
   print line
   line = raw_input()