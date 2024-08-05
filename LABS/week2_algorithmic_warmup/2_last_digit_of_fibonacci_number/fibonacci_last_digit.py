def fibonacci_last_digit(n):
    if n <= 1:
        return n
    else:
        list = [0, 1 , 1]


        for i in range(2, n+1):
            list[2] = (list[0] + list[1]) % 10
            list[0] = list[1]
            list[1] = list[2]
        
        result = list[2]

        return result % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
