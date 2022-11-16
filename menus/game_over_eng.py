import pygame
import menutexts.texts as text
import menus.menu as menu
import menus.game_over as over
import gameloop.game as loop
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

def game_over_eng(pisteet, keratyt, missatut, tuhotut, ammukset):
    pygame.display.set_caption("Morsoinvaders: Game Over")
    kello = pygame.time.Clock()
    fps = 60
    game_over_tekstit = text.TekstitJaMuodot()
    game_over_tekstit.luo_tahdet()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE:
                    menu.menu()
                if tapahtuma.key == pygame.K_r:
                    loop.peli()
                if tapahtuma.key == pygame.K_q:
                    exit()
                if tapahtuma.key == pygame.K_F1:
                    over.game_over(pisteet, keratyt, missatut, tuhotut, ammukset)
            if tapahtuma.type == pygame.QUIT:
                exit()

        naytto.fill((20, 0, 0))
        game_over_tekstit.tulosta_tahdet()
        game_over_tekstit.game_over_teksti_eng(pisteet, keratyt, missatut, tuhotut, ammukset)
        pygame.display.flip()
        kello.tick(fps)