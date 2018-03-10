import pygame
from pygame.locals import *

from src.const import *


class HUD():
    
    def __init__(self, game):
        self.game = game
        
        self.fonts = {"fps": pygame.font.SysFont("monospace", 20)}
        
        self.dev_mode = True

    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # developer mode
        if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_m]:
            self.dev_mode = not self.dev_mode
    
    def render(self):
        self.handle_input()
        if self.dev_mode:
            fps_display = self.fonts["fps"].render(f"{round(self.game.fps_clock.get_fps())}",
                                                   True,
                                                   BLACK)
            self.game.surface.blit(fps_display, (DISPLAY_WIDTH-fps_display.get_width(),0))