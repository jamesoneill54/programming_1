import sys
q = int(sys.argv[1])
integers = raw_input()

a = integers.split(',')
i = 0
while i < len(a):
   a[i] = int(a[i])
   i += 1

low = 0
high = len(a)

while low < high:
   mid = (low + high) / 2 
   if a[mid] < q:
      low = mid + 1
   else:
      high = mid
print q, 'is at position:', low, '\nSorted list:', a