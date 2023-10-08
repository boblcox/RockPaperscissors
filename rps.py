import math
import random
import pygame

# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
OFFWHITE = [215, 215, 215]
GRAY = [160, 160, 160]
RED = [255, 0 ,0]
GREEN = [0, 238, 0]
CYAN = [0, 238, 238]

screencolor = OFFWHITE
resolution = 2
jit = 1 * resolution
speed = 1 * resolution
newhanddist = 10000
handcount = 10
ishandtype1 = False
ishandtype2 = False
ishandtype3 = False
menu = True
menuselect = 1
resolutionselect = 1
handselect = 1
gameover = False
winner = "noone"
done = False
startgame = True
pause = False

# Set the height and width of the screen
screensize = [400 * resolution, 400 * resolution]
font1 = pygame.font.SysFont('freesansbold.ttf',  100)
font2 = pygame.font.SysFont('freesansbold.ttf',  72)
font3 = pygame.font.SysFont('freesansbold.ttf',  45)
font4 = pygame.font.SysFont('freesansbold.ttf',  24)

#call window
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Rock Paper Scissors")

#hand graphics
handtype1 = pygame.image.load("sign1.png").convert_alpha()
handtype1.set_colorkey(screencolor)

handtype2 = pygame.image.load("sign2.png").convert_alpha()
handtype2.set_colorkey(screencolor)

handtype3 = pygame.image.load("sign3.png").convert_alpha()
handtype3.set_colorkey(screencolor)

handtype1h = pygame.image.load("sign1h.png").convert_alpha()
handtype1h.set_colorkey(screencolor)

handtype2h = pygame.image.load("sign2h.png").convert_alpha()
handtype2h.set_colorkey(screencolor)

handtype3h = pygame.image.load("sign3h.png").convert_alpha()
handtype3h.set_colorkey(screencolor)

#handtype4 = pygame.image.load("handtype4.png").convert()
#handtype4.set_colorkey(BLACK)

#handtype5 = pygame.image.load("handtype5.png").convert()
#handtype5.set_colorkey(BLACK)

#selector = pygame.image.load("selector.png").convert()
#selector.set_colorkey(BLACK)

clock = pygame.time.Clock()

class rps(object):
    _registry = []

    def __init__(self, id, handtype, xpos, ypos, xvel, yvel):
        self._registry.append(self)
        self.id = id
        self.handtype = handtype
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel

    def proximity(self):
        for item in rps._registry:
            handdist = math.dist([item.xpos, item.ypos], [self.xpos, self.ypos])
            if item.handtype == 1 and self.handtype == 3 and handdist <10:
                self.handtype = 1
            if item.handtype == 2 and self.handtype == 1 and handdist <10:
                self.handtype = 2
            if item.handtype == 3 and self.handtype == 2 and handdist <10:
                self.handtype = 3
            #if item.handtype == self.handtype:
                #self.yvel += 10 * resolution
                #self.xvel += 10 * resolution
    
    def move(self):
        x1 = self.xpos
        y1 = self.ypos
        newhanddist = 1000
        for item in rps._registry:
            handdist = math.dist([item.xpos, item.ypos], [self.xpos, self.ypos])
            if item.handtype == 1 and self.handtype == 2 and handdist < newhanddist:
                newhanddist = handdist
                x1 = item.xpos
                y1 = item.ypos
            if item.handtype == 2 and self.handtype == 3 and handdist < newhanddist:
                newhanddist = handdist
                x1 = item.xpos
                y1 = item.ypos
            if item.handtype == 3 and self.handtype == 1 and handdist < newhanddist:
                newhanddist = handdist
                x1 = item.xpos
                y1 = item.ypos
            if item.handtype == self.handtype and 0 < handdist < 20 and item.id < self.id:
                if self.xvel < 15 * resolution:
                    self.xvel += speed
                if self.yvel < 15 * resolution:
                    self.yvel += speed
            if item.handtype == self.handtype and 0 < handdist < 20 and item.id > self.id:
                if self.xvel > speed:
                    self.xvel -= 1
                if self.yvel > speed:
                    self.yvel -= 1
        if self.xpos > x1:
            self.xpos -= self.xvel + random.randint(0 - jit, jit)
            if self.xpos - (50 * resolution) > x1:
                self.xpos -= self.xvel
        if self.xpos < x1:
            self.xpos += self.xvel + random.randint(0 - jit, jit)
            if self.xpos + (50 * resolution) < x1:
                self.xpos += self.xvel        
        else:
            self.xpos += random.randint(0 - jit, jit)
        if self.ypos > y1:
            self.ypos -= self.yvel + random.randint(0 - jit, jit)
            if self.ypos - (50 * resolution) > y1:
                self.ypos -= self.yvel
        if self.ypos < y1:
            self.ypos += self.yvel + random.randint(0 - jit, jit)
            if self.ypos + (50 * resolution) < y1:
                self.ypos += self.yvel
        else:
            self.ypos += random.randint(-1, 1)
        if self.xvel > speed:
            self.xvel -= speed
        if self.yvel > speed:
            self.yvel -= speed
        if self.xvel > 5 * resolution:
            self.xvel -= speed
        if self.yvel > 5 * resolution:
            self.yvel -= speed
        if self.xvel > 10 * resolution:
            self.xvel -= speed * resolution
        if self.yvel > 10 * resolution:
            self.yvel -= speed * resolution

    def draw(self):
        if self.handtype == 1 and resolutionselect == 1:
            screen.blit(handtype1, [self.xpos, self.ypos])
        elif self.handtype == 1 and resolutionselect == 2:
            screen.blit(handtype1h, [self.xpos, self.ypos])
        elif self.handtype == 2 and resolutionselect == 1:
            screen.blit(handtype2, [self.xpos, self.ypos])
        elif self.handtype == 2 and resolutionselect == 2:
            screen.blit(handtype2h, [self.xpos, self.ypos])
        elif self.handtype == 3 and resolutionselect == 1:
            screen.blit(handtype3, [self.xpos, self.ypos])
        elif self.handtype == 3 and resolutionselect == 2:
            screen.blit(handtype3h, [self.xpos, self.ypos])

#the game
while done is False:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.KEYDOWN:
            #if menu is False:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                #if event.key == pygame.K_LEFT:
                    #x_speed = -30
                #elif event.key == pygame.K_RIGHT:
                    #x_speed = 30
                #elif event.key == pygame.K_UP:
                    #y_speed = -30
                #elif event.key == pygame.K_DOWN:
                    #y_speed = 30
                #if event.key == pygame.K_SPACE:
                    #blast = True

                    
            if menu is True:
                if event.key == pygame.K_DOWN:
                    menuselect += 1
                    if menuselect > 4:
                        menuselect = 4
                elif event.key == pygame.K_UP:
                    menuselect -= 1
                    if menuselect < 1:
                        menuselect = 1
                elif event.key == pygame.K_LEFT:
                    if menuselect == 2:
                        resolutionselect -= 1
                        if resolutionselect < 1:
                            resolutionselect = 1
                    if menuselect == 3:
                        handselect -= 1
                        if handselect < 1:
                            handselect = 1
                elif event.key == pygame.K_RIGHT:
                    if menuselect == 2:
                        resolutionselect += 1
                        if resolutionselect > 2:
                            resolutionselect = 2
                    if menuselect == 3:
                        handselect += 1
                        if handselect > 4:
                            handselect = 4
                    
            if event.key == pygame.K_RETURN:
                if menu is True:
                    if menuselect == 1:
                        menu = False
                        startgame = True
                        menuselect = 0
                    if menuselect == 2:
                        pass
                    if menuselect == 3:
                        pass
                    if menuselect == 4:
                        pygame.QUIT
                        done = True  # Flag that we are done so we exit this loop
                if menu is False and gameover is True:
                    menu = True
                    menuselect = 3
                    gameover = False
                    pause = False     
                    handselect = 1
                    handcount = 10
                    rps._registry = []

                
            if event.key == pygame.K_ESCAPE:
                done = True  # Flag that we are done so we exit this loop
                #menu = True

        # User let up on a key
        #elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #x_speed = 0
            #elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #y_speed = 0
            #if event.key == pygame.K_SPACE:
                #blast = False
    
    # Set the screen background
    screen.fill(screencolor)

    if menu is True:
        menutext1 = font1.render("!!!RockPaperScissors!!!", True, BLACK)
        menutext2 = font4.render("IN EARLY DEVELOPMENT", True, RED)
        menutext3 = font2.render("PLAY", True, BLACK)
        menutext4 = font2.render("SCALE", True, BLACK)
        menutext5 = font2.render("NUMBER OF HANDS", True, BLACK)
        menutext6 = font2.render("EXIT", True, BLACK)
        menuscale1 = font3.render("[     ] x2", True, BLACK)
        menuscale2 = font3.render("[     ] x4", True, BLACK)
        menuhand10 = font3.render("[     ] 10", True, BLACK)
        menuhand50 = font3.render("[     ] 50", True, BLACK)
        menuhand100 = font3.render("[     ] 100", True, BLACK)
        menuhand500 = font3.render("[     ] 200", True, BLACK)
        screen.blit(menutext1, (0 * resolution, 75 * resolution))
        screen.blit(menutext2, (150 * resolution, 115 * resolution))
        screen.blit(menutext3, (60 * resolution, 160 * resolution))
        screen.blit(menutext4, (60 * resolution, 195 * resolution))
        screen.blit(menutext5, (60 * resolution, 245 * resolution))
        screen.blit(menutext6, (60 * resolution, 295 * resolution))
        screen.blit(menuscale1, (60 * resolution, 220 * resolution))
        screen.blit(menuscale2, (135 * resolution, 220 * resolution))
        screen.blit(menuhand10, (60 * resolution, 270 * resolution))
        screen.blit(menuhand50, (115 * resolution, 270 * resolution))
        screen.blit(menuhand100, (170 * resolution, 270 * resolution))
        screen.blit(menuhand500, (245 * resolution, 270 * resolution))

        # Menu selecter
        if menuselect == 1:
            pygame.draw.circle(screen, RED, [45 * resolution, 175 * resolution], 10 * resolution)
            #screen.blit(selector, [150 * resolution, 175 * resolution])
        elif menuselect == 2:
            pygame.draw.circle(screen, RED, [45 * resolution, 205 * resolution], 10 * resolution)
            #screen.blit(selector, [150 * resolution, 225 * resolution])
        elif menuselect == 3:
            pygame.draw.circle(screen, RED, [45 * resolution, 255 * resolution], 10 * resolution)
            #screen.blit(selector, [150 * resolution, 275 * resolution])
        elif menuselect == 4:
            pygame.draw.circle(screen, RED, [45 * resolution, 305 * resolution], 10 * resolution)
            #screen.blit(selector, [150 * resolution, 275 * resolution])
        if resolutionselect == 1:
            pygame.draw.circle(screen, RED, [75 * resolution, 228 * resolution], 5 * resolution)
            if resolution != 2:
                resolution = 2
                screensize = [400 * resolution, 400 * resolution]
                font1 = pygame.font.SysFont('freesansbold.ttf',  100)
                font2 = pygame.font.SysFont('freesansbold.ttf',  72)
                font3 = pygame.font.SysFont('freesansbold.ttf',  45)
                font4 = pygame.font.SysFont('freesansbold.ttf',  24)
                screen = pygame.display.set_mode(screensize)
                pygame.display.set_caption("Rock Paper Scissors")
                screen.fill(screencolor)
        elif resolutionselect == 2:
            pygame.draw.circle(screen, RED, [150 * resolution, 228 * resolution], 5 * resolution)
            if resolution != 4:
                resolution = 4
                screensize = [400 * resolution, 400 * resolution]
                font1 = pygame.font.SysFont('freesansbold.ttf',  200)
                font2 = pygame.font.SysFont('freesansbold.ttf',  144)
                font3 = pygame.font.SysFont('freesansbold.ttf',  90)
                font4 = pygame.font.SysFont('freesansbold.ttf',  48)
                screen = pygame.display.set_mode(screensize)
                pygame.display.set_caption("Rock Paper Scissors")
                screen.fill(screencolor)
        if handselect == 1:
            pygame.draw.circle(screen, RED, [75 * resolution, 278 * resolution], 5 * resolution)
            handcount = 10
        elif handselect == 2:
            pygame.draw.circle(screen, RED, [130 * resolution, 278 * resolution], 5 * resolution)
            handcount = 50
        elif handselect == 3:
            pygame.draw.circle(screen, RED, [185 * resolution, 278 * resolution], 5 * resolution)
            handcount = 100
        elif handselect == 4:
            pygame.draw.circle(screen, RED, [260 * resolution, 278 * resolution], 5 * resolution)
            handcount = 200

    if menu is False:
        if startgame is True:
            for i in range(handcount):
                rps(i, random.randint(1, 3), (random.randint(25 * resolution, 375 * resolution)), (random.randint(25 * resolution, 375 * resolution)), speed * resolution, speed * resolution)
                startgame = False
        
        for item in rps._registry:
            item.draw()
            item.proximity()
            if pause is False:
                item.move()
            if item.handtype == 1:
                ishandtype1 = True
            if item.handtype == 2:
                ishandtype2 = True
            if item.handtype == 3:
                ishandtype3 = True

        if ishandtype1 is True and ishandtype2 is False and ishandtype3 is False:
            gameover = True
            winner = "paper"
        if ishandtype1 is False and ishandtype2 is True and ishandtype3 is False:
            gameover = True
            winner = "scissors"
        if ishandtype1 is False and ishandtype2 is False and ishandtype3 is True:
            gameover = True
            winner = "rock"
        ishandtype1 = False
        ishandtype2 = False
        ishandtype3 = False

        if gameover == True:
            pause = True
            gameovertext = font1.render("GAME OVER", True, RED)
            gameovertext1 = font2.render(f"the winner is {winner}!", True, BLACK)
            gameovertext2 = font3.render(f"press enter to return to main menu", True, BLACK)
            screen.blit(gameovertext, (75 * resolution, 125 * resolution))
            screen.blit(gameovertext1, (80 * resolution, 165 * resolution))
            screen.blit(gameovertext2, (80 * resolution, 195 * resolution))
            #print("GAME OVER")
            #print(f"the winner is {winner}!")
            #print(f"press enter to return to main menu")

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(10)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()