import pygame
import sprites.robo as R
import features.pistelaskuri as P
from random import randint, choice

robo = pygame.image.load("images/robo.png")
kolikko = pygame.image.load("images/kolikko.png")
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

class Kolikot:
    '''Luokka spawnaa putoavia kolikkoja, joita pelaajan tulee kerätä. Kolikko poistetaan, kun se menee ruudun ulkopuolelle tai se kerätään'''
    def __init__(self, pistelaskuri: P.Pistelaskuri):
        self.__pistelaskuri = pistelaskuri
        self.__koordinaatit = {}
        self.__i = 0
        self.__kolikko_y_nopeus = [2, 3, 3, 4, 5]
        self.__leveys = leveys-kolikko.get_width() 
        self.__korkeus = 0-kolikko.get_height()

    def lisaa_kolikko(self):
        '''Tätä metodia kutsutaan jatkuvasti peliloopin sisällä. Ajastin arpoo satunnaisen numeron 0-250 väliltä ja jos numero sattuu olemaan 250, 
        metodi lisää koordinaatteihin uuden kolikon.'''
        kolikko_nopeus = self.__kolikko_y_nopeus
        ajastin = randint(0, 250)
        if self.__i not in self.__koordinaatit and ajastin == 250:
            self.__koordinaatit[self.__i] = [randint(0, self.__leveys), randint(-200, self.__korkeus), choice(kolikko_nopeus)]
            self.__i += 1

    def spawn_kolikko(self, naytto, pelaaja: R.Robo):
        krd = self.__koordinaatit
        for i in krd.copy(): 
            naytto.blit(kolikko, (krd[i][0], krd[i][1]))
            if krd[i][1]+kolikko.get_height() < korkeus + 100:
                krd[i][1]+=krd[i][2]
            if krd[i][1] >= korkeus + kolikko.get_height():
                self.__pistelaskuri.vahenna_viisisataa()
                self.poista_kolikko(i)
            elif krd[i][1]+kolikko.get_height() in range(pelaaja.robo_y, pelaaja.robo_y+robo.get_height()) and krd[i][0]+kolikko.get_width()//2 in range(pelaaja.robo_x, pelaaja.robo_x+robo.get_width()):
                #Tämä elif haara luo "hitboxin" pelaajalle ja katsoo osuuko kolikon alalaita pelaajaan, jos osuu, kolikko poistetaan ja pisteet lisätään"
                self.__pistelaskuri.lisaa_tuhat()
                self.poista_kolikko(i)
    
    def poista_kolikko(self, indeksi):
        del self.__koordinaatit[indeksi]