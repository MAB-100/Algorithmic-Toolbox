def maximum_gold(capacity, weights):
    # Number of gold bars
    n = len(weights)
    
    # DP array where dp[w] represents the maximum weight that can be achieved with capacity w
    dp = [0] * (capacity + 1)
    
    # Fill the dp array using the weights of the gold bars
    for weight in weights:
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + weight)
    
    # The maximum weight of gold that can be fit into the backpack of given capacity
    return dp[capacity]

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    input_capacity = data[0]
    n = data[1]
    input_weights = data[2:]
    
    assert len(input_weights) == n
    
    print(maximum_gold(input_capacity, input_weights))
