def swap(a, i, j):
   temp = a[i]
   a[i] = a[j]
   a[j] = temp

def find_smallest_value(a, i):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   return p

def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_value(a, i)
      swap(a, i, p)
      i += 1
   return a

def main():
   a = [23, 1, 2, 3, 1, 2, 3, 0]
   print selection_sort(a)

if __name__ == "__main__":
   main()