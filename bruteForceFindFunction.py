from itertools import product

def OR(a, b):
    return max(a, b)

def AND(a, b):
    return min(a, b)

# Corrected SHIFT operation using a dictionary for transitions
def SHIFT(a):
    SHIFT_map = {0: 0.5, 0.5: 1, 1: 0}
    return SHIFT_map[a]

# Apply a sequence of operations to an input value
def apply_operations(sequence, input_value):
    result = input_value
    for op in sequence:
        if op == 'SHIFT':
            result = SHIFT(result)
        elif op == 'OR':
            result = OR(result, result)
        elif op == 'AND':
            result = AND(result, result)
    return result

# Inputs and their desired NOT outputs
inputs = [0, 0.5, 1]
desired_outputs_NOT = [1, 0.5, 0]

operations = ['SHIFT', 'OR', 'AND']

def find_successful_sequences():
    current_depth = 1
    while True:  # Loop indefinitely until a solution is found or a break condition is met
        possible_sequences = [p for p in product(operations, repeat=current_depth)]
        for sequence in possible_sequences:
            results = [apply_operations(sequence, input_value) for input_value in inputs]
            if results == desired_outputs_NOT:
                return sequence, current_depth  # Return the successful sequence and its depth
        current_depth += 1
        print(f"trying depth {current_depth}")

successful_sequence, successful_depth = find_successful_sequences()

# If a successful sequence is found, print it and the depth. Otherwise, indicate failure.
if successful_sequence:
    print(f"Successful sequence for NOT operation found at depth {successful_depth}:", successful_sequence)
else:
    print("No sequence found that performs the NOT operation, stopped at depth 10 for practicality.")
