import sys
import pygame
from Settings import Settings
from ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    def __init__(self):
        """ Initialize the game and create the game resources. """
        # [1] Create the tools that pygame needs to run properly
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # [2] Name the window
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color
        self.bg_color = (230,230,230)

       
    def RunGame(self):
        """ Start the main loop """
        # [3] Main game loop
        while True:
            self._check_events()
            self.ship.update()

            # RUN THIS LAST
            self._update_screen()
            
            
    def _check_events(self):
        """ Respond to key presses and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)


    def _check_keydown_event(self, event):
        """ Respond to key presses """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_event(self, event):
        """ Respond to key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """ Update the images on the screen and flip to the new screen """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.RunGame()