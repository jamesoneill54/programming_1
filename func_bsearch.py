def bsearch(a,q):
   low = 0
   high = len(a)
   mid = len(a) / 2
   while low < high:
      if q > a[mid]:
         low = mid + 1
      else: 
         high = mid
      mid = (low + high) / 2
   return low