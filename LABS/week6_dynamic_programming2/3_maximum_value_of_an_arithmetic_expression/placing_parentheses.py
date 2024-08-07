def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Unsupported operator")

def maximum_value(expression):
    # Extract digits and operators
    n = len(expression)
    num_values = (n + 1) // 2
    nums = [int(expression[2 * i]) for i in range(num_values)]
    ops = [expression[2 * i + 1] for i in range(num_values - 1)]
    
    # Initialize DP tables
    dp_max = [[float('-inf')] * num_values for _ in range(num_values)]
    dp_min = [[float('inf')] * num_values for _ in range(num_values)]
    
    # Base cases: single numbers
    for i in range(num_values):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]
    
    # Fill DP tables
    for length in range(2, num_values + 1):  # Length of subexpression
        for i in range(num_values - length + 1):
            j = i + length - 1
            for k in range(i, j):
                op = ops[k]
                max_value = evaluate(dp_max[i][k], dp_max[k + 1][j], op)
                min_value = evaluate(dp_min[i][k], dp_min[k + 1][j], op)
                
                dp_max[i][j] = max(dp_max[i][j], max_value)
                dp_min[i][j] = min(dp_min[i][j], min_value)
    
    return dp_max[0][num_values - 1]

if __name__ == "__main__":
    import sys
    input_expression = sys.stdin.read().strip()
    print(maximum_value(input_expression))
