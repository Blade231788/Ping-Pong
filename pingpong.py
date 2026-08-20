from pygame import *

class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

back = (200, 255, 255)
window = display.set_mode((600, 500))
window.fill(back)

clock = time.Clock()
FPS = 60

platform_1 = Player('Untitled.png', 30, 200, 4, 15, 140)
platform_2 = Player('Untitled.png', 520, 200, 4, 15, 140)
ball = GameSprite('vecteezy_soccer-ball-png-with-ai-generated_26772408.png', 280, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
win_1 = font.render('ИГРОК 1 ВЫИГРАЛ', True, (0, 250, 0))
win_2 = font.render('ИГРОК 2 ВЫИГРАЛ', True, (0, 250, 0))

speed_x = 3
speed_y = 3

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)

        platform_1.update_l()
        platform_2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(platform_1, ball) or sprite.collide_rect(platform_2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(win_2, (200, 200))
        
        if ball.rect.x > 600:
            finish = True
            window.blit(win_1, (200, 200))

        platform_1.reset()
        platform_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
