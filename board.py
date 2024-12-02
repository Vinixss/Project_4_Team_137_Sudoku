from cell import Cell
import pygame


class Board:

    def __init__(self, width, height, screen, difficulty): #intialize the board class with variables
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, self.screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None
        self.start_board = [[],[],[],[],[],[],[],[],[]]
        self.solved_board = [[],[],[],[],[],[],[],[],[]]

    def draw(self): #creates the outline, sets color to white
        self.screen.fill((255, 255, 255))
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (self.width/9 * i, 0), (self.width/9*i, self.height), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, self.height / 9 * i), (self.width, self.height/9 * i), thickness)

    def select(self, row, col): #allows cell to be selected so user can input value
        if self.selected_cell:
            self.selected_cell = None
        # print(row, col)
        self.selected_cell = self.cells[row][col]
        # self.selected_cell.select()

    def click(self, x, y): #returns coordinates of the selected cell
        if x < 0 or x > self.width or y < 0 or y > self.height:
            return None
        row = int(y // (self.height / 9))
        col = int(x // (self.width / 9)) # I don't know why, but these were returning floats. - Kaiden
        return row, col

    def clear(self): #erases value input onto cell
        if self.selected_cell and not self.selected_cell.is_locked():
            self.selected_cell.clear()

    def sketch(self, value): #sketched value set to a selected cell
        if self.selected_cell is not None and not self.selected_cell.is_locked():
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value): #sets the selected cell's value to the inputted value
        if self.selected_cell is not None and not self.selected_cell.is_locked():
            # print('Placing number')
            self.selected_cell.set_cell_value(value)
            #self.selected_cell.unselect()
            self.selected_cell = None

    def reset_to_original(self): #resets every cell to original value
        for i in range(9):
            for j in range(9):
                if not self.cells[i][j].is_locked():
                    self.cells[i][j].set_cell_value(self.start_board[i][j])

    def is_full(self): #determins whether board is filled out completely
        for i in range(9):
            for j in range(9):
                if self.solved_board[i][j] == 0:
                    return False
        return True

    def update_board(self): #updates board to diplay values user inputs
        for i in range(9):
            for j in range(9):
                self.solved_board[i][j] = self.cells[i][j].value

    def find_empty(self): #displays coordinates of empty cells
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return i, j
        return None

    def set_solved_board(self):
        for i in range(9):
            for j in range(9):
                self.solved_board[i].append(self.cells[i][j].value)
                self.start_board[i].append(self.cells[i][j].value) # This was the only way to get it to stop pointing to solved_board - Kaiden

    def check_board(self): #determine whether puzzle was correctly solved
        for i in range(9):
            row_nums = set()
            col_nums = set()
            box_nums = set()
            for j in range(9):
                row_val = self.cells[i][j].value
                col_val = self.cells[j][i].value
                box_val = self.cells[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3]

                if row_val != 0:
                    if row_val in row_nums:
                        return False
                    else:
                        row_nums.add(row_val)

                if col_val != 0:
                    if col_val in col_nums:
                        return False
                    else:
                        col_nums.add(col_val)

                if box_val != 0:
                    if box_val in box_nums:
                        return False
                    else:
                        box_nums.add(box_val)

        return True