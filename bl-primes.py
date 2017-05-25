import sys
n = int(sys.argv[1])

primes = []
i = 2
while i < n:
   j = 2
   while j < i and i % j != 0:
      j += 1
   if j >= i:
      primes.append(i)
   i += 1

k = 0 
while k < len(primes):
   print primes[k]
   k += 1