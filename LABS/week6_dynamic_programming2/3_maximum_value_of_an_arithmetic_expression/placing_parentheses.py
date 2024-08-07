def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Invalid operator")
 
def maximum_value(expression):
    # Extract numbers and operators
    numbers = []
    operators = []
   
    for i in range(len(expression)):
        if i % 2 == 0:
            numbers.append(int(expression[i]))
        else:
            operators.append(expression[i])
   
    n = len(numbers)
   
    # Initialize DP tables
    max_val = [[0] * n for _ in range(n)]
    min_val = [[0] * n for _ in range(n)]
   
    # Fill the tables
    for i in range(n):
        max_val[i][i] = numbers[i]
        min_val[i][i] = numbers[i]
 
    for length in range(2, n + 1):  # length of the sub-expression
        for i in range(n - length + 1):
            j = i + length - 1
            max_val[i][j] = float('-inf')
            min_val[i][j] = float('inf')
           
            for k in range(i, j):  # k is the position of the operator
                op = operators[k]
                a = evaluate(max_val[i][k], max_val[k + 1][j], op)
                b = evaluate(max_val[i][k], min_val[k + 1][j], op)
                c = evaluate(min_val[i][k], max_val[k + 1][j], op)
                d = evaluate(min_val[i][k], min_val[k + 1][j], op)
               
                max_val[i][j] = max(max_val[i][j], a, b, c, d)
                min_val[i][j] = min(min_val[i][j], a, b, c, d)
 
    return max_val[0][n - 1]
 
if __name__ == "__main__":
    print(maximum_value(input().strip()))