import pygame


icons_on_screen = []
class Icon:
    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(image), [self.width, self.height])

    def show(self, window, x, y):
        window.blit(self.image, [x, y])

    def clicked(self):
        self.clicked_func


def show(win_state, window):
    pygame.display.update()
    pygame.time.wait(1000)
    waiting = True
    while waiting:
        window.fill((0, 60, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                    if selector.y < 200 + (80 * (len(icons_on_screen)-1)):
                        selector.y += 80
                if e.key == pygame.K_UP or e.key == pygame.K_w:
                    if selector.y > 200:
                        selector.y -= 80
                if e.key == pygame.K_RETURN:
                    if selector.y == 200:
                        pygame.quit()
                        quit()
                    elif selector.y == 280:
                        waiting = False
                    elif selector.y == 360:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.play()

        if win_state == 'w':
            icon = pygame.transform.scale(pygame.image.load('Win_logo.gif'), [100, 70])
            window.blit(icon, (250, 80))
        else:
            icon = pygame.transform.scale(pygame.image.load('Lost_logo.gif'), [100, 70])
            window.blit(icon, (250, 80))

        selector.show(window, 200, selector.y)
        for i in range(len(icons_on_screen)):
            icon = icons_on_screen[i]
            icon.show(window, 280, 200 + (i * 80))


        pygame.display.update()
        pygame.time.wait(15)


selector = Icon(35, 40, 'Selector_icon.gif')
selector.y = 200

qu = Icon(100, 40, 'Quit_icon.gif')
icons_on_screen.append(qu)

replay = Icon(140, 40, 'Replay_icon.gif')
icons_on_screen.append(replay)

music = Icon(100, 40, 'Music_icon.gif')
icons_on_screen.append(music)


