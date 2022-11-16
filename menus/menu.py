import pygame
import menutexts.texts as text
import gameloop.game as loop
import menus.menu_eng as eng
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

def menu():
    pygame.display.set_caption("Morsoinvaders: Menu")
    kello = pygame.time.Clock()
    fps = 60
    menutekstit = text.TekstitJaMuodot()
    menutekstit.luo_tahdet()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F1:
                    loop.peli()
                if tapahtuma.key == pygame.K_F2:
                    eng.menu_english()
                if tapahtuma.key == pygame.K_q:
                    exit()

            if tapahtuma.type == pygame.QUIT:
                exit()

        naytto.fill((10, 0, 20))
        menutekstit.tulosta_tahdet()
        menutekstit.menuteksti()
        pygame.display.flip()
        kello.tick(fps)