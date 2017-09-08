from timer import Timer

def fib_digit(n):
    numbers = []
    numbers.extend([0, 1])
    for i in range(2,n+1):
        numbers.append((numbers[i-1] + numbers[i-2]) % 10)
    return numbers[n]



def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

