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


waiting = True
def show(window):
    global waiting
    while waiting:
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
                        if play in icons_on_screen:
                            waiting = False
                        if music in icons_on_screen:
                            if pygame.mixer.music.get_busy():
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.play()
                    elif selector.y == 280:
                        if menu in icons_on_screen:
                            menu_func()
                            selector.y = 200
                        elif ex in icons_on_screen:
                            exit_func()
                            selector.y = 200
                    elif selector.y == 360:
                        if qu in icons_on_screen:
                            pygame.quit()
                            quit()


        pygame.display.update()
        window.fill((0, 50, 0))
        selector.show(window, 200, selector.y)
        for i in range(len(icons_on_screen)):
            icon = icons_on_screen[i]
            icon.show(window, 280, 200 + (i * 80))

play = Icon(100, 40, 'Play_button.gif')
icons_on_screen.append(play)

menu = Icon(100, 40, 'Menu_icon.gif')
icons_on_screen.append(menu)

selector = Icon(35, 40, 'Selector_icon.gif')
selector.y = 200

music = Icon(100, 40, 'Music_icon.gif')

ex = Icon(100, 40, 'Exit_icon.gif')

qu = Icon(100, 40, 'Quit_icon.gif')

def menu_func():
    icons_on_screen.remove(play)
    icons_on_screen.remove(menu)
    icons_on_screen.append(music)
    icons_on_screen.append(ex)
    icons_on_screen.append(qu)


def exit_func():
    icons_on_screen.remove(music)
    icons_on_screen.remove(ex)
    icons_on_screen.remove(qu)
    icons_on_screen.append(play)
    icons_on_screen.append(menu)

