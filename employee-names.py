import sys

with open("employees.txt") as f:
   emp_det = f.readlines()

employees = {}
i = 0
while i < len(emp_det):
   a = emp_det[i].split()
   employees[a[0]] = {
   "id": a[0],
   "name": " ".join(a[2:]),
   "dob": a[1],
   }
   i += 1

emp_id = sys.stdin.readlines()

j = 0
while j < len(emp_id):
   emp_id[j] = emp_id[j].strip()
   if emp_id[j] in employees:
      print employees[emp_id[j]]["name"]
   j += 1