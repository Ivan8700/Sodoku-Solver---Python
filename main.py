def update_row_column(row, column):
    #The function returns a list with 2 elements, [first, second]
    # first means "next column number" and second means "next row number" after given position (row,column).
    # i.e row = 1, column = 4 -> returned row = 1, column = 5
    list_returned = []
    if column == 8:
        list_returned.append(0)
        if row == 8:
            return None
        else:
            list_returned.append(row + 1)
    else:
        list_returned.append(column + 1)
        list_returned.append(row)
    return list_returned
def is_valid_to_insert(num, row, column,board):
    # check if it's valid to insert the number "num" to the position at (row, column) by checking row, column and "cube".
    # "cube" means - specific 9 indices which forms a box, i.e top-left 9 indices
    if num in board[row]:
        return False
    # check column
    for lists in board:
        if num == lists[column]:
            return False
    # check cube
    cube_column_number = int(column / 3)
    cube_row_number = int(row / 3)
    for row_num in range((3 * cube_row_number), (3 * cube_row_number) + 3):
        for col_num in range(3 * cube_column_number, (3 * cube_column_number) + 3):
            if (num == board[row_num][col_num]) and (row_num != row or col_num != column):
                return False
    return True
def print_Board(board):
    for row_num in range(9):
        print(board[row_num])

def solveSudoku(board):
    #runs the main algorithm to solve the sudoku.
    # input = board, list of lists, i.e -
    # [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."]    ##rows 0-2
    # ,["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"]    ##rows 3-5
    # ,[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]   ##rows 6-8
    # each list inside symbolize a "row", columns are the specific indices in the lists.
    list_of_tried_nums = [] # initialize list of "tried" numbers
    valid_solution = False # used to indicate when solution was found
    row_index = 0 #start pos
    column_index = 0
    may_insert = False #check if we can insert the num in specific position
    from_which_number_to_try = 1
    while valid_solution == False:
        if board[row_index][column_index] == ".": #if we can try to insert
            for num in range(from_which_number_to_try, 10): #try to search for a number that can be inserted
                may_insert = is_valid_to_insert(str(num), row_index, column_index, board)
                if may_insert == True: #if can be inserted, add the position and tried number to the "...tried_nums" list and update the next position
                    list_of_tried_nums.append((row_index, column_index, num))
                    board[row_index][column_index] = str(num)
                    update = update_row_column(row_index, column_index)
                    if update != None: #if there is a next position (not last row and last column) - update to the next
                        column_index = update[0]
                        row_index = update[1]
                        from_which_number_to_try = 1
                        break
                    else: #if no next position, then found solution
                        valid_solution = True
                        break
            # reached here means we failed to insert any number at the position - begin to backtrack
            reset = False
            while reset == False and may_insert == False:
                temp = list_of_tried_nums[-1][-1]
                if temp != 9:
                    from_which_number_to_try = (temp + 1) #if the last tried number is not 9, i.e 6, try to insert 7 in the same spot.
                    reset = True
                row_index = list_of_tried_nums[-1][0]
                column_index = list_of_tried_nums[-1][1]
                board[row_index][column_index] = "."
                list_of_tried_nums.pop(-1) #(whether last tried number is 9 just pop, if not 9 then try the next number but pop anyway
        else: #if the position contains a number inside
            update = update_row_column(row_index, column_index) #move to next pos
            if update != None:
                column_index = update[0]
                row_index = update[1]
            else:
                break
    print_Board(board)

#main
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#board = [[".",".","2",".",".","8",".",".","9"],["7",".",".",".",".",".",".",".","."],[".",".",".",".","4","3",".","6","."],["2",".","6",".",".",".",".",".","."],[".","4",".",".","1",".","7",".","."],[".",".",".","9","6",".",".",".","."],["9","1",".",".",".",".",".",".","7"],[".","8",".",".",".",".",".","5","."],["4",".",".",".","8",".","9",".","."]]
solveSudoku(board)