def max_dot_product(prices, clicks):
    # Sort both lists in ascending order
    prices.sort()
    clicks.sort()
    
    # Compute the maximum dot product
    max_product = sum(p * c for p, c in zip(prices, clicks))
    
    return max_product

if __name__ == '__main__':
    import sys
    input = sys.stdin.read().split()
    
    n = int(input[0])
    prices = list(map(int, input[1:n+1]))
    clicks = list(map(int, input[n+1:2*n+1]))
    
    print(max_dot_product(prices, clicks))
