import sys

def only_numbers(a):
   for char in a:
      orig = char
      if char[0] == '-':
         char = char[1:]
      if '.' in char:
         floatnum = True
         for n in char.split('.'):
            if not n.isdigit():
               floatnum = False
         if floatnum and len(char.split('.')) == 2:
            char = ''.join(char.split('.'))
      if char.isdigit():
         print orig



def main():
   lines = sys.stdin.read().split()
   only_numbers(lines)


if __name__ == '__main__':
   main()