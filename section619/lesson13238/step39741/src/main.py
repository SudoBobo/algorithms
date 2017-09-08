import math

n = int(input())
k = (math.floor((math.sqrt(1 + 8 * n) - 1) / 2))
print(k)
current_number = 1

for i in range(k):
    if i == k - 1:
        numbers.append(n)
    else:
        n -= current_number
        numbers.append(i)


print(*numbers)