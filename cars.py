import pygame
import random
cars = []

class Car:
    def __init__(self, x, y, width, height, image, direction):
        self.x = x
        self.y = y
        self.speed = 1
        if direction == 'right':
            self.rotation = 90
        else:
            self.rotation = -90
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load(image), self.rotation), [self.width, self.height])
        cars.append(self)
        self.direction = direction

    def check_hit(self, player_x, player_y, player_width, player_height):
        if player_x - self.width < self.x < player_x + player_width and player_y - self.height < self.y < player_y + player_height:
            return True
        else:
            return False

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x >= 600:
                self.x = -self.width
        elif self.direction == 'left':
            self.x -= self.speed
            if self.x + self.width <= 0:
                self.x = 600



def row1(cars): #creates a row of evenly spaced cars
    offset = random.randint(-50, 50)
    for i in range(cars):
        new = Car((i * (665/cars)) + offset, 520, 55, 32, 'Car1.gif', 'left')

def row2(cars): #creates a row of evenly spaced cars
    offset = random.randint(-50, 50)

    for i in range(cars):
        new = Car((i * (665/cars)) + offset, 480, 55, 32, 'Car2.gif', 'right')

def row3(cars): #creates a row of evenly spaced cars
    offset = random.randint(-50, 50)

    for i in range(cars):
        new = Car((i * (665/cars)) + offset, 440, 55, 32, 'Car3.gif', 'left')

def row4(cars): #creates a row of evenly spaced cars
    offset = random.randint(-50, 50)

    for i in range(cars):
        new = Car((i * (665/cars)) + offset, 400, 55, 32, 'Car4.gif', 'right')

def row5(cars): #creates a row of evenly spaced cars
    offset = random.randint(-50, 50)

    for i in range(cars):
        new = Car((i * (665/cars)) + offset, 364, 55, 32, 'Car5.gif', 'left')


row1(3)
row2(3)
row3(2)
row4(1)
row5(2)