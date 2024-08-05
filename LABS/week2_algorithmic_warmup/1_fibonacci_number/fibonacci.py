def fibonacci_number(n):
    list = []
    list.append(0)
    list.append(1)
    for i in range(2, n+1):
        list.append(list[i-1] + list[i-2])

    return list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))