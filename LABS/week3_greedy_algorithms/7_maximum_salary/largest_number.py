from functools import cmp_to_key

def compare(x, y):
    # Custom comparator function
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def largest_number(numbers):
    # Convert all numbers to strings
    numbers = list(map(str, numbers))
    
    # Sort numbers based on the custom comparator
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    
    # Join sorted numbers to form the largest number
    largest_num = ''.join(sorted_numbers)
    
    # Handle the case where there are leading zeros (e.g., "0000")
    return largest_num if largest_num[0] != '0' else '0'

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
