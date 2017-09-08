from array import array


def count_sort(arr, n):
    # return new array
    parameter = 10
    count_arr = array('I', [0 for i in range(parameter)])

    for elem in arr:
        # Example: store counter for '3' in count_arr[2]
        count_arr[elem - 1] += 1

    for i in range(1, parameter):
        count_arr[i] = count_arr[i] + count_arr[i - 1]

    res_arr = array('I', [0 for i in range(n)])
    for j in range(n - 1, -1, -1):
        res_arr[count_arr[arr[j] - 1] - 1] = arr[j]
        count_arr[arr[j] - 1] -= 1

    return res_arr


n = int(input())
numbers = map(int, input().split(' '))
# numbers = [2, 3, 9, 2, 9]

arr = array('I', numbers)

print(*count_sort(arr, n))