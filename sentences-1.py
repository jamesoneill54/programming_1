import sys

lines = sys.stdin.readlines()

endings = '.!?'
sentences = []
current = []

i = 0
while i < len(lines):
   line = lines[i].strip().split()
   j = 0
   while j < len(line):
      current.append(line[j])
      if line[j][-1] in endings:
         sentences.append(' '.join(current))
         current = []
      j += 1
   i += 1

print '\n'.join(sentences)