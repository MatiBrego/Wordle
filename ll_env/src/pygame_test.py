import sys, pygame
from Map import Map

pygame.init()

#Screen and map configurations
size = width, height = 600, 600
background_color = 255, 247, 235
rectangle_color = (208, 208, 208)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wordle")

new_map = Map(background_color, rectangle_color, screen)

#Text input config
base_font = pygame.font.SysFont(None, 80)
user_text = ''
input_rect = pygame.Rect(65, 60, 100, 100)
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

    new_map.build() #Builds the map

    text_surface = base_font.render(user_text, True, (0, 0, 0))

    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    input_rect.w = max(100, text_surface.get_width()+10)

    pygame.display.flip()



