from Sandbox.timed import compare, timed


def gcd_3(a, b):
    if a == 0 and b == 0:
        return max(a,b)

    return gcd_3(b % a, a)


def gcd_1(a, b):
    while True:
        if a == 0 or b == 0:
            return max(a,b)

        if a >= b:
            a = a % b
        else:
            b = b % a


def gcd_2(a, b):

    a, b = max(a,b), min(a,b)
    while True:
        if a == 0 or b == 0:
            return max(a, b)
        a, b = b, a % b

def main():
    # a, b = map(int, input().split())
    # print(gcd(a,b))

    a, b = 14159572, 63967072
    answer = 4

    print(gcd_1(a, b) == 4)
    print(gcd_2(a, b) == 4)
    # print(gcd_3(a, b) == 4)

    print(timed(gcd_2, a, b))
    print(timed(gcd_1, a, b))
    # print(timed(gcd_3, a, b))



if __name__ == "__main__":
    main()