def fib_mod(n, m):
    numbers = []
    numbers.extend([0, 1])
    for i in range(2, n + 1):
        numbers.append((numbers[i - 1] + numbers[i - 2]) % m)
    return numbers[n]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()