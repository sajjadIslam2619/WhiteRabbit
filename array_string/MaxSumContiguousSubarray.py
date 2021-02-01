# time complexity = n*n
def max_subarray(input_arr):
    max_sum = input_arr[0]
    sum = input_arr[0]
    for i in range(0, len(input_arr)):
        if max_sum < input_arr[i]:
            max_sum = input_arr[i]
        for j in range(i + 1, len(input_arr) - (i + 1)):
            sum = sum + input_arr[j]
            if max_sum < sum:
                max_sum = sum
    return max_sum

# time complexity = n
def max_subarray_improved(input_arr):
    max_sum = -9999
    sum = 0
    for i in range(0, len(input_arr)):
        sum = sum + input_arr[i]
        if max_sum < sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum

input_arr = [-1, -2, 1, 2, 3, -5, 4]
input_arr = [-1, -2, 1, 2, 3, -5, 4, 5]
input_arr = [-1, -2, -11]
input_arr = [-11, -1, -12]
input_arr = [-11, -1, -2 , -1]
input_arr = [-11, -2, 0]
input_arr = [1, 2, 1]
input_arr = [0, 0, 0]
input_arr = [-1, -2, 1, 2, 3, -8, 4, 5]
max_sum = max_subarray_improved(input_arr)
print(max_sum)