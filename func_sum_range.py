import func_bsearch

def sum_range(a,low,high):
   val_a = func_bsearch.bsearch(a,low)
   p = val_a
   total = 0
   while p < len(a) and a[p] < high:
      total = a[p] + total
      p += 1
   return total

def main():
   sum_range([2,3,6,6,7,8], 3, 7)    # 15
   sum_range([2,3,6,6,7,8], 3, 8)    # 22
   sum_range([2,3,6,6,7,8], -10, 3)  # 2
   sum_range([2,3,6,6,7,8], 7, 20)   # 15
   sum_range([2,3,6,6,7,8], 10, 20)  # 0

if __name__ == "__main__":
   main()