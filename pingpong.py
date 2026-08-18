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

platform_1 = Player('png-transparent-black-m-unity-2d-black-unity-2d-black-m.png', 30, 200, 4, 50, 150)
platform_2 = Player('png-transparent-black-m-unity-2d-black-unity-2d-black-m.png', 520, 200, 4, 50, 150)
ball = GameSprite('png-transparent-a-football-football-one-in-kind.png', 200, 200, 4, 50, 50)

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
        platform_1.reset()
        platform_2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
