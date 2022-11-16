import pygame
import menutexts.texts as text
import menus.menu as menu
import gameloop.game as loop
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

def menu_english():
    pygame.display.set_caption("Morsoinvaders: Menu (English)")
    kello = pygame.time.Clock()
    fps = 60
    menutext = text.TekstitJaMuodot()
    menutext.luo_tahdet()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F1:
                    loop.peli()
                if tapahtuma.key == pygame.K_F2:
                    menu.menu()
                if tapahtuma.key == pygame.K_q:
                    exit()
            if tapahtuma.type == pygame.QUIT:
                exit()

        naytto.fill((10, 0, 20))
        menutext.tulosta_tahdet()
        menutext.menuteksti_eng()
        pygame.display.flip()
        kello.tick(fps)