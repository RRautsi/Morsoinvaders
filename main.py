import pygame
import menus.menu as fin
import menus.menu_eng as eng
import menus.game_over as over
import menus.game_over_eng as over_eng
import gameloop.game as main_loop


def main():
    fin.menu()
    eng.menu_english()
    main_loop.peli()
    over.game_over()
    over_eng.game_over_eng()
main()
    