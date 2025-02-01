import pygame
import math
from startScreen import start_screen

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 50
        self.vx = 0
        self.vy= 0
        self.facing = "front"
        self._imgs = {
            "back": pygame.image.load('Assets/girl_facing_back.png').convert_alpha(),
            "left": pygame.image.load('Assets/girl_facing_left.png').convert_alpha(),
            "front": pygame.image.load('Assets/girl_facing_front.png').convert_alpha(),
            "right": pygame.transform.flip(pygame.image.load('Assets/girl_facing_left.png').convert_alpha(), True, False),
        }

    @property
    def imgs(self):
        return self._imgs[self.facing]
    
class Sword:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 150
        self.vx = 0
        self.vy = 0
        self.throw_cooldown = False
        self.destination = (0, 0)
        self.state = "move"
        self.facing = "right"
        self._imgs = {
            "right": pygame.image.load('Assets/player_sword_right.png').convert_alpha(),
            "left": pygame.transform.flip(pygame.image.load('Assets/player_sword_right.png').convert_alpha(), True, False),
        }
    
    @property
    def imgs(self):
        return self._imgs[self.facing]
    
    def throw(self):
        self.state = "throw"
        self.throw_cooldown = True
        self.destination = pygame.mouse.get_pos()


        
        



    

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((384, 216), pygame.SCALED)
sky = (158, 153, 139)
black = (0, 0, 0)
border = [(0, 0), (384, 0), (384, 216), (0, 216)]
diagonalFactor = 1 / math.sqrt(2)

player = Player(128, 72)
player_sword = Sword(128, 72)

def start_game():
    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(sky)
        player.vx, player.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.facing = "back"
            player_sword.facing = ""
            player.vy = -1
        if keys[pygame.K_a]:
            player.facing = "left"
            player_sword.facing = "left"
            player.vx = -1
        if keys[pygame.K_s]:
            player.facing = "front"
            player_sword.facing = ""
            player.vy = 1
        if keys[pygame.K_d]:
            player.facing = "right"
            player_sword.facing = "right"
            player.vx = 1
        
        if player.vx != 0 and player.vy != 0:
            player.x = player.x + player.vx * player.speed * dt * diagonalFactor
            player.y = player.y + player.vy * player.speed * dt * diagonalFactor
        else:
            player.x = player.x + player.vx * player.speed * dt 
            player.y = player.y + player.vy * player.speed * dt 
    
        if pygame.mouse.get_pressed()[0] and player_sword.throw_cooldown == False:
            player_sword.throw()

        if player_sword.state != "throw":
            if player.facing == "right":
                player_sword.x = player.x + 55
                player_sword.y = player.y + 2
            if player.facing == "left":
                player_sword.x = player.x - 30
                player_sword.y = player.y + 2

        elif player_sword.state == "throw":
            player_sword.x += (1 if player_sword.x < player_sword.destination[0] else -1)
            player_sword.y += (1 if player_sword.y < player_sword.destination[1] else -1)
            print(f"destination: {player_sword.destination} sword x, y: {player_sword.x, player_sword.y}")

            if int(player_sword.destination[0]) == int(player_sword.x) and int(player_sword.destination[1]) == int(player_sword.y):
                player_sword.state = "move"
                player_sword.throw_cooldown = False


        #draw time
        screen.blit(player.imgs, (player.x, player.y))
        if player_sword.facing != "":
            screen.blit(player_sword.imgs, (player_sword.x, player_sword.y))




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