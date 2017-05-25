a = raw_input().split()
print a
i = 1
counter = 0
while i <= len(a):
   if int(a[i - 1]) > int(a[i]) and  i < len(a):
      temp = a[i]
      a[i] = a[i - 1]
      a[i - 1] = a[i]
      counter += 1
      i += 1
   elif int(a[i - 1]) <= int(a[i]) and i < len(a):
      i += 1
   elif i == len(a) and counter != 0:
      i = 1
      counter = 0
   elif i == len(a) and counter == 0:
      i += 1
      print a 
print a