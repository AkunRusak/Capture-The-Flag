from itertools import product

def generate_truth_table(variables, expression):
    print(" | ".join(variables) + " | Result")
    print("-" * (4 * len(variables) + 10))
    for values in product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        try:
            result = eval(expression, {}, env)
            val_str = [str(int(v)) for v in values]
            print(" | ".join(val_str) + f" |   {int(result)}")
        except Exception as e:
            print("Error evaluating expression:", e)
            break

# Example usage
variables = ['A', 'B']
expression = "(A and not B) or (not A and B)"  # XOR
generate_truth_table(variables, expression)