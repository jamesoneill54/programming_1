import func_bsearch

def contains(a,q):
   p = func_bsearch.bsearch(a,q)
   if p < len(a) and a[p] == q: 
      return p
   else:
      return 0