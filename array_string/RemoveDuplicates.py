def remove_dupliates_from_array(input_arr):
    print("Remove Duplicates Function!! ")

    if len(input_arr) == 0: return 0
    cursor = 1
    for i in range(1, len(input_arr)):
        if input_arr[i] != input_arr[i - 1]:
            cursor = cursor + 1
    return cursor


arr = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 8, 9]
arr = [1, 1, 1]
arr = [1, 2, 3]
arr = [0]
arr = []
arr = [-8, -8, 0, 0, 1, 1, 7, 8, 9, 9]
uniqueNum = remove_dupliates_from_array(arr)
print(uniqueNum)
