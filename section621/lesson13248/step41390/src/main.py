
def inversies(n, arr):
    if n < 2:
        return 0

    inv_count = [0]

    while len(arr) > 1:
        for i in range(0, len(arr), 1):
            if (i + 1) < len(arr):
                arr.insert(i, merge(arr.pop(i), arr.pop(i), inv_count))
    return inv_count[0]


def merge(arr_1, arr_2, inv_count):
    idx_1 = 0
    idx_2 = 0

    result = list()
    while idx_1 < len(arr_1) or idx_2 < len(arr_2):

        if idx_1 != len(arr_1) and (idx_2 == len(arr_2) or arr_1[idx_1] <= arr_2[idx_2]):
            result.append(arr_1[idx_1])
            idx_1 += 1
        else:
            result.append(arr_2[idx_2])
            idx_2 += 1

            inv_count[0] += len(arr_1) - idx_1

    return result


n = int(input())
# n = 5
line = input().split(' ')
# line = ['2', '3', '9', '2', '9']
arr = list([[int(number)] for number in line])

print(inversies(n, arr))
