from itertools import product

class Zit():
    """
    Add two zit's does a 'or' operand
    Subtract two zit's does a 'and 'operand 
    Use bit negate for 'shift' operand
    """
    def __init__(self, order: int, value: int):
        assert order > 1, "ERR Zit __init__ fail: The order is two small"
        assert 0 <= value < order, "ERR Zit __init__ fail: Your value is invalid for this order"
        self.order = order
        self.value = value

    def __add__(self, other):
        """
        Do a 'or' operand
        """
        assert type(other) == type(self), "ERR attempted to or not Zit to Zit"
        assert other.order == self.order, f"ERR attempted to or Zit with order {other.order} to Zit with order {self.order}"
        return Zit(self.order, max(self.value, other.value))

    def __sub__(self, other):
        """
        Do a 'and' operand
        """
        assert type(other) == type(self), "ERR attempted to and not Zit to Zit"
        assert other.order == self.order, f"ERR attempted to and Zit with order {other.order} to Zit with order {self.order}"
        return Zit(self.order, min(self.value, other.value))

    def __invert__(self):
        """
        Do a 'shift' operand
        """
        return Zit(self.order, (self.value + 1) % self.order)

    def __eq__(self, other):
        return type(other) == type(self) and other.order == self.order and self.value == other.value

    def __str__(self):
        return f"{self.order}: {self.value}"

def YesOrNoInput(userResponse):
    if userResponse == "":
        return False
    
    if userResponse[0].lower() == 'y':
        return True
    return False

def dataIsTheSame(order, firstData, secondData):
    for key in firstData.keys():
        if firstData[key] != secondData[key]:
            return False
    return True

def func(userFunc, varsToSolve, zits):
    for name, zit in zip(varsToSolve, zits):
        exec(f"{name} = Zit({zit.order}, {zit.value})")
    resultZit = eval(userFunc)
    return resultZit

def calculate(order, varsToSolve, userFunc):
    possibleZits = [Zit(order, i) for i in range(order)]
    data = {}
    for vals in product(possibleZits, repeat=len(varsToSolve)):
        data[tuple([zit.value for zit in vals])] = func(userFunc, varsToSolve, vals)
    return data

def outputData(order, varsToSolve, data):
    if len(varsToSolve) != 2: # No special rendering
        print(varsToSolve)
        for key in data.keys():
            print(f"{list(key)}: {data[key].value}")
    
    else: # Render as a 2d matrix
        print(f"  {varsToSolve[0]}")
        print(f"{varsToSolve[1]}", end=" ")
        for row in range(order):
            for column in range(order):
                value = data[tuple([column, row])].value
                print(value, end=" " * (3 - len(str(value))))
            print("\n  ", end='')
        
def outputDifferenceMap(order, varsToSolve, firstData, secondData):
    if len(varsToSolve) != 2: # No special rendering
        print(varsToSolve)
        for firstKey, secondKey in zip(firstData.keys(), secondData.keys()):
            firstValue = firstData[firstKey]
            secondValue = secondData[secondKey]
            if firstValue == secondValue:
                print(f"{list(firstKey)}: both {firstValue}")
            else:
                print(f"\033[93m{list(firstKey)}: first {firstValue} second {secondValue}\033[0m")
    
    else: # Render as a 2d matrix
        print(f"  {varsToSolve[0]}")
        print(f"{varsToSolve[1]}", end=" ")
        for row in range(order):
            for column in range(order):
                firstValue = firstData[(column, row)].value
                secondValue = secondData[(column, row)].value
                if firstValue == secondValue:
                    print(f"{firstValue}", end=" " * (3 - len(str(firstValue))))
                else:
                    print(f"\033[93m{firstValue}\033[0m", end=" " * (3 - len(str(firstValue))))
            print("\n  ", end='')
