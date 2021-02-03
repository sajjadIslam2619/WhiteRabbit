def max_distance(input_arr):
    max_distance = -1
    for i in range(0, len(input_arr)):
        for j in range(0, len(input_arr) - (i)):
            if (j != i) and (input_arr[i] <= input_arr[j]):
                distance = j - i
                if distance > max_distance:
                    max_distance = distance
    return max_distance


def max_distance_improved(input_arr):
    list_index = []
    for i in range(0, len(input_arr)):
        list_index.append([input_arr[i], i])
    list_index.sort()
    max_distance = -1
    large_index = list_index[0][1]
    for i in range(1, len(list_index)):
        if large_index > list_index[i][1]:
            large_index = list_index[i][1]
        else:
            distance = list_index[i][1] - large_index
            if distance > max_distance:
                max_distance = distance
    return max_distance


input_arr = [3, 5, 4, 2]
input_arr = [6, 5, 4, 3, 2, 1]
input_arr = [1, 2, 3, 4, 5, 6]
input_arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
input_arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
distance = max_distance_improved(input_arr)
print("--")
print(distance)
distance = max_distance(input_arr)
print(distance)
