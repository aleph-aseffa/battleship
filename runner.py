import pygame
import board
import player
import ai


def register_click(bd, coords, p):
    val = bd.draw_x_sign(coords[0]//50, coords[1]//50, p)
    return val


def main():

    game_board = board.Board()
    p1 = player.Player()
    comp = ai.AI()

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        if game_board.player_hit_ships == 20 or game_board.ai_hit_ships == 20:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                valid = register_click(game_board, pos, p1)

                if valid:
                    comp_move = comp.make_move()
                    game_board.register_ai_hit(comp_move)

    if p1.num_hit == 20:
        print("Player has won!")
    else:
        print("Computer has won!")


if __name__ == '__main__':
    main()
