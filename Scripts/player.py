import pygame

players = []

class Player:
    def __init__(self):
        self.size = [34,32]
        self.step = 40
        self.speed = 0
        self.image = pygame.transform.scale(pygame.image.load('Frogger_frog.gif'),self.size)
        self.x = 283
        self.y = 563
        self.facing = 'up'
        self.alive = True
        self.riding = False
        self.log_riding = None
        self.won = False
        players.append(self)


    def move(self, direction):
        #keeps player on map and rotates to face the direction of travel
        if direction == 'right':
            if self.x + self.step + self.size[0] <= 600:
                if self.facing == 'up':
                    self.image = pygame.transform.rotate(self.image, -90)
                elif self.facing == 'down':
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.facing == 'left':
                    self.image = pygame.transform.rotate(self.image, 180)
                self.x += self.step
                self.facing = 'right'
        if direction == 'left':
            if self.x - self.step >= 0:
                if self.facing == 'up':
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.facing == 'down':
                    self.image = pygame.transform.rotate(self.image, -90)
                elif self.facing == 'right':
                    self.image = pygame.transform.rotate(self.image, 180)
                self.x -= self.step
                self.facing = 'left'
        if direction == 'up':
            if self.y - self.step >= 0:
                if self.facing == 'right':
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.facing == 'down':
                    self.image = pygame.transform.rotate(self.image, 180)
                elif self.facing == 'left':
                    self.image = pygame.transform.rotate(self.image, -90)
                self.y -= self.step
                self.facing = 'up'
        if direction == 'down':
            if self.y + self.size[1] + self.step <= 600:
                if self.facing == 'right':
                    self.image = pygame.transform.rotate(self.image, -90)
                elif self.facing == 'left':
                    self.image = pygame.transform.rotate(self.image, 90)
                elif self.facing == 'up':
                    self.image = pygame.transform.rotate(self.image, 180)
                self.y += self.step
                self.facing = 'down'

    def check_on(self, log_x, log_y, log_width, log_height):
        #will return true if the player is mostly on the log
        if self.x+8 >= log_x >= self.x + self.size[0] - log_width - 8 and self.y >= log_y >= self.y + self.size[1] - log_height:
            return True
        else:
            return False



player1 = Player()

