def swap(a, i, j):
   temp = a[i]
   a[i] = a[j]
   a[j] = temp

def reverse(a):
   i = 0
   while i < len(a) / 2:
      j = len(a) - i - 1
      swap(a, i, j)
      i += 1

def main():
   a = [1, 2, 3, 4]
   swap(a, 0, 3)
   print a
   reverse(a)
   print a

if __name__ == "__main__":
   main()