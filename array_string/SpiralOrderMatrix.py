def spiral_to_linear_matrix(input_arr):
    linear_arr = []
    row = len(input_arr)
    col = len(input_arr[0])
    print(row)
    print(col)
    total_element = row * col
    cursor_left = 0
    cursor_right = col
    cursor_top = 0
    cursor_bottom = row
    while (cursor_top <= cursor_bottom) & (cursor_left <= cursor_right):
        for i in range(len(input_arr)):
            print("Left to Right!!")
            for j in range(cursor_left, cursor_right):
                print(input_arr[cursor_top][j])
                linear_arr.append(input_arr[cursor_top][j])
            cursor_top = cursor_top + 1
            print("Top to Bottom!!")
            for j in range(cursor_top, cursor_bottom):
                print(input_arr[j][cursor_right - 1])
                linear_arr.append(input_arr[j][cursor_right - 1])
            cursor_right = cursor_right - 1
            print("Right to Left!!")
            for j in range(cursor_right - 1, cursor_left - 1, -1):
                print(input_arr[cursor_bottom - 1][j])
                linear_arr.append(input_arr[cursor_bottom - 1][j])
            cursor_bottom = cursor_bottom - 1
            print("Bottom to Top!!")
            for j in range(cursor_bottom - 1, cursor_top - 1, -1):
                print(input_arr[j][cursor_left])
                linear_arr.append(input_arr[j][cursor_left])
            cursor_left = cursor_left + 1
    return linear_arr


input_2D_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
input_2D_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
input_2D_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
output_linear_arr = spiral_to_linear_matrix(input_2D_arr)
print(output_linear_arr)
