def edit_distance(first_string, second_string):
    m, n = len(first_string), len(second_string)
    
    # Create a (m+1) x (n+1) DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the DP table
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting all characters from first_string to match an empty second_string
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting all characters into an empty first_string to match second_string
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No additional cost if characters match
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  # Delete
                               dp[i][j - 1] + 1,  # Insert
                               dp[i - 1][j - 1] + 1)  # Replace
    
    return dp[m][n]

if __name__ == "__main__":
    first_string = input().strip()
    second_string = input().strip()
    print(edit_distance(first_string, second_string))
