import pygame
from pygame.locals import *

from src.const import *
from src.game_object.timeline import Timeline


class HUD():
    
    def __init__(self, game):
        self.game = game
        
        self.fonts = {"fps": pygame.font.SysFont("monospace", 20)}
        
        self.dev_mode = False

        # floor
        floor = Timeline(self.game, left=0)
        self.game.add_entity(floor)

    def mode_toggle(self):
        self.dev_mode = not self.dev_mode
    
    def draw(self):
        if self.dev_mode:
            fps_display = self.fonts["fps"].render(f"{round(self.game.fps_clock.get_fps())}",
                                                   True,
                                                   GREEN)
            self.game.surface.blit(fps_display, (DISPLAY_WIDTH-fps_display.get_width(),0))