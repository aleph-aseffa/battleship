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

    while run:
        clock.tick(60)

        # if all the ships of the player or of the AI have been hit, end the game.
        if game_board.player_hit_ships == 20 or game_board.ai_hit_ships == 20:
            # declare the winner and terminate the game
            if game_board.player_hit_ships == 20:
                game_board.fullscreen_message("AI has won!")
            else:
                game_board.fullscreen_message("Player has won!")
            time.sleep(3)
            pygame.quit()
            run = False
            break

        # process each event.
        for event in pygame.event.get():
            #game_board.small_text("test", (100, 550))
            #game_board.small_text("another", (100, 550))
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                valid = register_click(game_board, pos, p1)

                if valid:
                    time.sleep(0.5)  # slight delay before AI makes a move
                    comp_move = comp.make_move()
                    game_board.register_ai_hit(comp_move)


if __name__ == '__main__':
    main()
