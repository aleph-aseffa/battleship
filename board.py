import pygame
import random
import storage


class Board:

    def __init__(self):
        """
        Initialize an instance of the Board class.
        """
        self.player_ship_locations = set()  # keeps track of where the player's ships are located.
        self.ai_ship_locations = set()  # keeps track of where the ai's ships are located.
        width = 1200  # resolution of game display window.
        height = 600  # resolution of game display window.
        self.win = pygame.display.set_mode((width, height))  # game display window instance.

        # collect user information
        # TODO: Fix check for -1
        self.info = storage.Storage(self.win)
        if self.info == -1:
            pygame.quit()
        else:
            # begin game
            self.draw_board()
            self.player_hit_ships = 0  # counter of how many of the player's ships have been hit.
            self.ai_hit_ships = 0  # counter of how many of the ai's ships have been hit.

    def draw_board(self):
        """
        Draw the game board on the display window.
        :return: None.
        """
        # RGB values of selected colors:
        white = (255, 255, 255)
        black = (0, 0, 0)
        blue = (0, 0, 255)

        self.win.fill(white)
        pygame.display.set_caption("Battleship")

        # headers of the game boards
        self.small_text("Your Board", 32, (315, 25), black)
        self.small_text("AI's Board", 32, (900, 25), black)

        # counter of how many ships each player has hit
        self.small_text("You have hit 0/20", 25, (280, 575), black)
        self.small_text("AI has hit: 0/20", 25, (880, 575), black)

        # draw grids
        i = 0
        while i < 11:
            # NOTE: +50 is the offset
            # player's grid
            pygame.draw.lines(self.win, black, False, [(0+50, (i*50+50)), (500+50, (i*50+50))], 1)
            pygame.draw.lines(self.win, black, False, [((i*50+50), 0+50), ((i*50+50), 500+50)], 1)

            # opponent's grid
            pygame.draw.lines(self.win, black, False, [(600+50, (i*50+50)), (1100+50, (i*50+50))], 1)
            pygame.draw.lines(self.win, black, False, [(600+50+(i*50), 0+50), (600+50+(i*50), 500+50)], 1)

            i += 1

        # randomly generate the ship locations
        self.create_ships()

        # draw the ships on the user's board
        for ship in self.player_ship_locations:
            pygame.draw.rect(self.win, blue, (ship[0]*50+50, ship[1]*50+50, 50, 50), 0)

        pygame.display.update()

    def create_ships(self):
        """
        Generates the battleships for the player and for the AI.
        :return: None.
        """
        # Generate two 4x1 ships
        self.ship_bounds(4, 0)
        self.ship_bounds(4, 1)

        # Generate four 3x1 ships
        self.ship_bounds(3, 0)
        self.ship_bounds(3, 1)
        self.ship_bounds(3, 0)
        self.ship_bounds(3, 1)

        # Generate six 2x1 ships
        self.ship_bounds(2, 0)
        self.ship_bounds(2, 1)
        self.ship_bounds(2, 0)
        self.ship_bounds(2, 1)
        self.ship_bounds(2, 0)
        self.ship_bounds(2, 1)

        # Generate eight 1x1 ships
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)
        self.ship_bounds(1, 0)
        self.ship_bounds(1, 1)

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

            # check if the current starting location for the ship is not already occupied
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

    def user_hit(self, x, y, p):  # only called when the user clicks, not the ai
        """
        Registers the user's click.
        :param x: int, x-coordinate (top-left)
        :param y: int, y-coordinate (top-left)
        :param p: Player object
        :return: bool: whether or not the player has hit a ship
        """
        red = (255, 0, 0)
        green = (0, 255, 0)

        # check if user has already clicked on this box
        if (x-13, y-1) in p.tried_positions:  # subtractions are to get rid of the offsets
            return False
        else:
            p.tried_positions.add((x-13, y-1))

        if 0 <= x-13 < 10 and 0 <= y-1 < 10:
            # check if the box contains a ship and update display accordingly
            if (x-13, y-1) in self.ai_ship_locations:
                self.ai_hit_ships += 1
                self.small_text("You have hit: " + str(self.ai_hit_ships) + "/20", 25, (280, 575), (0, 0, 0))
                pygame.draw.rect(self.win, green, (x * 50, y * 50, 50, 50), 0)
            else:
                pygame.draw.rect(self.win, red, (x * 50, y * 50, 50, 50), 0)
            pygame.display.update()
            return True
        else:
            return False

    def register_ai_hit(self, coord):
        """
        Registers the AI's click.
        :param coord: int, the coordinates of the box the AI hit.
        :return: bool, whether or not the AI hit a player's ship.
        """
        ship_hit = False
        red = (255, 0, 0)
        green = (0, 255, 0)

        if coord in self.player_ship_locations:
            pygame.draw.rect(self.win, green, (coord[0] * 50+50, coord[1] * 50+50, 50, 50), 0)
            self.player_hit_ships += 1
            self.small_text("AI has hit: " + str(self.player_hit_ships) + "/20", 25,(880, 575), (0, 0, 0))
            ship_hit = True
        else:
            pygame.draw.rect(self.win, red, (coord[0] * 50+50, coord[1] * 50+50, 50, 50), 0)
        pygame.display.update()

        return ship_hit

    def fullscreen_message(self, message):
        """
        Overwrites the screen with the given message
        :param message: str, the message to display
        :return: None
        """
        pygame.font.init()
        green = (0, 255, 0)
        white = (255, 255, 255)

        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render(message, True, green)
        text_rect = text.get_rect()
        text_rect.center = (1200 / 2, 600 / 2)

        self.win.fill(white)
        self.win.blit(text, text_rect)

        pygame.display.update()

    def small_text(self, message, font_size, coords, color):
        """
        Overwrites the previously displayed text and then writes the given message to
            the screen at the specified coordinates.
        :param message: str, the message to display
        :param font_size: int, the font size of the message
        :param coords: tuple (int, int), the coordinates at which to display the text
        :param color: tuple (int, int, int), the RGB values of the desired color
        :return: None
        """
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', font_size)

        # pygame.draw.rect(self.win, (255, 255, 255), (coords[0], coords[1], 300, 300))
        self.win.fill((255, 255, 255), (coords[0]-200, coords[1]-23, 500, 500))

        # write the new text
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = coords

        self.win.blit(text, text_rect)
