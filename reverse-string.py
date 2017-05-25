s = raw_input()
t = ""

i = 0 
while i < len(s):
   t = t + s[len(s) - 1 - i] 
   i = i + 1

print t
