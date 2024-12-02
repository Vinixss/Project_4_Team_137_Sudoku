from sudoku_generator import SudokuGenerator, generate_sudoku
import pygame, sys
from board import Board
from cell import Cell
def draw_game_start(screen):# creates the start menu screen
    LINE_COLOR = (245, 152, 66)

    start_title_font = pygame.font.Font(None, 45)
    select_title_font = pygame.font.Font(None, 45)
    button_font = pygame.font.Font(None, 30)

    screen.fill((255,255,255))

    title_surface = start_title_font.render('Sudoku Program', 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center = (270, 150))
    screen.blit(title_surface, title_rectangle)

    select_surface = select_title_font.render('Please select difficulty', 0, LINE_COLOR)
    select_rectangle = select_surface.get_rect(center = (270,300))
    screen.blit(select_surface, select_rectangle)

    easy_text = button_font.render('easy', 0, (255,255,255))
    medium_text = button_font.render('medium', 0, (255,255,255))
    hard_text = button_font.render('hard', 0 ,(255,255,255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(center = (90, 600))
    medium_rectangle = medium_surface.get_rect(center=(260, 600))
    hard_rectangle = hard_surface.get_rect(center = (430, 600))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(medium_surface, medium_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                else:
                    continue
                return difficulty
        pygame.display.update()

def draw_game_lose(screen):# creates the game lose screen
    LINE_COLOR = (245, 152, 66)
    title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 50)

    screen.fill((255,255,255))

    title_surface = title_font.render('Game Over', 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center = (270, 150))
    screen.blit(title_surface, title_rectangle)

    restart_text = button_font.render('restart', 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10,10))
    restart_rectangle = restart_surface.get_rect(center = (270,400))
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()
        pygame.display.update()
def draw_game_win(screen):# creates the game won screen
    LINE_COLOR = (245, 152, 66)
    title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 50)

    screen.fill((255, 255, 255))

    title_surface = title_font.render('Game Won', 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(270, 150))
    screen.blit(title_surface, title_rectangle)

    quit_text = button_font.render('quit', 0, (255, 255, 255))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))
    quit_rectangle = quit_surface.get_rect(center=(270, 400))
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

def display_button(screen):

    button_font = pygame.font.Font(None, 30)
    reset_text = button_font.render('reset', 0, (255, 255, 255))
    restart_text = button_font.render('restart', 0, (255, 255, 255))
    exit_text = button_font.render('exit', 0, (255, 255, 255))
    LINE_COLOR = (245, 152, 66)

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(90, 600))
    restart_rectangle = restart_surface.get_rect(center=(260, 600))
    exit_rectangle = exit_surface.get_rect(center=(430, 600))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 800))
    difficulty_selected = draw_game_start(screen)
    sudoku = generate_sudoku(9, difficulty_selected) # Seems to generate duplicate values
    for i in range(0,9):
        for j in range(0,9):
            cell_value = sudoku[i][j]
            if cell_value != 0:
                cell = Cell(cell_value, i, j, screen, True)
            else:
                cell = Cell(cell_value, i, j, screen)
            sudoku[i][j] = cell
    board = Board(540,540, screen, difficulty_selected)
    board.cells = sudoku
    board.set_solved_board()
    board.draw()

    button_font = pygame.font.Font(None, 30)
    reset_text = button_font.render('reset', 0, (255, 255, 255))
    restart_text = button_font.render('restart', 0, (255, 255, 255))
    exit_text = button_font.render('exit', 0, (255, 255, 255))
    LINE_COLOR = (245, 152, 66)

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(90, 600))
    restart_rectangle = restart_surface.get_rect(center=(260, 600))
    exit_rectangle = exit_surface.get_rect(center=(430, 600))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if board.click(pos[0], pos[1]) != None:
                    x, y = board.click(pos[0], pos[1])
                    # print(x, y)
                    board.select(x, y)
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
                elif reset_rectangle.collidepoint(event.pos):
                    board.reset_to_original()
                elif restart_rectangle.collidepoint(event.pos):
                    main()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # each one detects number input
                    num = 1
                if event.key == pygame.K_2:
                    num = 2
                if event.key == pygame.K_3:
                    num = 3
                if event.key == pygame.K_4:
                    num = 4
                if event.key == pygame.K_5:
                    num = 5
                if event.key == pygame.K_6:
                    num = 6
                if event.key == pygame.K_7:
                    num = 7
                if event.key == pygame.K_8:
                    num = 8
                if event.key == pygame.K_9:
                    num = 9
                board.sketch(num)
                if event.key == pygame.K_RETURN:
                    # print('Adding Number')
                    board.place_number(num)
                    board.update_board()
            board.draw()
            display_button(screen)
        pygame.display.update()

        if board.is_full() == True:
            if board.check_board() == True:
                draw_game_win(screen)
            elif board.check_board() == False:
                draw_game_lose(screen)


        pygame.display.update()


if __name__ == '__main__':
    main()