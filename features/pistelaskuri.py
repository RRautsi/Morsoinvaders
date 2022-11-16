import pygame
import menus.game_over as over

robo = pygame.image.load("images/robo.png")
morso = pygame.image.load("images/hirvio.png")
kolikko = pygame.image.load("images/kolikko.png")

leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

fontti1 = pygame.font.SysFont("Rockwell", 20)
fontti2 = pygame.font.SysFont("Rockwell", 16)
menufontti = pygame.font.SysFont("Broadway", 66)
menufontti2 = pygame.font.SysFont("Cooper Black", 22)
class Pistelaskuri:
    '''Luokka pitää kirjaa pisteistä. Metodeja kutsutaan niin muista luokista, kuin peliloopin sisältä.'''
    def __init__(self, pisteet: int, elamat: int, pelaaja):
        self.__pisteet = pisteet
        self.__elamat = elamat
        self.tulostettavat = []
        self.ajastin = 0
        self.aikaraja = 500
        self.pelaaja = pelaaja
        self.__kerattyjen_maara = 0
        self.__missatut_maara = 0
        self.__tuhotut_morsot = 0
        self.__kaytetyt_ammukset = 0

    def lisaa_tuhat(self):
        self.__pisteet += 1000
        self.__kerattyjen_maara += 1
        teksti_tuhat = fontti2.render(f"+1000", True, (0, 255, 0))
        self.tulostettavat.append([teksti_tuhat, self.pelaaja.robo_x, self.pelaaja.robo_y - 25])

    def lisaa_sata(self):
        self.__pisteet += 100
        self.__tuhotut_morsot +=1
        teksti_sata = fontti2.render(f"+100", True, (0, 255, 0))
        self.tulostettavat.append([teksti_sata, self.pelaaja.robo_x, self.pelaaja.robo_y - 25])

    def vahenna_viisisataa(self):
        self.__pisteet -= 500
        self.__missatut_maara += 1
        teksti_viisisataa = fontti2.render(f"-500", True, (255, 0, 0))
        self.tulostettavat.append([teksti_viisisataa, self.pelaaja.robo_x+3, self.pelaaja.robo_y - 25])

    def vahenna_elama(self):
        '''Tämä metodi elämien vähentämisen lisäksi välittää pistelaskurin keräämät tiedot "game_over" funktiolle kun elämät <= 0.'''
        self.__elamat -= 1
        teksti_elama = fontti1.render(f"-1 Elämä", True, (255, 0, 0))
        self.tulostettavat.append([teksti_elama, self.pelaaja.robo_x-15, self.pelaaja.robo_y - 25])
        if self.__elamat <= 0:
            over.game_over(self.__pisteet, self.__kerattyjen_maara, self.__missatut_maara, self.__tuhotut_morsot, self.__kaytetyt_ammukset)
    
    def kaytettyjen_ammusten_maara(self):
        self.__kaytetyt_ammukset += 1

    def tulosta_naytolle(self):
        '''Tämä metodi tulostaa "pop-up" notifikaatiot pelaajan yläpuolelle kun pelaaja ansaitsee tai menettää pisteitä/elämiä'''
        for tulostus in self.tulostettavat:
            if tulostus[2] > korkeus-160:
                naytto.blit(tulostus[0], (tulostus[1], tulostus[2]))
                tulostus[2] -= 2
            else:
                self.tulostettavat.pop(self.tulostettavat.index(tulostus))

    @property
    def paivita_tulokset(self):
        '''Tämä metodi päivittää pelin aikana reaaliajassa pisteiden ja elämien määrää pelinäytöllä'''
        return (self.__pisteet, self.__elamat)