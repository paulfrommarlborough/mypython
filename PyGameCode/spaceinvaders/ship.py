import pygame

class Ship:
    """ class for our ship """
    def __init__(self, ai_game):
        """ init ship. Set starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load shp
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 1.0
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:          
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        self.rect.x = self.x

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)
