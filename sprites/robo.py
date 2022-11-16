import pygame
robo = pygame.image.load("images/robo.png")
leveys, korkeus = 800, 800
naytto = pygame.display.set_mode((leveys, korkeus))

class Robo:
    '''Tämä luokka alustetaan "peli" funktion alussa. Metodeja kutsutaan peliloopin sisällä. Luokka piirtää pelaajan hahmon ruudulle,
    sekä liikuttaa pelaajaa nuolinäppäimiä painettaessa. Välilyönnistä ampuu laser säteitä, joilla voi puolustautua morsoja vastaan'''
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self._vasemmalle = False
        self._oikealle = False
        
    def piirra_robo(self, naytto):
        naytto.blit(robo, (self.__x, self.__y))

    def liikuta_roboa(self):
        if self._oikealle and self.__x < leveys - robo.get_width():
            if leveys == 1920 and korkeus == 1080:
                self.__x += 16
            else:
                self.__x += 8
        if self._vasemmalle and self.__x > 0:
            if leveys == 1920 and korkeus == 1080:
                self.__x -= 16
            else:
                self.__x -= 8

    @property
    def robo_x(self):
        return round(self.__x)
    
    @property
    def robo_y(self):
        return round(self.__y)
