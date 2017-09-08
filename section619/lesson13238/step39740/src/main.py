
n, W = map(int, input().split())

if W == 0:
    print(0)
else:
    objects = []
    for i in range(int(n)):
        # 0 - price, 1 - weight

        a, b = map(float, input().split())
        objects.append([a,b])

    objects = sorted(objects, key = lambda obj : obj[0] / obj[1], reverse=True)

    summaryPrice = 0

    for obj in objects:
        weight_diff = W - obj[1]

        if weight_diff >= 0.0:
            summaryPrice += obj[0]
            W = weight_diff

        else:
            summaryPrice += obj[0] * ((W) / obj[1])
            W = 0

        if W <= 0.0:
            break

    print(summaryPrice)