def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Unsupported operator")

def max_expression_value(expression):
    n = len(expression)
    # Initialize DP tables
    dp_max = [[float('-inf')] * (n // 2 + 1) for _ in range(n // 2 + 1)]
    dp_min = [[float('inf')] * (n // 2 + 1) for _ in range(n // 2 + 1)]
    
    # Fill the base cases
    for i in range(n // 2 + 1):
        dp_max[i][i] = int(expression[2 * i])
        dp_min[i][i] = int(expression[2 * i])

    # Fill the DP tables
    for length in range(1, n // 2 + 1):  # Length of subexpressions
        for i in range(n // 2 - length + 1):
            j = i + length
            for k in range(2 * i + 1, 2 * j, 2):
                op = expression[k]
                max_value = evaluate(dp_max[i][k // 2 - 1], dp_max[k // 2 + 1][j], op)
                min_value = evaluate(dp_min[i][k // 2 - 1], dp_min[k // 2 + 1][j], op)
                
                dp_max[i][j] = max(dp_max[i][j], max_value)
                dp_min[i][j] = min(dp_min[i][j], min_value)
    
    return dp_max[0][n // 2]

if __name__ == "__main__":
    import sys
    input_expression = sys.stdin.read().strip()
    print(max_expression_value(input_expression))
