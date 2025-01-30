import pygame
import math
from startScreen import start_screen

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 160
        self.vx = 0
        self.vy= 0
        self.facing = "front"
        self._imgs = {
            "back": pygame.image.load('Assets/girl_facing_back.png').convert_alpha(),
            "left": pygame.image.load('Assets/girl_facing_left.png').convert_alpha(),
            "front": pygame.image.load('Assets/girl_facing_front.png').convert_alpha(),
            "right": pygame.image.load('Assets/girl_facing_right.png').convert_alpha(),
        }

    @property
    def imgs(self):
        if self.facing in(self._imgs):
            return self._imgs[self.facing]


    

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
sky = (158, 153, 139)
black = (0, 0, 0)
border = [(0, 0), (1600, 0), (1600, 900), (0, 900)]
diagonalFactor = 1 / math.sqrt(2)


player = Player(800, 450)

def start_game():
    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.vx, player.vy = 0, 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.facing = "back"
            player.vy = -1
        if keys[pygame.K_a]:
            player.facing = "left"
            player.vx = -1
        if keys[pygame.K_s]:
            player.facing = "front"
            player.vy = 1
        if keys[pygame.K_d]:
            player.facing = "right"
            player.vx = 1
        
        if player.vx != 0 and player.vy != 0:
            player.x = player.x + player.vx * player.speed * dt * diagonalFactor
            player.y = player.y + player.vy * player.speed * dt * diagonalFactor
        else:
            player.x = player.x + player.vx * player.speed * dt 
            player.y = player.y + player.vy * player.speed * dt 
    
        #draw time
        screen.fill(sky)
        player_scale = pygame.transform.scale(player.imgs,(75, 75))
        screen.blit(player_scale, (player.x, player.y))














        pygame.display.flip()
    return
        


def main():
    
    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if start_screen() == "start_game":
            start_game()


        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()