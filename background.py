import pygame

class Background:
    def __init__(self, sky, border, screen):
        self.sky = sky
        self.border = border
        self.screen = screen

    
class StartScreen(Background):
    def __init__(self, sky, border, screen):
        super().__init__(sky, border, screen)
        self.strStart = " S T A R T "

    
    def draw_background(self):
        pygame.draw.polygon(self.screen, "black", self.border, 3)