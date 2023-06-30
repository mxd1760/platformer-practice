import pygame,sys

def draw_block(screen,color,x,y):
    pygame.draw.rect(screen,color,(64*x,64*y,64,64))
    pygame.draw.rect(screen,(0,0,0),(64*x,64*y,64,64),1)

def input(controls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        controls["jump"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                controls["left"] = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                controls["right"] = True
            if event.key == pygame.K_w or event.key==pygame.K_SPACE:
                controls["jump"] = True
            if event.key == pygame.K_w or event.key==pygame.K_UP:
                controls["up"] = True
            if event.key == pygame.K_s or event.key==pygame.K_DOWN:
                controls["down"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                controls["left"] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                controls["right"] = False
            if event.key == pygame.K_w or event.key==pygame.K_UP:
                controls["up"] = False
            if event.key == pygame.K_s or event.key==pygame.K_DOWN:
                controls["down"] = False

def draw(screen,player):
    screen.fill((100,200,255))
    for n in blocks:
        draw_block(screen,(0,100,100),n[0],n[1])
    player.draw(screen)
    pygame.display.flip()
    # if controls["left"]:
    #     pygame.draw.rect(screen,(255,0,0),(200,100,200,100))
    # # if s:
    # #     pygame.draw.circle(screen,(0,255,0),(300,300),100)
    # if controls["right"]:
    #     pygame.draw.polygon(screen,(0,0,255),[(400,100),(400,200),(500,200)])
    # if controls["jump"]:
    #     pygame.draw.polygon(screen,(255,255,255),[(600,400),(600,300),(500,200),(400,300),(400,400)])

def collisionResolution(player):
    hit = False
    for n in blocks:
        top = player.y - (n[1]*64+64)
        bottom = n[1]*64 - (player.y+64)
        left = player.x - (n[0]*64+64)
        right = n[0]*64 - (player.x+64)
        if top<0 and bottom<0 and left<0 and right<0:
            if top>bottom and top>left and top>right:
                player.y-=top
            elif bottom>left and bottom>right:
                player.y+=bottom
            elif left>right:
                player.x-=left
            else:
                player.x+=right
            hit = True
    return hit

blocks = [
    [0,9],
    [1,9],
    [2,9],
    [3,9],
    [4,9],
    [5,9],
    [6,9],
    [7,9],
    [8,9],
    [9,9],
]

class Sprite:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,screen):
        pygame.draw.rect(screen,(255,100,100),(self.x,self.y,64,64))
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,64,64),1)
    def move_left(self,speed=1):
        self.x -= speed*0.1
    def move_right(self,speed=1):
        self.x +=speed*0.1
    def move_up(self,speed=1):
        self.y -=speed*0.1
    def move_down(self,speed=1):
        self.y += speed*0.1