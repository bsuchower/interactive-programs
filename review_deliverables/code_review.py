import pygame
import time
from pygame.locals import *

pygame.init() # initialize pygame
pygame.mixer.init() # initialize mixer module

# global constants
black = (0, 0, 0)
white = (255, 255, 255)
screen_width = 500
screen_height = 500

class SoundObjects:
    """
    This class creates a sound object for each drum sound, using the
    built-in Sound class in Pygame.
    """
    cowbell = pygame.mixer.Sound("cowbell-808.wav")
    hihat = pygame.mixer.Sound("hihat-acoustic02.wav")
    kick = pygame.mixer.Sound("kick-acoustic02.wav")
    openhat = pygame.mixer.Sound("openhat-tight.wav")
    ride = pygame.mixer.Sound("ride-acoustic02.wav")
    snare = pygame.mixer.Sound("snare-vinyl02.wav")
    tom = pygame.mixer.Sound("tom-acoustic02.wav")

    def play_sound(sound_object):
        """
        This method takes in an argument sound_object, which represents an
        object associated with a certain sound. It plays the sound for 1
        second, and then stops the sound.

        Args:
            sound_object: An object representing the name of the sound in the
            SoundObjects class.

        Returns:
            Plays the sound for 1 second.
        """
        sound_object.play()
        time.sleep(1) # play the sound for 1 second
        sound_object.stop()


class Display:
    """
    This class handles the background display and events.
    """
    def display_background(self, screen):
        """
        This method fills in the background of the display and adds
        text in the middle of the screen.

        Args:
            screen: An object representing the screen display.

        Returns:
            Blits the updates to the screen.
        """
        screen.fill(white)
        font = pygame.font.SysFont("tlwgtypewriter", 20)
        text = font.render("Press the keys on the home row (A-J).", True, black)
        center_x = (screen_width // 2) - (text.get_width() // 2)
        center_y = (screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        pygame.display.flip()

    def process_events(self):
        """
        This method handles the events. If the event is to quit the game,
        True is returned, and False is returned otherwise. The keys from
        A-J each correspond to playing a certain sound when pressed.

        Args:
            None.

        Returns:
            True if the event is to quit the game, False otherwise.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    SoundObjects.play_sound(SoundObjects.cowbell)
                if event.key == pygame.K_s:
                    SoundObjects.play_sound(SoundObjects.hihat)
                if event.key == pygame.K_d:
                    SoundObjects.play_sound(SoundObjects.kick)
                if event.key == pygame.K_f:
                    SoundObjects.play_sound(SoundObjects.openhat)
                if event.key == pygame.K_g:
                    SoundObjects.play_sound(SoundObjects.ride)
                if event.key == pygame.K_h:
                    SoundObjects.play_sound(SoundObjects.snare)
                if event.key == pygame.K_j:
                    SoundObjects.play_sound(SoundObjects.tom)

        return False


def main():
    # set up the screen display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Drum Machine")

    # create objects
    done = False
    display = Display()

    while not done:
        # process events
        done = display.process_events()
 
        # display the screen background
        display.display_background(screen)

    # exit the window
    pygame.quit()


if __name__ == '__main__': main()