def binary_search_first(keys, query):
    left, right = 0, len(keys) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == query:
            result = mid
            right = mid - 1  # Continue searching in the left half to find the first occurrence
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Read the sorted array
    index = 0
    n = int(data[index])
    index += 1
    keys = list(map(int, data[index:index + n]))
    index += n
    
    # Read the queries
    m = int(data[index])
    index += 1
    queries = list(map(int, data[index:index + m]))
    
    # Process each query
    results = []
    for query in queries:
        results.append(str(binary_search_first(keys, query)))
    
    # Output results
    print(' '.join(results))

if __name__ == '__main__':
    main()
