import pygame
from random import randint
pygame.font.init()
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))
fontti1 = pygame.font.SysFont("Rockwell", 20)
fontti2 = pygame.font.SysFont("Rockwell", 16)
menufontti = pygame.font.SysFont("Broadway", 66)
menufontti2 = pygame.font.SysFont("Cooper Black", 22)

class TekstitJaMuodot:
    '''Tämä luokka luo staattiset tekstit ja tähdet peliruudun taustan päälle. Metodeja kutsutaan peli ja menu funktioiden while loopin sisällä'''
    def __init__(self):
        self.tahdet = []

    def tulosta_teksti(self, elamat, pisteet):
        if elamat <= 1: 
            teksti_elamat = fontti1.render(f"Elämät: {elamat}", True, (255, 0, 0))
        else:
            teksti_elamat = fontti1.render(f"Elämät: {elamat}", True, (255, 255, 255))
        teksti_pisteet = fontti1.render(f"Pisteet: {pisteet}", True, (255, 255, 255))
        naytto.blit(teksti_elamat, (leveys-90, 0))
        naytto.blit(teksti_pisteet, (5, 0))

    def menuteksti(self):
        teksti_pelin_nimi = menufontti.render(f"MORSOINVADERS", True, (75, 0, 200))
        teksti_ohje1 = menufontti2.render(f"NÄPPÄIMET:", True, (200, 0, 0))
        teksti_ohje2 = menufontti2.render(f"[LEFT ARROW] / [RIGHT ARROW] LIIKUTTAA HAHMOA", True, (75, 0, 200))
        teksti_ohje3 = menufontti2.render(f"[SPACEBAR] AMPUU LASEREITA", True, (75, 0, 200))
        teksti_ohje4 = menufontti2.render(f"[R] RESTART", True, (75, 0, 200))
        teksti_ohje5 = menufontti2.render(f"[Q] QUIT", True, (75, 0, 200))
        teksti_ohje6 = menufontti2.render(f"TAVOITE:", True, (200, 0, 0))
        teksti_ohje7 = menufontti2.render(f"KERÄÄ PUTOAVIA KOLIKOITA", True, (75, 0, 200))
        teksti_ohje8 = menufontti2.render(f"AMMU MORSOJA ENNENKUIN NE SAAVUTTAVAT SINUT", True, (75, 0, 200))
        teksti_ohje9 = menufontti2.render(f"YRITÄ SAADA MAHDOLLISIMMAN PALJON PISTEITÄ", True, (75, 0, 200))
        teksti_ohje10 = menufontti2.render(f"[F1 - START]", True, (200, 0, 0))
        teksti_ohje11 = menufontti2.render(f"[F2 - ENGLISH MENU]", True, (200, 0, 0))
        teksti_ohje12 = menufontti2.render(f"[Q - QUIT]", True, (200, 0, 0))
        naytto.blit(teksti_pelin_nimi, (leveys//2 - teksti_pelin_nimi.get_width()//2, 100))       
        naytto.blit(teksti_ohje1, (leveys//2 - teksti_ohje1.get_width()//2, 215))
        naytto.blit(teksti_ohje2, (leveys//2 - teksti_ohje2.get_width()//2, 265))
        naytto.blit(teksti_ohje3, (leveys//2 - teksti_ohje3.get_width()//2, 315))
        naytto.blit(teksti_ohje4, (leveys//2 - teksti_ohje4.get_width()//2, 365))
        naytto.blit(teksti_ohje5, (leveys//2 - teksti_ohje5.get_width()//2, 415))
        naytto.blit(teksti_ohje6, (leveys//2 - teksti_ohje6.get_width()//2, 465))
        naytto.blit(teksti_ohje7, (leveys//2 - teksti_ohje7.get_width()//2, 515))
        naytto.blit(teksti_ohje8, (leveys//2 - teksti_ohje8.get_width()//2, 565))
        naytto.blit(teksti_ohje9, (leveys//2 - teksti_ohje9.get_width()//2, 615))
        naytto.blit(teksti_ohje10, (10, korkeus - 120))
        naytto.blit(teksti_ohje11, (10, korkeus - 80))
        naytto.blit(teksti_ohje12, (10, korkeus - 40))

    def menuteksti_eng(self):
        teksti_pelin_nimi = menufontti.render(f"MORSOINVADERS", True, (75, 0, 200))
        teksti_ohje1 = menufontti2.render(f"CONTROLS:", True, (200, 0, 0))
        teksti_ohje2 = menufontti2.render(f"[LEFT ARROW] / [RIGHT ARROW] MOVE CHARACTER", True, (75, 0, 200))
        teksti_ohje3 = menufontti2.render(f"[SPACEBAR] SHOOTS LASERS", True, (75, 0, 200))
        teksti_ohje4 = menufontti2.render(f"[R] RESTART", True, (75, 0, 200))
        teksti_ohje5 = menufontti2.render(f"[Q] QUIT", True, (75, 0, 200))
        teksti_ohje6 = menufontti2.render(f"GOAL:", True, (200, 0, 0))
        teksti_ohje7 = menufontti2.render(f"COLLECT FALLING COINS", True, (75, 0, 200))
        teksti_ohje8 = menufontti2.render(f"SHOOT BOOGEYMEN BEFORE THEY GET TO YOU", True, (75, 0, 200))
        teksti_ohje9 = menufontti2.render(f"TRY TO GET AS HIGH SCORE AS POSSIBLE", True, (75, 0, 200))
        teksti_ohje10 = menufontti2.render(f"[F1 - START]", True, (200, 0, 0))
        teksti_ohje11 = menufontti2.render(f"[F2 - FINNISH MENU]", True, (200, 0, 0))
        teksti_ohje12 = menufontti2.render(f"[Q - QUIT]", True, (200, 0, 0))
        naytto.blit(teksti_pelin_nimi, (leveys//2 - teksti_pelin_nimi.get_width()//2, 100))       
        naytto.blit(teksti_ohje1, (leveys//2 - teksti_ohje1.get_width()//2, 215))
        naytto.blit(teksti_ohje2, (leveys//2 - teksti_ohje2.get_width()//2, 265))
        naytto.blit(teksti_ohje3, (leveys//2 - teksti_ohje3.get_width()//2, 315))
        naytto.blit(teksti_ohje4, (leveys//2 - teksti_ohje4.get_width()//2, 365))
        naytto.blit(teksti_ohje5, (leveys//2 - teksti_ohje5.get_width()//2, 415))
        naytto.blit(teksti_ohje6, (leveys//2 - teksti_ohje6.get_width()//2, 465))
        naytto.blit(teksti_ohje7, (leveys//2 - teksti_ohje7.get_width()//2, 515))
        naytto.blit(teksti_ohje8, (leveys//2 - teksti_ohje8.get_width()//2, 565))
        naytto.blit(teksti_ohje9, (leveys//2 - teksti_ohje9.get_width()//2, 615))
        naytto.blit(teksti_ohje10, (10, korkeus - 120))
        naytto.blit(teksti_ohje11, (10, korkeus - 80))
        naytto.blit(teksti_ohje12, (10, korkeus - 40))

    def game_over_teksti(self, pisteet, keratyt, missatut, tuhotut, ammukset):
        if ammukset > 0 and tuhotut > 0:
            osuma_prosentti = (tuhotut/ammukset)*100
        else:
            osuma_prosentti = 0
        teksti_game_over1 = menufontti.render(f"SINÄ KUOLIT", True, (150, 0, 50))
        teksti_pisteet = menufontti2.render(f"Pisteet: {pisteet}", True, (255, 255, 255))
        teksti_tilasto1 = menufontti2.render(f"Kerätyt kolikot: {keratyt}", True, (255, 255, 255))
        teksti_tilasto2 = menufontti2.render(f"Menetetyt kolikot: {missatut}", True, (255, 255, 255))
        teksti_tilasto3 = menufontti2.render(f"Tuhotut morsot: {tuhotut}", True, (255, 255, 255))
        teksti_tilasto4 = menufontti2.render(f"Käytetyt ammukset: {ammukset}", True, (255, 255, 255))
        teksti_tilasto5 = menufontti2.render(f"Osumaprosentti: {osuma_prosentti:.1f}%", True, (255, 255, 255))
        teksti_eng_stats = menufontti2.render(f"[F1 - STATS IN ENGLISH]", True, (150, 0, 50))
        teksti_restart = menufontti2.render(f"[R - RESTART]", True, (150, 0, 50))
        teksti_menu = menufontti2.render(f"[ESC - MENU]", True, (150, 0, 50))
        teksti_quit = menufontti2.render(f"[Q - QUIT]", True, (150, 0, 50))
        naytto.blit(teksti_game_over1, (leveys//2 - teksti_game_over1.get_width()//2, 100))
        naytto.blit(teksti_pisteet, (leveys//2 - teksti_pisteet.get_width()//2, 225))
        naytto.blit(teksti_tilasto1, (leveys//2 - teksti_tilasto1.get_width()//2, 275)) 
        naytto.blit(teksti_tilasto2, (leveys//2 - teksti_tilasto2.get_width()//2, 325)) 
        naytto.blit(teksti_tilasto3, (leveys//2 - teksti_tilasto3.get_width()//2, 375)) 
        naytto.blit(teksti_tilasto4, (leveys//2 - teksti_tilasto4.get_width()//2, 425))
        naytto.blit(teksti_tilasto5, (leveys//2 - teksti_tilasto5.get_width()//2, 475))
        naytto.blit(teksti_eng_stats, (leveys//2 - teksti_eng_stats.get_width()//2, 525))
        naytto.blit(teksti_restart, (10, korkeus - 120))
        naytto.blit(teksti_menu, (10, korkeus - 80))
        naytto.blit(teksti_quit, (10, korkeus - 40))     

    def game_over_teksti_eng(self, pisteet, keratyt, missatut, tuhotut, ammukset):
        if ammukset > 0 and tuhotut > 0:
            osuma_prosentti = (tuhotut/ammukset)*100
        else:
            osuma_prosentti = 0
        teksti_game_over1 = menufontti.render(f"YOU DIED", True, (150, 0, 50))
        teksti_pisteet = menufontti2.render(f"Points: {pisteet}", True, (255, 255, 255))
        teksti_tilasto1 = menufontti2.render(f"Coins collected: {keratyt}", True, (255, 255, 255))
        teksti_tilasto2 = menufontti2.render(f"Coins missed: {missatut}", True, (255, 255, 255))
        teksti_tilasto3 = menufontti2.render(f"Boogiemen banished: {tuhotut}", True, (255, 255, 255))
        teksti_tilasto4 = menufontti2.render(f"Ammo used: {ammukset}", True, (255, 255, 255))
        teksti_tilasto5 = menufontti2.render(f"Hit rate: {osuma_prosentti:.1f}%", True, (255, 255, 255))
        teksti_fin_stats = menufontti2.render(f"[F1 - STATS IN FINNISH]", True, (150, 0, 50))
        teksti_restart = menufontti2.render(f"[R - RESTART]", True, (150, 0, 50))
        teksti_menu = menufontti2.render(f"[ESC - MENU]", True, (150, 0, 50))
        teksti_quit = menufontti2.render(f"[Q - QUIT]", True, (150, 0, 50))
        naytto.blit(teksti_game_over1, (leveys//2 - teksti_game_over1.get_width()//2, 100))
        naytto.blit(teksti_pisteet, (leveys//2 - teksti_pisteet.get_width()//2, 225))
        naytto.blit(teksti_tilasto1, (leveys//2 - teksti_tilasto1.get_width()//2, 275)) 
        naytto.blit(teksti_tilasto2, (leveys//2 - teksti_tilasto2.get_width()//2, 325)) 
        naytto.blit(teksti_tilasto3, (leveys//2 - teksti_tilasto3.get_width()//2, 375)) 
        naytto.blit(teksti_tilasto4, (leveys//2 - teksti_tilasto4.get_width()//2, 425))
        naytto.blit(teksti_tilasto5, (leveys//2 - teksti_tilasto5.get_width()//2, 475))
        naytto.blit(teksti_fin_stats, (leveys//2 - teksti_fin_stats.get_width()//2, 525))
        naytto.blit(teksti_restart, (10, korkeus - 120))
        naytto.blit(teksti_menu, (10, korkeus - 80))
        naytto.blit(teksti_quit, (10, korkeus - 40))

    def luo_tahdet(self):
        '''R, G ja B muuttujat arpovat satunnaiset värit tähdille. x ja y arpovat niille satunnaisen sijainnin.'''       
        for i in range(200):
            R = randint(0, 255)
            G = randint(0, 255)
            B = randint(0, 255)
            x = randint(0, leveys)
            y = randint(0, korkeus)
            self.tahdet.append([(R, G, B), (x, y), 1])

    def tulosta_tahdet(self):
        for tahti in self.tahdet:
            pygame.draw.circle(naytto, (tahti[0][0],tahti[0][1],tahti[0][2]), (tahti[1][0],tahti[1][1]), tahti[2])
