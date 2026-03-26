import pygame

class Ship:
    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load("Images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store float for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """ Update the ship's position based on the movement flag. """
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_up:
            self.y -= self.settings.ship_speed
        elif self.moving_down:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)