import pygame
class Core:
    def __init__(self, MAX_WIDTH: int, MAX_HEIGHT: int):
        pygame.init()
        self.screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        self.running = True

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False