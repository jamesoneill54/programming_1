pi = 3.141
def circumference(r):
   ans = 2 * pi * r
   return ans

def area(r):
   ans = pi * (r ** 2)
   return ans

def main():
   print circumference(2)
   print area(3)

if __name__ == "__main__":
   main()