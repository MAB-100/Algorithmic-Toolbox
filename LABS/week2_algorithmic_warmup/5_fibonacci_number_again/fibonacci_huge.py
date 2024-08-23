def pisano_period(m):
    a, b = 0, 1
    for i in range(0, m*m):
        a, b = b, (a+b) % m
        if a == 0 and b == 1:
            return i + 1


def fibonacci_number(n):
    list = []
    list.append(0)
    list.append(1)
    for i in range(2, n+1):
        list.append(list[i-1] + list[i-2])
    return list[n]


def fibonacci_huge(n, m):
    pissan_period = pisano_period(m)
    n = n % pissan_period
    return fibonacci_number(n) % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
    