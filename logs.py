import pygame
import random


logs = []
class Log:
    def __init__(self, x, y, width, height, image, direction, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(image), [self.width, self.height])
        logs.append(self)
        self.direction = direction
        if self.direction == 'left':
            self.speed = -self.speed


    def move(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x >= 600:
                self.x = -self.width
        elif self.direction == 'left':
            self.x += self.speed
            if self.x + self.width <= 0:
                self.x = 600


#l1 = Log(300, 200, 120, 38, 'Small_log.gif', 'right')
#l2 = Log(120, 240, 240, 38, 'Large_log.gif', 'left')

def create_logs(row1num, row2num, row3num, row4num, row5num, row6num):
    for i in range(row1num):
        new = Log((i * (840 / row1num)) - 120, 280, 240, 38, 'Large_log.gif', 'right', 1.8)
    for i in range(row2num):
        new = Log((i * (720 / row2num)) + 240, 240, 120, 38, 'Small_log.gif', 'left', .9)
    offset = random.randint(-20, 20)
    for i in range(row3num):
        new = Log((i * (720 / row2num)) -100, 200, 120, 38, 'Small_log.gif', 'right', 1.2)
    offset = random.randint(-20, 20)
    for i in range(row4num):
        new = Log((i * (720 / row2num)) - 120, 160, 240, 38, 'Large_log.gif', 'right', .5)
    offset = random.randint(-20, 20)
    for i in range(row5num):
        new = Log((i * (720 / row2num)) + offset, 120, 120, 38, 'Small_log.gif', 'left', 1)
    for i in range(row6num):
        new = Log((i * (720 / row2num)) + 200, 80, 240, 38, 'Large_log.gif', 'right', .8)


create_logs(1,2,2,1,2,1)