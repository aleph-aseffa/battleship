import pygame
import random


class Board:

    def __init__(self):
        self.player_ship_locations = set()
        self.ai_ship_locations = set()
        width = 1200
        height = 600
        self.win = pygame.display.set_mode((width, height))
        self.draw_board()

    def draw_board(self):

        white = (255, 255, 255)
        black = (0, 0, 0)
        blue = (0, 0, 255)
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

        # randomly generate the ship locations
        self.create_ships()

        # draw the ships on the user's board
        for ship in self.player_ship_locations:
            pygame.draw.rect(self.win, blue, (ship[0]*50, ship[1]*50, 50, 50), 0)

        pygame.display.update()

    def create_ships(self):

        self.ship_bounds(4, 0)
        self.ship_bounds(4, 1)

        self.ship_bounds(3, 0)
        self.ship_bounds(3, 1)
        self.ship_bounds(3, 0)
        self.ship_bounds(3, 1)

        self.ship_bounds(2, 0)
        self.ship_bounds(2, 1)
        self.ship_bounds(2, 0)
        self.ship_bounds(2, 1)
        self.ship_bounds(2, 0)
        self.ship_bounds(2, 1)

        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)

        print(self.player_ship_locations)

        return None

    def ship_bounds(self, size, val):
        """
        :param size:
        :param val: 0 = player, 1 = AI
        :return:
        """
        random.seed()
        valid = False

        while not valid:  # continue to search for locations for the ship until a valid one is found
            direction = random.randint(0, 3)  # 0 = left, 1 = right, 2 = up, 3 = down

            # designates left-bound x-coordinate of the first block of the ship
            begin = (random.randint(0, 9), random.randint(0, 9))
            b_x = begin[0]  # x-coord
            b_y = begin[1]  # y-coord

            if val == 0:
                proceed = begin not in self.player_ship_locations
            else:
                proceed = begin not in self.ai_ship_locations

            if proceed:  # if the location is not occupied by a ship already

                if direction == 0:
                    if b_x - (size-1) >= 0:
                        end = (b_x - (size-1), b_y)
                        i = 0
                        curr = end[0]
                        while i < size:
                            if val == 0:
                                self.player_ship_locations.add((curr, b_y))
                            else:
                                self.ai_ship_locations.add((curr, b_y))
                            curr += 1
                            i += 1
                        return begin, end

                elif direction == 1:
                    if b_x + (size-1) <= 9:
                        end = (b_x + (size-1), b_y)
                        i = 0
                        curr = end[0]
                        while i < size:
                            if val == 0:
                                self.player_ship_locations.add((curr, b_y))
                            else:
                                self.ai_ship_locations.add((curr, b_y))
                            curr -= 1
                            i += 1
                        return begin, end

                elif direction == 2:
                    if b_y + (size-1) <= 9:
                        end = (b_x, b_y + (size-1))
                        i = 0
                        curr = end[1]
                        while i < size:
                            if val == 0:
                                self.player_ship_locations.add((b_x, curr))
                            else:
                                self.ai_ship_locations.add((b_x, curr))
                            curr -= 1
                            i += 1
                        return begin, end

                else:
                    if b_y - (size-1) >= 0:
                        end = (b_x, b_y - (size-1))
                        i = 0
                        curr = end[1]
                        while i < size:
                            if val == 0:
                                self.player_ship_locations.add((b_x, curr))
                            else:
                                self.ai_ship_locations.add((b_x, curr))
                            curr += 1
                            i += 1
                        return begin, end
            else:
                valid = False

    def draw_x_sign(self, x, y):
        """
        :param x: x-coordinate (top-left)
        :param y: y-coordinate (top-left)
        :return:
        """
        # TODO: complete function.
