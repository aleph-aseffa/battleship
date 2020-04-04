import pygame


class Board:

    def __init__(self):
        width = 1200
        height = 600
        self.win = pygame.display.set_mode((width, height))
        self.draw_board()

    def draw_board(self):

        white = (255, 255, 255)
        black = (0, 0, 0)
        self.win.fill(white)
        pygame.display.set_caption("Battleship")

        # draw grids
        i = 0
        while i < 11:
            # player's grid
            pygame.draw.lines(self.win, black, False, [(0, (i*50)), (500, (i*50))], 1)
            pygame.draw.lines(self.win, black, False, [((i*50), 0), ((i*50), 500)], 1)

            # opponent's grid
            pygame.draw.lines(self.win, black, False, [(600, (i*50)), (1100, (i*50))], 1)
            pygame.draw.lines(self.win, black, False, [(600+(i*50), 0), (600+(i*50), 500)], 1)

            i += 1

        pygame.display.update()



