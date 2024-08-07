def change(money):
    # Define the coin denominations
    coins = [1, 3, 4]
    
    # Create a DP array initialized with a large number
    dp = [float('inf')] * (money + 1)
    
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0
    
    # Fill the DP array
    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # The result is the minimum number of coins needed for 'money'
    return dp[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))
