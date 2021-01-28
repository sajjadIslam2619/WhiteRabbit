# time complexity = n*n
def max_suvarray(input_arr):
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


input_arr = [-1, -2, 1, 2, 3, -5, 4]
max_sum = max_suvarray(input_arr)
print(max_sum)
