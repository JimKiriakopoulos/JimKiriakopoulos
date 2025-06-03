for p in range(5):
    print p
    x=input(3*5-1+2)
    y=raw_input(x*5)
    c=x+4
    print c
    j=c**2
    print j
    i=j+5
    print i
    x=(x+i)
    print x
    x=x**2
    print x
    x=x+7
    print x
    x=x-8
    print x
    x=x*9
    print x
    x=x/10
    print x
    x=x%6
    print x
    x=int(x)
    print x
    x=float(x)
    print x
    x=abs(x)
    print x
    x=pow(x,2)
    print x
    x=divmod(x,3)
    print y
    y=str(y)
    print x
    y=int(y)
    print y
    x=x and y 
    print x
    z=(x)or(x)
    print z
    z=not(z)
    print z
    z=z<7
    print z
    z=z>8
    print z
    z=z<=5
    print z
    z=z>=9
    print x
    z=z==10
    print z
    z=z!=20
    print z
    z=type (z)
    print z
    y=100*y
    print y
    x=x+87
    print x
    x=x-56
    print x
    print x*y
    x=x+3
    print (x)
    x=p+x
    print x
    yh=x+y
    print yh
    io=yh**2
    print io
    i=io**3
    print i
    ip=i**4
    print ip
    il=ip**3
    print il
    x2=il+c
    print x2
    j=x2+c
    print j
    x=j+c
    print x
    x=x+c
    print x
    x=x+c
    print x
    x=x+c
    print x
    x=x+c
    print x
    x=c+x
    print x
    x=c+1
    print x
    x=x+c
    print x
    x=x+c
    print x
    x=x*c
    print x
    i=x*c
    x=int(i)
    print x
    y=float(x)
    print y
    k=abs(y)
    print k
    l=pow(k,2)
    print l
    b=divmod(l,2)
    print b
    g=((l<b) and (i>b))
    print g
    d=((b>=0)and(l<y))
    print d
    h=(l==x)or(x<k)
    print h
    v=(i==k)and(i!=x)
    print v
    sd=g and d
    fg=h or v
    print fg
    x6="����"
    y6="����"
    print x6
    print y6
    v=c-100
    f=v-100
    while v<=50 and f>=100:
        print v,f
        v=v+1
        f=f+1
        print x6+y6
    else:
        v=v+1
        f=f+1
        print x6,y6        
    from pygame.locals import *
from random import randint
import pygame
import time
 
class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3) 
        self.apple = Apple(5,5)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("block.jpg").convert()
        self._apple_surf = pygame.image.load("block.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
 
        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
 
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()    