import pygame
#from sys import exit


class Cell:
    SKETCH_POS = {'1':(10,10), '2':(30,10), '3':(50,10),
                  '4':(10,30), '5':(30,30), '6':(50,30),
                  '7':(10,50), '8':(30,50), '9':(50,50)}

    def __init__(self, value, row, col, screen, locked=False):
        self.value = value
        self.s_value = []
        self.pos = (row, col)
        self.screen = screen
        self.locked = locked

    def set_cell_value(self, value):
        self.value = value
        self.s_value = []

    def set_sketched_value(self, value):
        if value in self.s_value:
            self._remove_sketched_value(value)
        elif 0 < value < 10:  # Prevents duplicate values and ensures they're proper
            self.s_value.append(value)

    def _remove_sketched_value(self, value):
        while value in self.s_value:
            self.s_value.remove(value)

    def clear_sketched_values(self):
        self.s_value.clear()

    def is_locked(self):
        return self.locked

    def draw(self):
        # Sets up the cell surface and fills it with white
        pygame.font.init()
        cell_surface = pygame.Surface((60, 60))
        cell_surface.fill('WHITE')

        # If there is a solved value, it is drawn onto the center of the board
        if self.value != 0:
            font = pygame.font.Font(size=30)
            cell_surface.fill('WHITE')
            text = font.render(str(self.value), True, 'BLACK')
            text_rect = text.get_rect(center=(30, 30))
            cell_surface.blit(text, text_rect)

        # If there are sketched values, they are placed based on their value
        elif len(self.s_value) != 0:
            font = pygame.font.Font(size=20)
            for nums in self.s_value:
                text = font.render(str(nums), True, 'GREY')
                text_rect = text.get_rect(center=Cell.SKETCH_POS[str(nums)])
                cell_surface.blit(text, text_rect)

        # Otherwise, a blank cell is blit onto the screen based on its row and column position
        pygame.draw.lines(cell_surface, 'GREY', True, [(0, 0), (59, 0), (59, 59), (0, 59)], width=1)
        self.screen.blit(cell_surface, (0 + 60 * (self.pos[1]), 0 + 60 * (self.pos[0])))

# This was used to test the class. It has no other purpose
'''
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((540, 540))
    screen.fill('WHITE')
    clock = pygame.time.Clock()

    cell = Cell(0, 2, 2, screen)
    cell.set_sketched_value(1)
    cell.set_sketched_value(2)
    cell.set_sketched_value(3)

    cell2 = Cell(1, 2, 1, screen)
    cont = True

    while cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        cell.draw()
        cell2.draw()
        pygame.display.flip()
        clock.tick(60)
'''