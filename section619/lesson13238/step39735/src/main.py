
def my_sort(segments : list):
    res = list(segments)
    print(*res)
    res = sorted(res, key = lambda item : item[0])
    print(*res)
    # res = sorted(res, key = lambda item : item[1] - item[0])
    res = sorted(res, key = lambda item : item[1])
    print(*res)

    return res

def get_optimal_points(sorted_segments : list):

    rights = []
    rights.append(-1)

    for segment in sorted_segments:

        is_found = False

        for right in rights:
            if segment[0] <= right <= segment[1]:
                is_found = True
                break
        if not is_found:
            rights.append(segment[1])


    return list(set(rights[1:]))

def main():

    # n = int(input())
    # segments = []
    # for i in range(n):
    #     s = []
    #     s.extend(map(int, input().split()))
    #     segments.append(s)


    # s = [[4,7], [1,3], [2,5], [5,6]]
    # s1 = [[1,3], [2,5], [3,6]]
    segments = [[0,1], [0,3], [2,5], [4,7], [5,6]]

    sorted_segments = my_sort(segments)
    # print(*sorted_segments)
    optimal_points = get_optimal_points(sorted_segments)

    print(len(optimal_points))
    print(*sorted(optimal_points))


if __name__ == "__main__":
    main()