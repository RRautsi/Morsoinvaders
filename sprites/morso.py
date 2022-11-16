import pygame
import features.pistelaskuri as P
import sprites.robo as R
from random import randint, choice


robo = pygame.image.load("images/robo.png")
morso = pygame.image.load("images/hirvio.png")
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

class Morso:
    '''Tämä luokka luo pelin vastustajat. Vastustajat tippuvat "taivaalta" ja kimpoilevat seinistä.'''
    def __init__(self, pistelaskuri: P.Pistelaskuri):
        self.__pistelaskuri = pistelaskuri
        self.__koordinaatit = {}
        self.__i = 0
        self.__morso_x_nopeus = [0, 2, -2, 3, -3, 4, -4, 5, -5]
        self.__morso_y_nopeus = [2, 3, 4]

    def lisaa_morso(self):
        '''Tätä metodia kutsutaan jatkuvasti peliloopin sisällä. Ajastin arpoo satunnaisen numeron 0-150 väliltä ja jos numero sattuu olemaan
        150, metodi lisää koordinaatteihin uuden morson.'''
        y_nopeus = self.__morso_y_nopeus
        x_nopeus = self.__morso_x_nopeus
        ajastin = randint(0, 150)
        if self.__i not in self.__koordinaatit and ajastin == 150:
            self.__koordinaatit[self.__i] = [randint(0, leveys-morso.get_width()), randint(-200, 0-morso.get_height()), choice(x_nopeus), choice(y_nopeus)]
            self.__i += 1

    def spawn_morso(self, naytto, pelaaja: R.Robo):
        krd = self.__koordinaatit
        for i in krd.copy(): 
            naytto.blit(morso, (krd[i][0], krd[i][1]))
            if krd[i][1]+morso.get_height() < korkeus + 100:
                krd[i][1]+=krd[i][3]
            if krd[i][0]+morso.get_width() < 640 or krd[i][0]+morso.get_width() > 0:
                krd[i][0]+=krd[i][2]    
            if krd[i][0]+morso.get_width() > leveys or krd[i][0]+morso.get_width() <= 0+morso.get_width():
                krd[i][2] = -krd[i][2]
            if krd[i][1]+morso.get_height() >= korkeus+morso.get_height():
                self.__pistelaskuri.vahenna_elama()
                self.poista_morso(i)
            elif krd[i][1]+morso.get_height() in range(pelaaja.robo_y, pelaaja.robo_y+robo.get_height()) and krd[i][0]+morso.get_width()//2 in range(pelaaja.robo_x, pelaaja.robo_x+robo.get_width()):
                #Tämä elif haara luo "hitboxin" pelaajalle ja katsoo osuuko morso pelaajaan, jos osuu, morso poistetaan ja elämä vähennetään"
                self.__pistelaskuri.vahenna_elama()
                self.poista_morso(i)

    def poista_morso(self, indeksi):
        del self.__koordinaatit[indeksi]

    @property
    def morsonaatit(self):
        return self.__koordinaatit