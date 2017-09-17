import secret_number

def play():
   high = 1000
   low = 1
   mid = (high + low) / 2
   guess = secret_number.guess(mid)
   while guess != 'correct':
      if guess == 'too-low':
         low = mid + 1
         mid = (high + low) / 2
      elif guess == 'too-high':
         high = mid
         mid = (high + low) / 2
      guess = secret_number.guess(mid)


def main():
   pass

if __name__ == '__main__':
   main()