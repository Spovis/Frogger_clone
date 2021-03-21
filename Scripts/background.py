import pygame

backgrounds = []
class BackGround:
    def __init__(self, x, y, width, height, image, rotation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(image), [self.width,self.height]),rotation)
        backgrounds.append(self)



start_line = BackGround(0, 560, 600,40,'Start_line.gif',0)
riverbank = BackGround(0,320, 600, 40, 'Riverbank.gif',0)
road = BackGround(0,360, 600, 200, 'Road.gif',0)
river = BackGround(0, 80, 600, 240, 'Water.gif',0)
finish = BackGround(0,0,600,80,'Finish_line.gif',0)
