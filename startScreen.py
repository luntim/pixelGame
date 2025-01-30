import pygame

screen = pygame.display.set_mode((1600, 900))
border = [(0, 0), (1600, 0), (1600, 900), (0, 900)]
sky = (101, 51, 44)

def start_screen():
    screen.fill(sky)
    pygame.draw.polygon(screen, "black", border, 3)
    font = pygame.font.Font("freesansbold.ttf", 40)

    text = font.render("S T A R T", True, "black")
    textRect = text.get_rect()
    borderRect = textRect
    textRect.center = (1600 // 2, 900 // 2)
    borderRect.center = (1600// 2, (900 // 2) -5)

    cursor = pygame.mouse.get_pos()
    
    if textRect.collidepoint(cursor):
        fillOrWidth = 0
        color = "green"
    else:
        fillOrWidth = 3
        color = "black"

    pygame.draw.rect(screen, color, borderRect, fillOrWidth, 5)
    screen.blit(text, textRect)

    if textRect.collidepoint(cursor) and pygame.mouse.get_pressed()[0]:
        return "start_game"
    

  


    

        