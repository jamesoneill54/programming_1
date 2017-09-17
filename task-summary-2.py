import sys

lines = sys.stdin.readlines()

users = {}

i = 0
while i < len(lines):
   user, task = lines[i].strip().split('/')
   program, correctness = task.split('.')[0], task.split('.')[-1]
   if user not in users:
      users[user] = []
   if correctness == 'correct' and program not in users[user]:
      users[user].append(program)
   elif correctness == 'incorrect' and program in users[user]:
      j = 0
      while j < len(users[user]) and users[user][j] != program:
         j += 1
      del users[user][j]
   i += 1

k = 0
while k < len(users):
   student = sorted(users)[k]
   print student, len(users[student])
   k += 1