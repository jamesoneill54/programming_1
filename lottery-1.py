import sys

def lottery(draw, tickets):
   prizes = [0, 1, 5, 100]
   for line in tickets:
      matches = 0
      for num in line:
         if num in draw:
            matches += 1
      print prizes[matches]


def main():
   lottery_draw = sys.argv[1:]
   tickets = []
   for line in sys.stdin:
      tickets.append(line.strip().split())
   lottery(lottery_draw, tickets)


if __name__ == '__main__':
   main()