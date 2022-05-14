import pygame
from Map import Map
from InputManager import InputManager

pygame.init()

#Screen and map configurations
size = width, height = 600, 600
background_color = 255, 247, 235
rectangle_color = (208, 208, 208)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wordle")

new_map = Map(background_color, rectangle_color, screen)

new_map.build() #Builds the map

new_inputManager = InputManager(new_map.get_coordinates())

while True:
    new_map.build()

    new_inputManager.check_events()

    i = 0

    for coord in new_inputManager.get_rects():
        input_rect = pygame.Rect(coord[0], coord[1], 100, 100)
        text_surface = new_inputManager.get_base_font().render(new_inputManager.get_user_letter(i), True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        i += 1
    pygame.display.flip()



