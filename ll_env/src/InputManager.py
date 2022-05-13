import pygame

class InputManager():
    def __init__(self):
        base_font = pygame.font.SysFont(None, 80)
        user_text = ''
        input_rect = pygame.Rect(65, 60, 100, 100)
        active = False