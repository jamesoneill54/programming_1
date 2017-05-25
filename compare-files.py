import sys

with open(sys.argv[1]) as f:
   file_a = f.readlines()

with open(sys.argv[2]) as f:
   file_b = f.readlines()

if file_a != file_b:
   i = 0                                              #i is the line number        
   while i < len(file_a) and file_a[i].strip() == file_b[i].strip():
      i += 1
   if file_a[i] == '' or file_b[i] == '':
      print i, 0
   line_a = file_a[i]
   line_b = file_b[i]
   p = 0                                              #p is the character position
   while p < len(line_a) and line_a[p] == line_b[p]:
      p += 1
   print i, p 