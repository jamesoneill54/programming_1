import func_bsearch

def count(a,q):
   return func_bsearch.bsearch(a, q + 1) - func_bsearch.bsearch(a, q)

def main():
   count([2,3,6,6,7,8], 1)  # 0
   count([2,3,6,6,7,8], 2)  # 1
   count([2,3,6,6,7,8], 6)  # 2
   count([2,3,6,6,7,8], 8)  # 1
   count([2,3,6,6,7,8], 9)  # 0
   count([2,3,6,6,7,8], 4)  # 0

if __name__ == "__main__":
   main()