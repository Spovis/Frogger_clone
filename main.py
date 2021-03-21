import pygame
import player
import background
import cars
import logs
import end_screen
import Start_menu


pygame.init()

#window setup
window_size = (600, 600)
icon = pygame.image.load('Frogger logo.gif')
pygame.display.set_caption('Frogger')
pygame.display.set_icon(icon)
window = pygame.display.set_mode(window_size)
win_state = None


#set up music
pygame.mixer.music.load('Loading_Screen_Music.wav')
pygame.mixer.music.play(10000)


#death function
def death():
    global running
    running = False
    for pl in player.players:
        if pl.alive:
            running = True


#main loop
def main():
    global running, win_state
    running = True
    while running:
        #set up background
        window.fill((0, 120, 0))
        for bg in background.backgrounds:
            window.blit(bg.image, [bg.x, bg.y])

        #draw cars
        for car in cars.cars:
            car.move()
            window.blit(car.image, [car.x, car.y])
            for p in player.players:
                if car.check_hit(p.x, p.y, p.size[0], p.size[1]):
                    p.alive = False
                    death()

        #take inputs
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                    player.players[0].move('right')
                if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                    player.players[0].move('left')
                if e.key == pygame.K_UP or e.key == pygame.K_w:
                    player.players[0].move('up')
                if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                    player.players[0].move('down')


        #update logs
        for log in logs.logs:
            log.move()
            window.blit(log.image, [log.x, log.y])


        #update players
        for pl in player.players:
            if pl.alive:
                window.blit(pl.image, (pl.x, pl.y))
            else:
                player.players.remove(pl)
            for log in logs.logs:
                if pl.check_on(log.x, log.y, log.width, log.height):
                    if 0 < pl.x + log.speed < 600-pl.size[1]:
                        pl.x += log.speed
                    pl.riding = True
                    pl.log_riding = log
                else:
                    if pl.riding:
                        if not pl.check_on(pl.log_riding.x, pl.log_riding.y, pl.log_riding.width, pl.log_riding.height):
                            pl.riding = False
                            pl.log_riding = None
            if  85 < pl.y < 320:
                if not pl.riding:
                    pl.alive = False
                    death()
            if pl.y <= 40:
                pygame.display.update()
                pygame.time.wait(100)
                pl.won = True
                pl.alive = False
                win_state = 'w'
                death()


        pygame.display.update()
        pygame.time.wait(12)


Start_menu.show(window)
want_play = True
while want_play:
    main()
    end_screen.show(win_state, window)
    pl = player.Player()
pygame.quit()
quit()