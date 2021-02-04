def max_unsorted_subarray(input_array):
    lowest_index = len(input_array)
    highest_index = -1
    sorted_array = input_array.copy()
    sorted_array.sort()
    print(input_array)
    print(sorted_array)
    for i in range(0, len(input_array)):
        if input_array[i] != sorted_array[i]:
            if lowest_index > i :
                lowest_index = i
            if highest_index < i :
                highest_index = i

    if lowest_index == len(input_array) and highest_index == -1 : return [-1]
    index_array = []
    index_array.append(lowest_index)
    index_array.append(highest_index)
    return index_array

input_array = [1, 3, 2, 4, 5]
input_array = [1, 4, 2, 3, 5]
input_array = [3, 2, 1]
input_array = [1, 2, 3, 4, 5]
input_array = [5, 6, 1, 2, 4, 7]
index_array = max_unsorted_subarray(input_array)
print(index_array)
