line = raw_input()
emp_numbers = []
emp_names = []

while line != "end":
   emp_numbers.append(int(line[0:8]))
   emp_names.append(line[9:])
   line = raw_input()

line = raw_input()

while line != "end":
   line = int(line[:8])
   i = 0 
   while i < len(emp_numbers):
      if line == emp_numbers[i]:
         print emp_names[i]
      i += 1
   line = raw_input()