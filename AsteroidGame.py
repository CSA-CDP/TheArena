import pygame
import sys
import time
from pygame.locals import *
import random

background = (0, 0, 0)
entity_color = (255, 255, 255)

global lives
global points
lives = 3
points = 0
bullet = []
listAsteroid=[]
leveltime=50
creationTime=leveltime

pygame.init()

window_width = 400
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))

WHITE = (255, 255, 255)
fontObj = pygame.font.Font('freesansbold.ttf', 12)
Gameovertext = pygame.font.Font('freesansbold.ttf', 32)

ShipImg = pygame.image.load('ship.png')
Shiplive1Img = pygame.image.load('shiplives.png')
Shiplive2Img = pygame.image.load('shiplives.png')
Shiplive3Img = pygame.image.load('shiplives.png')
LaserSound = pygame.mixer.Sound('Laser.wav')
HitSound = pygame.mixer.Sound('Explosion.wav')
bulletImg = pygame.image.load("bullet.png")
LargeImg = pygame.image.load('largerock.png')
shipx = 175
shipy = 450
highestnumber = '5000'

class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, shipx, shipy, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = shipx
        self.y = shipy
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Spaceship(Entity):
    def __init__(self, x, y, width, height):
        super(Spaceship, self).__init__(x, y, width, height)

        self.image = ShipImg


class Player(Spaceship):

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)
        #self.y_change = 0
        self.x_change = 0
        #self.y_dist = 5
        self.x_dist = 5

    def MoveKeyRight(self, key):
        """Responds to a key-down event and moves accordingly"""
        #if (key == pygame.K_UP):
            #self.y_change += -self.y_dist
        #elif (key == pygame.K_DOWN):
            #self.y_change += self.y_dist
        if (key == pygame.K_LEFT):
            self.x_change += -self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += self.x_dist

    def MoveKeyLeft(self, key):
        """Responds to a key-up event and stops movement accordingly"""
        #if (key == pygame.K_UP):
            #self.y_change += self.y_dist
        #elif (key == pygame.K_DOWN):
            #self.y_change += -self.y_dist
        if (key == pygame.K_LEFT):
            self.x_change += self.x_dist
        elif (key == pygame.K_RIGHT):
            self.x_change += -self.x_dist

    def update(self):
        """
        Moves the paddle while ensuring it stays in bounds
        """
        # Moves it relative to its current location.
        #self.rect.move_ip(0, self.y_change)
        self.rect.move_ip(self.x_change, 0 )

        # If the paddle moves off the screen, put it back on.
        if self.rect.x < 10:
            self.rect.x = 10
        elif self.rect.x > 410 - self.width:
            self.rect.x = 410 - self.width

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = bulletImg

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 15


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = LargeImg

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the block. """
        self.rect.y += 2

First = Block()
player = Player(shipx, shipy, 20, 50)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(First)

clock = pygame.time.Clock()

block_list = pygame.sprite.Group()

listAsteroid.append(First)
block_list.add(First)
all_sprites_list.add(First)

pygame.mixer.music.load('BGMusic.mp3')
pygame.mixer.music.play(-1, 0.0)

screen.fill(background)

while True:
    AsteroidsObj = Gameovertext.render('Asteroids', True, WHITE)
    Asteroidsrect = AsteroidsObj.get_rect()
    Asteroidsrect.center = (200, 100)
    screen.blit(AsteroidsObj, Asteroidsrect)

    TitlescoreObj = fontObj.render('Highscore: ' + highestnumber, True, WHITE)
    Titlescorerect = TitlescoreObj.get_rect()
    Titlescorerect.center = (200, 300)
    screen.blit(TitlescoreObj, Titlescorerect)

    InstructionsObj = fontObj.render('Press space to start' , True, WHITE)
    Instructionsrect = InstructionsObj.get_rect()
    Instructionsrect.center = (200, 400)
    screen.blit(InstructionsObj, Instructionsrect)

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_SPACE:
                while True:
                    textSurfaceObj1 = fontObj.render('Lives x ' + str(lives), True, WHITE)
                    textSurfaceObj2 = fontObj.render(str(points), True, WHITE)
                    textRectObj1 = textSurfaceObj1.get_rect()
                    textRectObj2 = textSurfaceObj2.get_rect()
                    textRectObj1 = (20, 10)
                    textRectObj2.center = (370, 10)
                    screen.fill(background)
                    pygame.display.set_caption('Asteroid Game')
                    screen.blit(textSurfaceObj1, textRectObj1)
                    screen.blit(textSurfaceObj2, textRectObj2)
                    bullet_list = pygame.sprite.Group()

                    if creationTime <= 0:  # This creates asteroids after set amount of time
                        x = Block()
                        x.rect.x = random.randrange(window_width - 30)
                        x.rect.y = (0)
                        listAsteroid.append(x)
                        block_list.add(x)
                        all_sprites_list.add(x)
                        leveltime -= 1  # each time an asteroid is formed we make it shorter until next is made
                        creationTime = leveltime

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            player.MoveKeyRight(event.key)
                        elif event.type == pygame.KEYUP:
                            player.MoveKeyLeft(event.key)

                        if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                LaserSound.play()
                                bullet = Bullet()
                                # Set the bullet so it is where the player is
                                bullet.rect.x = player.rect.x + 13
                                bullet.rect.y = player.rect.y - 58
                                # Add the bullet to the lists
                                all_sprites_list.add(bullet)
                                bullet_list.add(bullet)
                                # while bullet.rect.y != 442:     #The y does not seem to change although the bullet does move
                                # print(bullet.rect.y)

                    for bullet in bullet_list:
                        bullet_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
                        for block in bullet_hit_list:
                            HitSound.play()
                            bullet_list.remove(bullet)
                            all_sprites_list.remove(bullet)
                            points += 100
                            # Bonus lifes
                            if points / 5000 == 1 or points / 5000 == 2 or points / 5000 == 3:
                                lives += 1

                    for bullet in bullet_list:
                        if bullet.rect.y < -10:
                            bullet_list.remove(bullet)
                            all_sprites_list.remove(bullet)

                    for block in block_list:
                        if block.rect.colliderect(player.rect):
                            HitSound.play()
                            # liveimg = 'Shiplive' + livenum + 'Img'
                            # livenum = int(livenum)- 1
                            block_list.remove(block)
                            block.remove(all_sprites_list)
                            lives -= 1
                            print(lives)
                        elif block.rect.y >= 500:
                            points -= 100
                            block_list.remove(block)
                            block.remove(all_sprites_list)

                    if lives <= 0:
                        screen.fill(background)
                        block_list.remove(block)
                        block.remove(all_sprites_list)
                        # all_sprites_list.remove(bullet)
                        GameoverObj = Gameovertext.render('GAME OVER', True, WHITE)
                        Gameoverrect = GameoverObj.get_rect()
                        Gameoverrect.center = (200, 100)
                        screen.blit(GameoverObj, Gameoverrect)
                        Finalscoreobj = Gameovertext.render('Final score: ' + str(points), True, WHITE)
                        Finalscorerect = Finalscoreobj.get_rect()
                        Finalscorerect.center = (200, 150)
                        screen.blit(Finalscoreobj, Finalscorerect)
                        # HighscoreObj = Gameovertext.render((highscores), True, WHITE)
                        # Highscorerect = HighscoreObj.get_rect()
                        # Highscorerect.center = (200, 200)
                        # screen.blit(HighscoreObj, Highscorerect)
                        all_sprites_list.remove(player)
                        all_sprites_list.remove(bullet)
                        leveltime = 1000000
                        if points >= 5000:
                            HighscoreObj = Gameovertext.render('Placement: 1st', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                            highestnumber = str(points)
                        elif points >= 4500 and points <= 4999:
                            HighscoreObj = Gameovertext.render('Placement: 2nd', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 4000 and points <= 4499:
                            HighscoreObj = Gameovertext.render('Placement: 3rd', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 3500 and points <= 3999:
                            HighscoreObj = Gameovertext.render('Placement: 4th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 3000 and points <= 3499:
                            HighscoreObj = Gameovertext.render('Placement: 5th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 2500 and points <= 2999:
                            HighscoreObj = Gameovertext.render('Placement: 6th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 2000 and points <= 2499:
                            HighscoreObj = Gameovertext.render('Placement: 7th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 1500 and points <= 1999:
                            HighscoreObj = Gameovertext.render('Placement: 8th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 1000 and points <= 1499:
                            HighscoreObj = Gameovertext.render('Placement: 9th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        elif points >= 500 and points <= 999:
                            HighscoreObj = Gameovertext.render('Placement: 10th', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)
                        else:
                            HighscoreObj = Gameovertext.render('Placement: None', True, WHITE)
                            Highscorerect = HighscoreObj.get_rect()
                            Highscorerect.center = (200, 200)
                            screen.blit(HighscoreObj, Highscorerect)

                    else:
                        pass

                    for ent in all_sprites_list:
                        ent.update()

                    all_sprites_list.draw(screen)
                    creationTime -= .25
                    pygame.display.update()

                    clock.tick(60)

            else:
                pass
