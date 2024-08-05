def max_pairwise_product(numbers): 
    n = len(numbers)
    max_product = 0
    MAX_num = max(numbers)
    numbers.remove(MAX_num)
    MAX_num2 = max(numbers)
    max_product = MAX_num * MAX_num2
    return max_product

    # for first in range(n):
    #     for second in range(first + 1, n):
    #         max_product = max(max_product,
    #             numbers[first] * numbers[second])

    # return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
