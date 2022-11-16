import pygame
import sprites.robo as R
import sprites.morso as M
import features.pistelaskuri as P

robo = pygame.image.load("images/robo.png")
morso = pygame.image.load("images/hirvio.png")

leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

class Laser:
    '''Tämä luokka mahdollistaa laser säteiden ampumisen. "ammu_laser" pitää kirjaa laser säteiden sekä morsojen koordinaateista. 
    Mikäli ne kohtaavat, morso ja säde poistetaan näytöltä'''
    def __init__(self, naytto, pelaaja: R.Robo, pistelaskuri: P.Pistelaskuri):
        self.__pistelaskuri = pistelaskuri
        self.robo = pelaaja
        self.naytto = naytto
        self.ammukset = {}
        self.laaseri_surf = pygame.Surface((5,35)).convert()
        self.laaseri_surf.fill((255,0,0))
        self.nopeus = 15
        self.cooldown = 300
        self.ajastin = 0
        self.i = 0
        self.lisaa_laser = False

    def lisaa_ammus(self):
        '''Tässä metodissa käytetään tickejä, jotta lasereiden ampumiseen saadaan ajastettua taukoja (=cooldown).'''
        robo_y = self.robo.robo_y
        robo_x = self.robo.robo_x + robo.get_width()//2
        if pygame.time.get_ticks() - self.ajastin > self.cooldown:
            self.ajastin = pygame.time.get_ticks()
            self.lisaa_laser = True
        if self.i not in self.ammukset and self.lisaa_laser:
            self.ammukset[self.i] = [robo_x, robo_y]
            self.i += 1
            self.__pistelaskuri.kaytettyjen_ammusten_maara()
            self.lisaa_laser = False

    def ammu_laser(self, morsot: M.Morso):
        '''Tämä metodi iteroi lasereiden sekä morsojen koordinaatteja. Mikäli ne kohtaavat, sekä lasersäde, että morso poistetaan tietorakenteista.
        Myös ruudun ulkopuolelle menevät lasersäteet poistetaan "ammukset" sanakirjasta'''
        ammukset = self.ammukset
        laser_pituus = self.laaseri_surf.get_height()
        laser_leveys = self.laaseri_surf.get_width()//2
        morsonaatit = morsot.morsonaatit
        for ammus in ammukset.copy():
            ammukset[ammus][1] -= self.nopeus
            self.naytto.blit(self.laaseri_surf, (ammukset[ammus][0], ammukset[ammus][1]))
            if ammukset[ammus][1] < 0:
                del ammukset[ammus]
            for j in morsonaatit.copy():
                if j in morsonaatit and ammus in ammukset:   
                    if ammukset[ammus][1]+laser_pituus in range(morsonaatit[j][1], morsonaatit[j][1]+morso.get_height()) and ammukset[ammus][0]+laser_leveys in range(morsonaatit[j][0], morsonaatit[j][0]+morso.get_width()):
                        del ammukset[ammus]
                        morsot.poista_morso(j)
                        self.__pistelaskuri.lisaa_sata()
                else:
                    continue