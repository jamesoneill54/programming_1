import sys

def gcd(a, b):
   a = int(a)
   b = int(b)
   while b != 0:
      remainder = a % b
      a = b
      b = remainder
   return a


def main():
   numbers = sorted(sys.argv[1:], reverse=True)
   while len(numbers) != 1:
      num1, num2 = numbers.pop(0), numbers.pop(0)
      numbers.append(gcd(num1, num2))
   print numbers[0]


if __name__ == '__main__':
   main()