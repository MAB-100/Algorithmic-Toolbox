def compute_operations(n):
    # Initialize DP and previous arrays
    dp = [float('inf')] * (n + 1)
    previous = [-1] * (n + 1)
    
    # Base case
    dp[1] = 0
    
    # Compute minimum operations and track previous numbers
    for i in range(1, n + 1):
        if i * 3 <= n and dp[i * 3] > dp[i] + 1:
            dp[i * 3] = dp[i] + 1
            previous[i * 3] = i
        if i * 2 <= n and dp[i * 2] > dp[i] + 1:
            dp[i * 2] = dp[i] + 1
            previous[i * 2] = i
        if i + 1 <= n and dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
            previous[i + 1] = i
    
    # Reconstruct the sequence from n to 1
    sequence = []
    while n != -1:
        sequence.append(n)
        n = previous[n]
    
    sequence.reverse()
    
    return sequence

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)  # Number of operations
    print(*output_sequence)  # Sequence of numbers
