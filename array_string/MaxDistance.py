def max_distance(input_arr):
    max_distance = -1
    for i in range(0, len(input_arr)):
        for j in range(0, len(input_arr) - (i)):
            if input_arr[i] <= input_arr[j]:
                distance = j - i
                if distance > max_distance:
                    max_distance = distance
    return max_distance


input_arr = [3, 5, 4, 2]
input_arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
input_arr = [6, 5, 4, 3, 2, 1]
input_arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
input_arr = [1, 2, 3, 4, 5, 6]
distance = max_distance(input_arr)
print(distance)
