import numpy as np

def max_summary_weight(W, N, weights):
    D = np.array([[-1 for w in range(W + 1)] for n in range(N+1)])

    for w in range(W + 1):
        D[0, w] = 0

    for n in range(N + 1):
        D[n, 0] = 0

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            D[n, w] = D[n - 1, w]

            if weights[n - 1] <= w:
                D[n, w] = max(D[n, w], D[n - 1, w - weights[n - 1]] + weights[n - 1])

    return D[N, W]


W, N = map(int, input().split(' '))
weights = [int(weight) for weight in input().split(' ')]


# W, N = 10, 3
# weights = [1, 4, 8]

print(max_summary_weight(W, N, weights))