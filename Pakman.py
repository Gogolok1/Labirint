from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,player_w,player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        prev_x,prev_y = self.rect.x,self.rect.y
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<950:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x<950:
            self.rect.x += self.speed
        if self.rect.collidelist(wall_list)!= -1:
            self.rect.x = prev_x
            self.rect.y = prev_y
class Enemy1(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 0:
            self.direction = 'right'
        if self.rect.x >= 925:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed  
class Enemy2(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.y <= 25:
            self.direction = 'top'
        if self.rect.y >= 885:
            self.direction = 'down'
        if self.direction == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed  
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_wight, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_wight = wall_wight
        self.wall_height = wall_height
        self.image = Surface((self.wall_wight, self.wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y 
    def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y)) 
#создай окно игры
window = display.set_mode((1000, 1000))
display.set_caption('Собери 5 костей')
#задай фон сцены
back = transform.scale(image.load("Fon1.png"),(1000, 1000))
#создай 2 спрайта и размести их на сцене
Dost = Enemy1('Dost.png', 460, 435, 10,65,65)
KORGI = Player('Korgi.png', 475, 155, 5,50,65)
Gogol = Enemy2('Gogolok.png', 235, 25, 10,65,65)
Gogol2 = Enemy2('Gogolok.png', 715, 895, 10,65,65)
K1 = Enemy1('Kost.PNG',75 , 100, 0,60,30)
K2 = Enemy1('Kost.PNG',875, 100,0,60,30)
K3 = Enemy1('Kost.PNG',75, 725, 0,60,30)
K4 = Enemy1('Kost.PNG',875, 725,0,60,30)
K5 = Enemy1('Kost.PNG',480, 430,0,60,30)
#Стены
w1 = Wall(100, 149, 237, 945, 15, 15, 300)
w2 = Wall(100, 149, 237, 945, 605, 15, 370)
w3 = Wall(100, 149, 237, 55, 605, 15, 370)
w4 = Wall(100, 149, 237, 55, 15, 15, 300)
w5 = Wall(100, 149, 237, 55, 15, 900, 15)
w6 = Wall(100, 149, 237, 55, 960, 900, 15)
w7 = Wall(100, 149, 237, 55, 590, 180, 15)
w8 = Wall(100, 149, 237, 780, 590, 180, 15)
w9 = Wall(100, 149, 237, 55, 500, 180, 15)
w10 = Wall(100, 149, 237, 780, 500, 180, 15)
w11 = Wall(100, 149, 237, 55, 420, 180, 15)
w12 = Wall(100, 149, 237, 780, 420, 180, 15)
w13 = Wall(100, 149, 237, 55, 315, 180, 15)
w14 = Wall(100, 149, 237, 780, 315, 180, 15)
w15 = Wall(100, 149, 237, 220, 315, 15, 120)
w16 = Wall(100, 149, 237, 780, 315, 15, 120)
w17 = Wall(100, 149, 237, 220, 515, 15, 90)
w18 = Wall(100, 149, 237, 780, 515, 15, 90)
w19 = Wall(100, 149, 237, 890, 780, 65, 15)
w20 = Wall(100, 149, 237, 65, 780, 65, 15)
w21 = Wall(100, 148, 237, 145, 870, 90, 15)
w22 = Wall(100, 149, 237, 300, 870, 120, 15)
w23 = Wall(100, 149, 237, 300, 780, 15, 105)
w24 = Wall(100, 149, 237, 775, 870, 95, 15)
w25 = Wall(100, 149, 237, 590, 870, 120, 15)
w26 = Wall(100, 149, 237, 695, 780, 15, 105)
w27 = Wall(100, 149, 237, 145, 685, 90, 15)
w28 = Wall(100, 149, 237, 220, 685, 15, 90)
w29 = Wall(100, 149, 237, 300, 685, 130, 15)
w30 = Wall(100, 149, 237, 305, 510, 15, 105)
w31 = Wall(100, 149, 237, 685, 510, 15, 105)
w32 = Wall(100, 149, 237, 305, 220, 15, 205)
w33 = Wall(100, 149, 237, 685, 220, 15, 205)
w34 = Wall(100, 149, 237, 500, 15, 15, 130)
w35 = Wall(100, 149, 237, 500, 225, 15, 115)
w36 = Wall(100, 149, 237, 500, 595, 15, 115)
w37 = Wall(100, 149, 237, 500, 775, 15, 110)
w38 = Wall(100, 149, 237, 785, 685, 15, 105)
w39 = Wall(100, 149, 237, 785, 685, 90, 15)
w40 = Wall(100, 149, 237, 590, 685, 120, 15)
w41 = Wall(100, 149, 237, 400, 595, 220, 15)
w42 = Wall(100, 149, 237, 400, 775, 220, 15)
w43 = Wall(100, 149, 237, 400, 225, 220, 15)
w44 = Wall(100, 149, 237, 320, 320, 110, 15)
w45 = Wall(100, 149, 237, 585, 320, 110, 15)
w46 = Wall(100, 149, 237, 140, 225, 90, 15)
w47 = Wall(100, 149, 237, 785, 225, 90, 15)
w48 = Wall(100, 149, 237, 140, 105, 90, 50)
w49 = Wall(100, 149, 237, 785, 105, 90, 50)
w50 = Wall(100, 149, 237, 300, 105, 130, 50)
w51 = Wall(100, 149, 237, 580, 105, 130, 50)
wall_list = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,\
    w11,w12,w13,w14,w15,w16,w17,w18,w19,\
    w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,\
    w30,w31,w32,w33,w34,w35,w36,w37,w38,w39,\
    w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50,w51]
score = 0
font.init()
font1 = font.SysFont('Arial',72)
font2 = font.SysFont('Arial', 142)
win = font2.render('Победа!',True,(255,255,255))
lose = font2.render('Поражение!',True,(255,255,255))
#mixer.init()
#mixer.music.load('Pacmenmusik.mp3')
#mixer.music.play()
clock = time.Clock()
FPS = 60
speed = 10
x1 = 600
y1 = 400
x2 = 10
y2 = 300
K_Gp = sprite.Group()
K_Gp.add(K1)
K_Gp.add(K2)
K_Gp.add(K3)
K_Gp.add(K4)
K_Gp.add(K5)
#обработай событие «клик по кнопке "Закрыть окно"»
game = True
finish = False
while game:
    for e in event.get():
       if e.type == QUIT:
           game = False
    if finish != True:

        window.blit(back,(0,0))
        Dost.update()
        KORGI.update()
        Gogol.update()
        Gogol2.update()
        Dost.reset()
        KORGI.reset()
        Gogol.reset()
        Gogol2.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()
        w18.draw_wall()
        w19.draw_wall()
        w20.draw_wall()
        w21.draw_wall()
        w22.draw_wall()
        w23.draw_wall()
        w24.draw_wall()
        w25.draw_wall()
        w26.draw_wall()
        w27.draw_wall()
        w28.draw_wall()
        w29.draw_wall()
        w30.draw_wall()
        w31.draw_wall()
        w32.draw_wall()
        w33.draw_wall()
        w34.draw_wall()
        w35.draw_wall()
        w36.draw_wall()
        w37.draw_wall()
        w38.draw_wall()
        w39.draw_wall()
        w40.draw_wall()
        w41.draw_wall()
        w42.draw_wall()
        w43.draw_wall()
        w44.draw_wall()
        w45.draw_wall()
        w46.draw_wall()
        w47.draw_wall()
        w48.draw_wall()
        w49.draw_wall()
        w50.draw_wall()
        w51.draw_wall()
        for k in K_Gp:
            k.reset()
            if sprite.collide_rect(KORGI,k):
                score+=1
                k.kill()
        if score >= 5:
                finish = True
                window.blit(win,(295,365))
        t_score = font1.render('Счёт: '+ str(score),1,(255,255,255))
        if sprite.collide_rect(KORGI,Dost) or sprite.collide_rect(KORGI,Gogol) or sprite.collide_rect(KORGI,Gogol2):
                finish = True
                window.blit(lose,(215,365))
        window.blit(t_score,(5,5))
    display.update()
    clock.tick(FPS)