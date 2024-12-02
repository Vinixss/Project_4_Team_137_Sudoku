import math
import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells): #initiliazes the parameters of the board
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self): #returns the board
        return self.board

    def print_board(self): #prints the values in the board, only used for debugging
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num): #checks to see if a specified number is already used in a row
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_col(self, col, num): #checks to see if a specified number is already used in a column
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num): #checks to see if a specified number is already used in a box
        if 0 <= row_start <= 2:
            row = 0
        elif 3 <= row_start <= 5:
            row = 3
        elif 6 <= row_start <= 9:
            row = 6
        if 0 <= col_start <= 2:
            col = 0
        elif 3 <= col_start <= 5:
            col = 3
        elif 6 <= col_start <= 9:
            col = 6

        for i in range(row, row + self.box_length): #confirms that there are no duplicate numbers
            for j in range(col, col + self.box_length):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num): #checks to see if a specified number used in the entire board
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)

    def unused_in_box(self, row_start, col_start): #finds all the unused numbers after board is generated
        used_nums = []
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                num = self.board[row][col]
                if num != 0:
                    used_nums.append(num)
        unused_nums = []
        for i in range(1, 10): #creates a list with all the unused numbers
            if i not in used_nums:
                unused_nums.append(i)
        return unused_nums

    def fill_box(self, row_start, col_start): #takes the unused numbers found above and inserts them into the board
        nums = self.unused_in_box(row_start, col_start)
        random.shuffle(nums)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = nums.pop()

    def fill_diagonal(self): #fills the diagonal sections of the board, starting at 0, 3, and 6
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col): #fills the remaining cells after the diagonals are full
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self): #fills the board, first the diagonal cells and then the left over cells
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


    def remove_cells(self): #removes sells based on the specified integer number
        cells_to_remove = self.removed_cells
        while cells_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1

def generate_sudoku(size, removed): #creates the board with all functions defined above
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

# board = generate_sudoku(9,20)
# print(board)

