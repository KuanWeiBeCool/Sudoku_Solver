# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Function to visualize the chart
def print_chart(chart):
    print("-------------------------")
    i = 0
    while i <= 8:
        print("|", end=" ")
        list_num = chart[i]
        j = 0

        while j <= 8:
            if j == 2 or j == 5:
                print(str(list_num[j]) + " |", end=" ")
            elif j == 8:
                print(str(list_num[j]) + " |")
            else:
                print(list_num[j], end=" ")
            j += 1

        if (i+1) % 3 == 0:
            print("-------------------------")
        i += 1

# Function to find the next blank slot
# return None if there is no blank slot
def find_blank(chart):
    for y in range(0, 9):
        for x in range(0, 9):
            if chart[y][x] == 0:
                return (y, x)
    # If not found, return None
    return None

# function to check if the given position chart[y][x] is valid
# return True if it is, and False otherwise
def check(chart, y, x, num):
    # Check horizontal, if there is any number that is the same
    for i in range(0, 9):
        if chart[y][i] == num and i != x:
            return False
    # Check vertical, if there is any number that is the same
    for j in range(0, 9):
        if chart[j][x] == num and j != y:
            return False

    # Check the box, if there is any number that is the same
    y_box = y // 3  # y -> 0, 1, 2 -> y_box = 0; y -> 3, 4, 5 -> y_box = 1; y -> 6, 7, 8 -> y_box = 2
    x_box = x // 3  # x -> 0, 1, 2 -> x_box = 0; x -> 3, 4, 5 -> x_box = 1; x -> 6, 7, 8 -> x_box = 2

    box_start_index_y = y_box * 3
    box_end_index_y = box_start_index_y + 3

    box_start_index_x = x_box * 3
    box_end_index_x = box_start_index_x + 3
    for i in range(box_start_index_y, box_end_index_y):
        for j in range(box_start_index_x, box_end_index_x):
            if chart[i][j] == num and i != x and j != y:
                return False

    # If none of the above case satisfied, the number can be a solution
    return True

# function to solve the puzzle
def solve(chart):
    next_blank = find_blank(chart)

    # No blank slot. Puzzle solved
    if next_blank == None:
        return True
    (y, x) = next_blank
    # Try every possible solutions from 1 to 9
    for num in range(1, 10):
        if check(chart, y, x, num):
            chart[y][x] = num
            if solve(chart):
                return True
            # If the next step cannot find the correct solution, set the current slot to 0
            # and try to find the correct solution again.
            chart[y][x] = 0
    return False
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # A 9x9 Sudoku chart.
    # 0: empty place to solve
    chart = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
             [6, 8, 0, 0, 7, 0, 0, 9, 0],
             [1, 9, 0, 0, 0, 4, 5, 0, 0],
             [8, 2, 0, 1, 0, 0, 0, 4, 0],
             [0, 0, 4, 6, 0, 2, 9, 0, 0],
             [0, 5, 0, 0, 0, 3, 0, 2, 8],
             [0, 0, 9, 3, 0, 0, 0, 7, 4],
             [0, 4, 0, 0, 5, 0, 0, 3, 6],
             [7, 0, 3, 0, 1, 8, 0, 0, 0]]
    print_chart(chart)
    solve(chart)
    print_chart(chart)





