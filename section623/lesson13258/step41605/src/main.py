import numpy as np

def editing_distance(first_word, second_word):

    f = np.array(list(first_word))
    s = np.array(list(second_word))

    n = range(len(f) + 1)
    m = range(len(s) + 1)

    D = np.array([[1000000 for i in n] for j in m])

    for i in m:
        D[i, 0] = i

    for j in n:
        D[0, j] = j

    for i in range(1, len(s) + 1):
        for j in range(1, len(f) + 1):
            D[i, j] = min([
                D[i-1, j] + 1,
                D[i, j-1] + 1,
                D[i-1, j-1] + diff(f[j - 1], s[i - 1])])

    return D[len(s), len(f)]


def diff(first_symbol, second_symbol):
    if first_symbol == second_symbol:
        return 0
    else:
        return 1

first_word = input()
second_word = input()

print(editing_distance(first_word, second_word))