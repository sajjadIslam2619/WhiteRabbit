# list of tuples
tuple_list = [(4, 6), (3, 5)]
# list of list
list_list = [[4, 6], [3, 5]]
#Negative numbers mean that you count from the right instead of the left.
# So, list[-1] refers to the last element, list[-2] is the second-last, and so on.

def merge_overlap_interval(input_list):
    input_list.sort()
    print(input_list)
    output_list = []
    output_list.append(input_list[0])
    for i in range(1, len(input_list)):
        start, end = output_list [-1]
        if end < input_list[i][0] :
            output_list.append(input_list[i])
        elif end < input_list[i][1] :
            end = input_list[i][1]
            output_list[-1] = [start, end]
    return output_list


input_list = [[1, 3], [2, 4], [5, 7], [6, 8]]
input_list = [[6, 8], [1, 9], [2, 4], [4, 7]]
input_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
output_list = merge_overlap_interval(input_list)
print(output_list)