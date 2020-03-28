import pygame


class Board:

    class Box:
        def __init__(self, x, y, ship, hit_status):
            self.x = x
            self.y = y
            self.ship = ship
            self.hit_status = hit_status

        def get_location(self):
            return self.x, self.y

        def get_ship(self):
            return self.ship

        def get_hit_status(self):
            return self.hit_status

    def __init__(self):
        width = 500
        height = 500
        self.win = pygame.display.set_mode((width, height))
        self.draw_board()

    def draw_board(self):

        white = (255, 255, 255)

        self.win.fill(white)

        pygame.display.set_caption("Client")

        black = (0, 0, 0)

        pygame.draw.lines(self.win, black, False, [(0, 0), (500, 0)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 50), (500, 50)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 100), (500, 100)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 150), (500, 150)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 200), (500, 200)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 250), (500, 250)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 300), (500, 300)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 350), (500, 350)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 400), (500, 400)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 450), (500, 450)], 1)
        pygame.draw.lines(self.win, black, False, [(0, 498), (500, 498)], 1)

        pygame.draw.lines(self.win, black, False, [(1, 0), (1, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(50, 0), (50, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(100, 0), (100, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(150, 0), (150, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(200, 0), (200, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(250, 0), (250, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(300, 0), (300, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(350, 0), (350, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(400, 0), (400, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(450, 0), (450, 500)], 1)
        pygame.draw.lines(self.win, black, False, [(498, 0), (498, 500)], 1)

        pygame.display.update()





