import sys

def count_on_after(n, middle, bottom):
   matches = 0
   i = 0
   while n + (i * 2) <= bottom[-1]:
      if (n + i in middle) and (n + (i * 2) in bottom):
         matches += 1
      i += 1
   return matches


def count_before(n, middle, bottom):
   matches = 0
   i = 1
   while n - (i * 2) >= bottom[0]:
      if (n - i in middle) and (n - (i * 2) in bottom):
         matches += 1
      i += 1
   return matches


def main():
   three_lines = []
   for line in sys.stdin:
      line = line.strip().split()
      i = 0
      while i < len(line):
         line[i] = int(line[i])
         i += 1
      three_lines.append(line)
   line_a, line_b, line_c = three_lines[0], three_lines[1], three_lines[2]
   
   straight_lines = 0
   for n in line_a:
      straight_lines += count_on_after(n, line_b, line_c)
      straight_lines += count_before(n, line_b, line_c)
   print straight_lines


if __name__ == '__main__':
   main()