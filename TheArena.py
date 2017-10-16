import pygame
import sys
import time
from pygame.locals import *
import random

pygame.init()

window_width = 450
window_height = 600
global screen
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
backgroundcolor = (0, 0, 0)
fontObj = pygame.font.Font('freesansbold.ttf', 12)
Gameovertext = pygame.font.Font('freesansbold.ttf', 24)
HPExp = pygame.font.Font('freesansbold.ttf', 11)
waveobj = pygame.font.Font('freesansbold.ttf', 16)

archerimg = pygame.image.load('Archer.png')
enemyimg = pygame.image.load('Zombiearcher.png')
enemy2img = pygame.image.load('enemy2.png')
enemy3img = pygame.image.load('enemy3.png')
enemyhitimg = pygame.image.load('Zombiearcherhit.png')
background = pygame.image.load('Arena.png')
gameoverimg = pygame.image.load('Gameover.png')
enemydeathimg = pygame.image.load('enemydeath.png')
stage2img = pygame.image.load('stage2.png')
titleimg = pygame.image.load('Title.png')
startimg = pygame.image.load('Start.png')
statsimg = pygame.image.load('Statsbar.png')
arrowimgTR = pygame.image.load('ArrowTR.png')
arrowimgDR = pygame.image.load('ArrowDR.png')
arrowimgTL = pygame.image.load('ArrowTL.png')
arrowimgDL = pygame.image.load('ArrowDL.png')
global archerx
global archery
archerx = 215
archery = 250
global enemyx
global enemyy
enemyx = 50
enemyy = 50

global wavenumber
global enemyhealthcounter
enemyhealthcounter = 20

afterhittime=15
HitTime=afterhittime         #wait time before more hits

global afterkilltime
global winTime
afterkilltime=5
winTime=afterkilltime

global afterdeathtime
global deathtime
afterdeathtime=5
deathtime=afterdeathtime

global gameovertimer
global gameovertime
gameovertimer=10
gameovertime=gameovertimer

global currenthealth
currenthealth = 200

global wavenumber
wavenumber = 1


class PlayerEntity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, archerx, archery, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = archerx
        self.y = archery
        self.width = 28
        self.height = 28
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class EnemyEntity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, enemyx, enemyy, width, height):
        pygame.sprite.Sprite.__init__(self)

        global randnum
        randnum = 0

        self.x = enemyx
        self.y = enemyy

        if randnum == 0:
            self.width = 40
            self.height = 46
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        elif randnum == 1:
            self.width = 50
            self.height = 71
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        elif randnum == 2:
            self.width = 50
            self.height = 56
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Archer(PlayerEntity):
    def __init__(self, x, y, width, height):
        super(Archer, self).__init__(x, y, width, height)

        self.image = archerimg

class Enemies(EnemyEntity):
    def __init__(self, x, y, width, height):
        super(Enemies, self).__init__(x, y, width, height)

        randnum = random.randint(0,2)
        if randnum == 0:
            self.image = enemyimg
        elif randnum == 1:
            self.image = enemy2img
        elif randnum == 2:
            self.image = enemy3img

        global hit
        hit = False


class Player(Archer):

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)
        self.y_change = 0
        self.x_change = 0
        self.y_dist = 3
        self.x_dist = 3

    def MoveKeyUp(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        if (key == pygame.K_w):
            self.y_change += self.y_dist
        elif (key == pygame.K_s):
            self.y_change += -self.y_dist
        elif (key == pygame.K_a):
            self.x_change += self.x_dist
        elif (key == pygame.K_d):
            self.x_change += -self.x_dist

    def MoveKeyDown(self, key):
        """Responds to a key-down event and moves accordingly"""
        if (key == pygame.K_w):
            if self.rect.y > 5:
                self.y_change += -self.y_dist
            #print('w')
        elif (key == pygame.K_s):
            if self.rect.y < 500:
                self.y_change += self.y_dist
            #print('s')
        elif (key == pygame.K_a):
            if self.rect.x > 20:
                self.x_change += -self.x_dist
            #print('a')
        elif (key == pygame.K_d):
            if self.rect.x < 430:
                self.x_change += self.x_dist
            #print('d')

    def update(self):
        """
        Moves the player while ensuring it stays in bounds
        """
        # Moves it relative to its current location.
        #self.rect.move_ip(0, self.y_change)
        self.rect.move_ip(self.x_change, 0)
        self.rect.move_ip(0, self.y_change)

        # If the player moves off the screen, put it back on.
        if self.rect.x < 20:
            self.rect.x = 20
        elif self.rect.x > 430 - self.width:
            self.rect.x = 430 - self.width
        elif self.rect.y < 5:
            self.rect.y = 5
        elif self.rect.y > 500 - self.height:
            self.rect.y = 500 - self.height

        # if self.rect.x < 20 and self.rect.y < 5:
        #     self.rect.x = 20
        #     self.rect.y = 5
        # elif self.rect.x < 20 and self.rect.y < 500:
        #     self.rect.x = 20
        #     self.rect.y = 500
        # elif self.rect.x > 430 and self.rect.y < 5:
        #     self.rect.x = 430
        #     self.rect.y = 5
        # elif self.rect.x < 430 and self.rect.y < 500:
        #     self.rect.x = 430
        #     self.rect.y = 500


class Enemy(Enemies):
    """
    AI controlled enemy, simply moves towards the player
    and nothing else.
    """

    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)

        self.y_change = 2
        self.x_change = 2

    def update(self):
        """
        Moves the enemy while ensuring it stays in bounds
        """
        # Moves the enemy up if the player is moves away
        if player.rect.y < self.rect.y:
            self.rect.y -= self.y_change
        elif player.rect.y > self.rect.y:
            self.rect.y += self.y_change
        elif player.rect.x < self.rect.x:
            self.rect.x -= self.x_change
        elif player.rect.x > self.rect.x:
            self.rect.x += self.x_change

        # The enemy can never go above the window since it follows
        # the player, but this keeps it from going under.
        if self.rect.x < 20:
            self.rect.x = 20
        elif self.rect.x > 430 - self.width:
            self.rect.x = 430 - self.width
        elif self.rect.y < 5:
            self.rect.y = 5
        elif self.rect.y > 500 - self.height:
            self.rect.y = 500 - self.height

class Arrow(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = arrowimgDR

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the arrow. """
        if mousex > player.rect.x and mousey > player.rect.y:
            self.image = arrowimgDR
            self.rect.x += ((mousex - player.rect.x) / 10)
            self.rect.y += ((mousey - player.rect.y) / 10)
        elif mousex < player.rect.x and mousey > player.rect.y:
            self.image = arrowimgDL
            self.rect.x -= ((player.rect.x -mousex) / 10)
            self.rect.y += ((mousey - player.rect.y) / 10)
        elif mousex > player.rect.x and mousey < player.rect.y:
            self.image = arrowimgTR
            self.rect.x += ((mousex - player.rect.x) / 10)
            self.rect.y -= ((player.rect.y - mousey) / 10)
        elif mousex < player.rect.x and mousey < player.rect.y:
            self.image = arrowimgTL
            self.rect.x -= ((player.rect.x - mousex) / 10)
            self.rect.y -= ((player.rect.y - mousey) / 10)





        if self.rect.x > 420 or self.rect.x < 20:
            all_sprites_list.remove(self)
            arrow_list.remove(self)
        elif self.rect.y > 490 or self.rect.y < 20:
            all_sprites_list.remove(self)
            arrow_list.remove(self)


        if 'enemy' in enemylist:
            if self.rect.colliderect(enemy.rect):
                global hit
                hit = True
                all_sprites_list.remove(self)
                arrow_list.remove(self)
                if hit == True:
                    screen.blit(enemyhitimg, (enemy.rect.x, enemy.rect.y))
                    global enemyhealthcounter
                    enemyhealthcounter -= 1
                    if enemyhealthcounter <= 0:
                        all_sprites_list.remove(enemy)
                        enemylist.remove('enemy')



def Startscreen():
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while True:
        screen.blit(startimg, (125, 300))
        screen.blit(titleimg, (100, 100))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    startscreentrue = True
                    if startscreentrue == True:
                        screen.fill(backgroundcolor)
                        LoadingObj = Gameovertext.render('Loading...', True, WHITE)
                        Loadingrect = LoadingObj.get_rect()
                        Loadingrect.center = (225, 250)
                        screen.blit(LoadingObj, Loadingrect)
                        pygame.display.flip()
                        Game()
        clock.tick(60)
        pygame.display.flip()



def Game():
    time.sleep(1)
    global player
    global enemy
    global enemylist
    global all_sprites_list
    global arrow_list
    player = Player(archerx, archery, 28, 28)
    enemy = Enemy(enemyx, enemyy, 24, 28)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    all_sprites_list.add(enemy)
    enemylist = []
    enemylist.append('enemy')
    arrow_list = pygame.sprite.Group()
    screen.fill(backgroundcolor)
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1, 0.0)
    global currenthealth
    global currentexp
    global totalhealth
    global totalexp
    global afterhittime
    totalhealth = 200
    currentexp = 0
    totalexp = 20
    afterhittime = 15
    while True:
        if player.rect.x < 20:
            player.rect.x = 20
        elif player.rect.x > 430 - player.width:
            player.rect.x = 430 - player.width
        elif player.rect.y < 5:
            player.rect.y = 5
        elif player.rect.y > 500 - player.height:
            player.rect.y = 500 - player.height

        screen.blit(background, (0,0))
        screen.blit(statsimg, (0, 524))
        curhealthstr = str(currenthealth)
        tothealthstr = str(totalhealth)
        HealthObj = HPExp.render(curhealthstr + '/' + tothealthstr, True, WHITE)
        Healthrect = HealthObj.get_rect()
        Healthrect.center = (65, 575)
        screen.blit(HealthObj, Healthrect)

        curexpstr = str(currentexp)
        totexpstr = str(totalexp)
        ExpObj = HPExp.render(curexpstr + '/' + totexpstr, True, WHITE)
        Exprect = ExpObj.get_rect()
        Exprect.center = (58, 550)
        screen.blit(ExpObj, Exprect)

        global wavenumber
        levelObj = waveobj.render('Wave ' + str(wavenumber), True, WHITE)
        levelrect = levelObj.get_rect()
        levelrect.center = (180, 560)
        screen.blit(levelObj, levelrect)

        arrow = Arrow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)
            else:
                pass
                #Text hp and exp bar need to be added

            if event.type == MOUSEBUTTONDOWN:
                global mousex
                global mousey
                mousex, mousey = event.pos
                # Set the bullet so it is where the player is
                arrow.rect.x = player.rect.x + 20
                arrow.rect.y = player.rect.y + 5
                # Add the bullet to the lists
                all_sprites_list.add(arrow)
                arrow_list.add(arrow)


        for ent in all_sprites_list:
            ent.update()


        if enemy.rect.colliderect(player.rect) or player.rect.colliderect(enemy.rect):
            if 'enemy' in enemylist:
                currenthealth -=2
                # while True:
                #     global HitTime
                #     HitTime -= .25
                #     clock.tick(60)
                #     if HitTime <=0:
                #         print('hi')
                #         currenthealth -=20
                #         afterhittime = 60
                #     else:
                #         pass

                if currenthealth <= 0:
                    while True:
                        global deathtime
                        deathtime -= .25
                        clock.tick(60)
                        if deathtime <= 0:
                            all_sprites_list.remove(player)
                            all_sprites_list.remove(enemy)
                            all_sprites_list.remove(arrow)
                            arrow_list.remove(arrow)
                            screen.fill(backgroundcolor)
                            screen.blit(gameoverimg, (25, 200))
                            pygame.display.flip()
                            global gameovertime
                            gameovertime -= .25
                            clock.tick(60)
                            if gameovertime <= 0:
                                sys.exit()
                            else:
                                pass
                        else:
                            pass

        if 'enemy' not in enemylist:
            time.sleep(1)
            global enemyhealthcounter
            wavenumber  += 1
            if wavenumber <= 4:
                enemyhealthcounter = 20
            elif wavenumber >= 5 and wavenumber <= 9:
                enemyhealthcounter = 30

            else:
                enemyhealthcounter = 50

            all_sprites_list.remove(player)
            all_sprites_list.remove(enemy)
            screen.fill(backgroundcolor)
            newObj = Gameovertext.render('Next stage', True, WHITE)
            newrect = newObj.get_rect()
            newrect.center = (225, 250)
            screen.blit(newObj, newrect)
            pygame.display.flip()
            if wavenumber == 5:
                healthObj = Gameovertext.render('Enemy health increased', True, WHITE)
                healthrect = healthObj.get_rect()
                healthrect.center = (225, 300)
                screen.blit(healthObj, healthrect)
                pygame.display.flip()
            elif wavenumber == 10:
                healthObj = Gameovertext.render('Enemy health increased', True, WHITE)
                healthrect = healthObj.get_rect()
                healthrect.center = (225, 250)
                screen.blit(healthObj, healthrect)
                pygame.display.flip()
            Game()


        # if 'enemy' not in enemylist:
        #     currentexp + 10
        #     global afterkilltimewd
        #     global winTime
        #     pygame.display.flip()
        #     while True:
        #         winTime -= .25
        #         clock.tick(60)
        #         if winTime <= 0:
        #             endscreen()


            # currenthealth -= 30
            # while True:
            #     afterhittime -= .25
            #     if afterhittime <= 0:
            #         afterhittime = 15


        # if currenthealth <= 0:
        #     all_sprites_list.remove(player)
        #     all_sprites_list.remove(enemy)
        #     all_sprites_list.remove(arrow)
        #     screen.fill(backgroundcolor)
        #     screen.blit(gameoverimg, (25, 100))


        all_sprites_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)


def endscreen():
    pygame.mixer.music.load('win.mp3')
    pygame.mixer.music.play(-1, 0.0)
    all_sprites_list.remove(player)
    all_sprites_list.remove(enemy)
    screen.fill(backgroundcolor)
    WinObj = Gameovertext.render('You Win!', True, WHITE)
    Winrect = WinObj.get_rect()
    Winrect.center = (225, 250)
    screen.blit(WinObj, Winrect)
    pygame.display.flip()
    time.sleep(2)
    sys.exit()


Startscreen()