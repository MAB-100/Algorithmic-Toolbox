def fibonacci_last_digit(n):
    list = []
    list.append(0)
    list.append(1)
    for i in range(2, n+1):
        list.append(list[i-1] + list[i-2])
    
    result = list[n]

    return result % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
