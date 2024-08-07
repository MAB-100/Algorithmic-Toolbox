def optimal_summands(n):
    summands = []
    current_sum = 0
    current_number = 1

    # Add numbers until the sum of summands reaches or exceeds n
    while current_sum + current_number <= n:
        summands.append(current_number)
        current_sum += current_number
        current_number += 1

    # Adjust the last number to ensure the sum is exactly n
    if current_sum < n:
        # The last number in the summands is adjusted
        summands[-1] += (n - current_sum)

    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
