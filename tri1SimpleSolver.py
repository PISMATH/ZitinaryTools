from utils import *
    
userOrder = input("What order do you want to work at: ")
userVars = input("What variables are you using solve eg x, y, z, a: ")
userFunc = input("What function do you want to explore: ")

varsToSolve = userVars.split(", ")
order = int(userOrder)

data = calculate(order, varsToSolve, userFunc)
outputData(order, varsToSolve, data)