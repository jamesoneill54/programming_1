import sys

def find_tasks_on_line():
   line = sys.stdin.readline().strip('\n')
   while line != 'end':
      i = 0
      while i < len(line):
         if line[i] == '+':
            j = i + 1
            while j < len(line) and line[j] != '+':
               j += 1
            if j < len(line) and line[j - 3:j] == '.py':
               print line[i + 1:j]
         i += 1
      line = sys.stdin.readline().strip('\n')


def main():
   find_tasks_on_line()


if __name__ == '__main__':
   main()