import pygame
import menutexts.texts as text
import sprites.robo as R
import sprites.morso as M
import sprites.kolikko as K
import sprites.laser as L
import features.pistelaskuri as P
pygame.init() 

robo = pygame.image.load("images/robo.png")
morso = pygame.image.load("images/hirvio.png")
kolikko = pygame.image.load("images/kolikko.png")

leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

def peli():
    pygame.display.set_caption(f"Morsoinvaders: In-game")
    kello = pygame.time.Clock()
    fps = 60
    
    elamat, pisteet= 5, 0
    pelaaja_x, pelaaja_y = leveys/2 - robo.get_width()/2, korkeus-robo.get_height()

    tekstit_ja_muodot = text.TekstitJaMuodot()
    pelaaja = R.Robo(pelaaja_x, pelaaja_y)
    pistelaskuri =  P.Pistelaskuri(pisteet, elamat, pelaaja)
    morsot = M.Morso(pistelaskuri)
    kolikot = K.Kolikot(pistelaskuri)
    tekstit_ja_muodot.luo_tahdet()
    laser = L.Laser(naytto, pelaaja, pistelaskuri)
    
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    pelaaja._vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    pelaaja._oikealle = True
                if tapahtuma.key == pygame.K_SPACE:
                    laser.lisaa_ammus()
                if tapahtuma.key == pygame.K_r:
                    peli()
                if tapahtuma.key == pygame.K_q:
                    exit()

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    pelaaja._vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    pelaaja._oikealle = False

            if tapahtuma.type == pygame.QUIT:
                exit()
        
        naytto.fill((20, 0, 35))
        tekstit_ja_muodot.tulosta_teksti(elamat, pisteet)
        tekstit_ja_muodot.tulosta_tahdet()

        morsot.lisaa_morso()
        kolikot.lisaa_kolikko()

        laser.ammu_laser(morsot)
        pelaaja.liikuta_roboa()
        pelaaja.piirra_robo(naytto)
        morsot.spawn_morso(naytto, pelaaja)
        kolikot.spawn_kolikko(naytto, pelaaja)

        pisteet = pistelaskuri.paivita_tulokset[0]
        elamat = pistelaskuri.paivita_tulokset[1]
        pistelaskuri.tulosta_naytolle()

        pygame.display.flip()
        kello.tick(fps)