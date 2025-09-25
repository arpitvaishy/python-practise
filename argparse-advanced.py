import argparse
import math
parser = argparse.ArgumentParser(description = "Advanced Calculator")

parser.add_argument("num1" ,type = float , help = "Type First Number")
parser.add_argument("num2" ,type = float , help = "Type Second Number")
parser.add_argument("operation" ,choices=["add", "sub", "mul", "div", "sqr", "sqrt", "cub"], help = "type your preferred operation")

args = parser.parse_args()

c = math.sqrt(args.num1) # just wanted to add that we can use in this way as well.


#print(args); prints details of the input given

if (args.operation == "add"):
    print(f"Your required sum is {args.num1 + args.num2}.")

elif (args.operation == "sub"):
    print(f"Your required difference is {args.num1 - args.num2}.")

elif (args.operation == "mul"):
    print(f"You are getting {args.num1 ** args.num2} when you multiply {args.num1} and {args.num2}.")

elif (args.operation == "div"):
    print(f"You are getting {args.num1 / args.num2} when you divide {args.num1} and {args.num2}.")

elif (args.operation == "sqr"):
    print(f"The square of this number is {args.num1 ** args.num1}.")

elif (args.operation == "sqrt"):
    print(f"The square-root of this number is {c}.")

elif (args.operation == "cub"):
    print(f"The cube-root of this number is {args.num1 ** 3}.")

else:
    print("Some error occured")

