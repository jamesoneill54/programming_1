import sys


def smallest_factor(n):
   smallest_factor = 2
   while n % smallest_factor != 0:
      smallest_factor += 1
   return smallest_factor

def largest_factor(n):
   smallest_factor = 2
   while n % smallest_factor != 0:
      smallest_factor += 1
   return n / smallest_factor

def main():
   integer = int(sys.argv[1])
   first_prime = smallest_factor(integer)
   final_factors = [first_prime]
   lar_fac = largest_factor(integer)
   
   while lar_fac >= first_prime:
      next_prime = smallest_factor(lar_fac)
      final_factors.append(next_prime)
      lar_fac = largest_factor(lar_fac)
   
   i = 0
   while i < len(final_factors):
      print final_factors[i]
      i += 1


if __name__ == '__main__':
   main()