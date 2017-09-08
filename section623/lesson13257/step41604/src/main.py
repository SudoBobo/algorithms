from array import array


def LS(arr, n):
    D = array('I', [0 for i in range(n)])

    for k in range(n):
        D[k] = 1

        for j in range(k - 1, -1, -1):

            if arr[k] % arr[j] == 0 and D[j] + 1 > D[k]:
                D[k] = D[j] + 1

    return max(D)


n = int(input())
numbers = map(int, input().split(' '))
arr = array('I', numbers)

print(LS(arr, n))