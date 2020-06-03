import pygame
import sqlite3


class Storage:

    def __init__(self, screen):
        """
        Initialize the Storage class.
        :param screen:
        """
        self.screen = screen
        """
        TODO: add database connection
        """
        self.username = ""
        self.collect_user_info()

    def collect_user_info(self):
        """
        Collect username from player.
        Code adapted from: https://www.reddit.com/r/pygame/comments/205i05/get_user_input/cg06jft/
        :return: -1 upon failure, username (str) upon success
        """
        username = []
        white = (255, 255, 255)
        black = (0, 0, 0)
        green = (0, 255, 0)

        # display instruction to enter username
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 100)
        message = font.render("Enter your username:", True, green)
        message_rect = message.get_rect()
        message_rect.center = (1200 / 2, 200)

        self.screen.fill(white)
        self.screen.blit(message, message_rect)
        pygame.display.update()

        # receive input from user
        while True:
            event = pygame.event.poll()
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                return -1

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)  # Returns string id of pressed key

                if len(key) == 1: # This covers all letters and numbers not on numpad
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                        username.append(key.upper())
                    else:
                        username.append(key)
                elif key == "space":
                    username.append(" ")
                elif key == "backspace":
                    # delete last entered key
                    username.pop()
                    self.screen.fill(white)
                    self.screen.blit(message, message_rect)
                    text = font.render(''.join(username), 1, black)
                    self.screen.blit(text, (325, 330))
                    pygame.display.update()
                elif event.key == pygame.K_RETURN:  # finished typing
                    break

            # screen.blit(backgroundSurface, (0,0))
            text = font.render(''.join(username), 1, black)
            self.screen.blit(text, (325, 330))
            pygame.display.update()

            # store username
            self.username = ''.join(username)
