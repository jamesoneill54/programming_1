import secret_number

def play():
   i = 500
   j = i
   while secret_number.guess(i) != "correct":
      j = j / 2
      print i 
      print j
      if j > 1 and secret_number.guess(i) == "too-low":
         i = i + j
      elif j > 1 and secret_number.guess(i) == "too-high":
         i = i - j
      elif j <= 1 and secret_number.guess(i) == "too-low":
         i += 1
      elif j <= 1 and secret_number.guess(i) == "too-high":
         i -= 1

print play()