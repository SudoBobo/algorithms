def max_sum_BU(n, a):

    if n == 1:
        return a[0]

    D = [-1 for i in range(n)]
    D[0] = a[0]
    D[1] = max(D[0], 0) + a[1]

    if n > 2:
        for i in range(2, n):
            D[i] = max(D[i - 1], D[i - 2]) + a[i]

    return D[n - 1]


n = int(input())
a = [int(number) for number in input().split(' ')]

print(max_sum_BU(n, a))