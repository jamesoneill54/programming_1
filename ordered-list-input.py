import sys

sys.stdout.write('Enter "1" for ascending ordered list, "2" for decending ordered list.\n')
list_type = input()

sys.stdout.write('Enter list length in positive integer form.\n')
n = input()

with open('input.txt', 'w') as f:
   
   if list_type == 1:       #ascending order 'if' statement
      i = 0
      while i < n:
         f.write(str(i) + ' ')
         i += 1

   elif list_type == 2:     #descending order 'if' statement
      i = 0
      while i < n:
         f.write(str(n - i - 1) + ' ')
         i += 1

sys.stdout.write('ordered list was sent to "input.txt" in current directory.\n')