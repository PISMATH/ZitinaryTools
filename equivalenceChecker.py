from utils import *
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some functions.')

# Add arguments
parser.add_argument('order', type=int, help='The order you want to work at')
parser.add_argument('variables', type=str, help='Variables you are using to solve eg x, y, z, a')
parser.add_argument('first_function', type=str, help='The first function')
parser.add_argument('second_function', type=str, help='The second function')

# Parse the arguments
args = parser.parse_args()

# Use the parsed arguments
order = args.order
varsToSolve = args.variables.split(", ")

FirstData = calculate(order, varsToSolve, args.first_function)
SecondData = calculate(order, varsToSolve, args.second_function)

print("\n")

if dataIsTheSame(order, FirstData, SecondData):
    print("The first function is the same as the second")
    print("Here is the data")
    outputData(order, varsToSolve, FirstData)

else:
    print("They are different")
    print("Here is the data for the first one")
    outputData(order, varsToSolve, FirstData)

    print("And For the second")
    outputData(order, varsToSolve, SecondData)

    userDiffenceMap = input("Would you like a difference map (y/n): ")
    if YesOrNoInput(userDiffenceMap):
        outputDifferenceMap(order, varsToSolve, FirstData, SecondData)
