import sys
import math

#binary fuctions
def plus(a,b):
   return a + b

def minus(a,b):
   return a - b

def multiply(a,b):
   return a * b

def divide(a,b):
   return a / b

def power(a,b):
   return a ** b

#unary functions
def negate(a):
   return a * -1

def square(a):
   return a * a 

def square_root(a):
   return math.sqrt(a)

def log(a):
   return math.log(a)


binary = {
   "+": plus,
   "-": minus,
   "*": multiply,
   "/": divide,
   "**": power,
}

unary = {
   "n": negate,
   "s": square,
   "r": square_root,
   "l": log,
}

stack = []

op = sys.stdin.readline().split()

while 0 < len(op):
   for key in op:
      if key in binary:
         b = stack.pop()
         a = stack.pop()
         stack.append(binary[key](a,b))

      elif key in unary:
         a = stack.pop()
         stack.append(unary[key](a))

      elif key == "p":
         print stack[len(stack) - 1]

      else:
         stack.append(float(key))
   op = sys.stdin.readline().split()