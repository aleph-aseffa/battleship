import pygame
import board
import player
import ai
import time


def register_click(bd, coords, p):
    """
    Register the user's click on the board
    :param bd: Board, an instance of the Board class.
    :param coords: tuple(int,int), coordinates of the click
    :param p: Player, an instance of the Player class.
    :return: bool, whether or not the player hit an AI ship.
    """
    val = bd.user_hit(coords[0]//50, coords[1]//50, p)
    return val


def main():

    game_board = board.Board()
    p1 = player.Player()
    comp = ai.AI()

    run = True
    clock = pygame.time.Clock()
    winner = None  # who won the game?

    while run:
        clock.tick(60)

        # if all the ships of the player or of the AI have been hit, end the game.
        if game_board.player_hit_ships == 1 or game_board.ai_hit_ships == 1:
            # declare the winner and end the game
            if game_board.player_hit_ships == 1:
                game_board.fullscreen_message("AI has won!")
                winner = "AI"
            else:
                game_board.fullscreen_message("Player has won!")
                winner = game_board.info.username
            time.sleep(3)
            run = False
            break

        # process each event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                valid = register_click(game_board, pos, p1)

                if valid:
                    time.sleep(0.5)  # slight delay before AI makes a move
                    comp_move = comp.make_move()
                    game_board.register_ai_hit(comp_move)

    # display the top scores
    game_board.info.end_game(game_board.player_hit_ships, game_board.ai_hit_ships, winner)
    # end the game
    pygame.quit()


if __name__ == '__main__':
    main()
