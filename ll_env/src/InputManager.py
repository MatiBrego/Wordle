import sys, pygame

class InputManager():
    def __init__(self, coords):
        self.base_font = pygame.font.SysFont(None, 80)
        self.user_letters = ''
        self.input_rects = []
        self.generate_rects(coords)

    def generate_rects(self, coords):
        for coord in coords:
            self.input_rects.append((coord[0]+25, coord[1]+20))

    def get_user_letter(self, i):
        if len(self.user_letters) > i:
            return self.user_letters[i]

    def get_base_font(self):
        return self.base_font

    def get_rects(self):
        return self.input_rects

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    self.user_letters = self.user_letters[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    self.user_letters += event.unicode