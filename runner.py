import pygame
import board


def register_click(board, coords):
    
    board.draw_x_sign(coords[0]//50, coords[1]//50)


def main():

    game_board = board.Board()

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                register_click(game_board, pos)



main()