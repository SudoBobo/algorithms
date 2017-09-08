def optimal_actions_BU(n, intermediates):
    if n == 1:
        intermediates.append(1)
        return 0

    if n == 2:
        intermediates.extend([1,2])
        return 1

    if n == 3:
        intermediates.extend([1,3])
        return 1

    # n > 3

    big_number = 10000000
    D = [big_number for i in range(0, n+1)]
    # C[i] points to optimal previous elemet
    C = [0 for i in range(0, n+1)]

    D[1] = 0
    D[2] = 1
    D[3] = 1

    for i in range(4, n+1):
        # D[n // 3] if possible otherwise very big number
        n_3 = big_number
        # D[n // 2] if possible otherwise very big number
        n_2 = big_number
        # D[n - 1]
        n_1 = big_number

        if i % 3 == 0:
            n_3 = D[i//3]

        if i % 2 == 0:
            n_2 = D[i//2]

        if i - 1 > 0:
            n_1 = D[i - 1]
        else:
            n_1 = D[1]

        opt_prev_n = min(n_3, n_2, n_1)
        D[i] = opt_prev_n + 1

        if n_3 == opt_prev_n:
            C[i] = i // 3
        elif n_2 == opt_prev_n:
            C[i] = i // 2
        elif n_1 == opt_prev_n:
            C[i] = i - 1
        else:
            C[i] = 1

    j = n
    while j > 1:
        intermediates.append(j)
        j = C[j]

    intermediates.append(1)

    return D[n]

n = int(input())

intermediates = list()
k = optimal_actions_BU(n, intermediates)

print(k)
print(*reversed(intermediates))
