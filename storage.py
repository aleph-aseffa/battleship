import pygame
import sqlite3
from os import path
import time


class Storage:

    def __init__(self, screen):
        """
        Initialize the Storage class.
        :param screen:
        """
        self.screen = screen  # game display window

        self.username = ""
        self.collect_user_info()
        self.db = (None, None)  # db[0] is the Connection object; db[1] is the Cursor object.

        # check if the database exists
        if not path.exists("scores.db"):
            self.create_database()
        else:
            conn = sqlite3.connect("scores.db")
            cursor = conn.cursor()
            self.db = (conn, cursor)

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

                if len(key) == 1:  # This covers all letters and numbers not on numpad
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

    def end_game(self, ai_hits, player_hits, winner):
        """
        Updates and displays the scores.
        :param: ai_hits: int, the number of ships the ai hit.
        :param: player_hits: int, the number of ships the player hit.
        :param: winner: str, which player won the game.
        :return: None.
        """
        if winner == "AI":
            self.add_score("AI", ai_hits, 1)
            self.add_score(self.username, player_hits, 0)
        else:
            self.add_score("AI", ai_hits, 0)
            self.add_score(self.username, player_hits, 1)

        self.view_scores()

    def create_database(self):
        """
        Creates database to store scores.
        :return: None.
        """
        conn = sqlite3.connect('scores.db')  # Connection object that represents the database
        c = conn.cursor()  # Cursor object
        c.execute('''CREATE TABLE scores
                    (id text, wins integer, total_score integer)''')
        conn.commit()
        self.db = conn, c

    def add_score(self, username, num_hits, win_status):
        """
        Adds the player's score to the database. Called upon game end.
        :param: username: str, player to add the score for.
        :param: num_hits: int, the number of ships the user hit.
        :param: win_status: int, 1 if the player won or 0 if the player lost.
        :return: None.
        """
        user_score = (10 * num_hits) + (500 * win_status)

        self.db[1].execute("SELECT id, wins, total_score from scores")
        # if ID matches
        # TODO: use EXISTS.
        self.db[1].execute("SELECT * FROM scores WHERE id = ?", (username,))
        data = self.db[1].fetchall()

        # if the row doesn't exist, create it
        if not data:
            self.db[1].execute("INSERT INTO scores (id, wins, total_score) VALUES (?, ?, ?)",
                               (username, win_status, user_score))
        # if the row already exists, update the score
        else:
            # collect scores that the user had prior to this game
            prev_wins = data[0][1]
            prev_score = data[0][2]
            # update the score
            self.db[1].execute("UPDATE scores SET wins = ?, total_score = ? WHERE id = ?",
                               (prev_wins + 1, prev_score + user_score, username))
        # save changes to the database
        self.db[0].commit()

    def view_scores(self):
        """
        Displays the top 10 scores at the end of the game.
        :return: None.
        """
        white = (255, 255, 255)
        black = (0, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)

        # display header
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 50)
        message = font.render("High Scores", True, blue)
        message_rect = message.get_rect()
        message_rect.center = (575, 25)

        self.screen.fill(white)
        self.screen.blit(message, message_rect)
        pygame.display.update()

        message = font.render("Username             Wins           Total Score", True, green)
        message_rect = message.get_rect()
        message_rect.center = (600, 75)
        self.screen.blit(message, message_rect)
        pygame.display.update()

        font = pygame.font.Font('freesansbold.ttf', 30)
        # select the top 10 scores (ordered by total_score)
        rows = self.db[1].execute("SELECT * FROM scores ORDER BY total_score DESC LIMIT 10")

        # display the scores of the top 10 players
        for idx, row in enumerate(rows):
            index = font.render(f"{idx+1}.", True, black)
            index_rect = index.get_rect()
            index_rect.center = (50, idx*50+125)

            name = font.render(f"{row[0]}", True, black)
            name_rect = name.get_rect()
            name_rect.center = (225, idx*50+125)

            user_wins = font.render(f"{row[1]}", True, black)
            user_wins_rect = user_wins.get_rect()
            user_wins_rect.center = (600, idx*50+125)

            user_score = font.render(f"{row[2]}", True, black)
            user_score_rect = user_score.get_rect()
            user_score_rect.center = (950, idx*50+125)

            message_rect.center = (600, 175+(idx*50))

            self.screen.blit(index, index_rect)
            self.screen.blit(name, name_rect)
            self.screen.blit(user_wins, user_wins_rect)
            self.screen.blit(user_score, user_score_rect)

            pygame.display.update()

        # close the game after 5 seconds
        time.sleep(5)
