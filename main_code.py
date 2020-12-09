import pygame
import time
import random
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
    metronome = pygame.mixer.Sound("perc-808.wav")

    @staticmethod
    def play_sound(sound_object, duration):
        """
        This method takes in an argument sound_object, which represents an
        object associated with a certain sound. It plays the sound for a
        specified amount of time, and then stops the sound.

        Args:
            sound_object: An object representing the name of the sound in the
            SoundObjects class.

            duration: An float representing the amount of time the sound plays.

        Returns:
            Plays the sound for a specified amount of time.
        """
        sound_object.play()
        time.sleep(duration)
        sound_object.stop()


class Display:
    """
    This class handles the background display.
    """
    @staticmethod
    def display_background(screen, color=white):
        """
        This method fills in the background of the display and adds
        text in the middle of the screen.

        Args:
            screen: An object representing the screen display.

        Returns:
            Blits the updates to the screen.
        """
        screen.fill(color)
        font = pygame.font.SysFont("tlwgtypewriter", 20)
        text = font.render("Press the keys on the home row (A-J).", True, black)
        center_x = (screen_width // 2) - (text.get_width() // 2)
        center_y = (screen_height // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])
        pygame.display.flip()

    @staticmethod
    def get_random_color():
        """
        This method generates a random RGB value within a specified range,
        and returns it.
        """
        R = random.randint(200, 250)
        G = random.randint(200, 250)
        B = random.randint(200, 250)
        random_rgb = (R, G, B)
        return random_rgb

    @staticmethod
    def color_change(screen):
        """
        This method fills in the background of the display with
        a color.

        Args:
            screen: An object representing the screen display.

        Returns:
            Displays the updates to the screen.
        """
        Display.display_background(screen, Display.get_random_color())


class Controller:
    """
    This class controls the user input and event handling.
    """
    @staticmethod
    def process_events(screen):
        """
        This method handles the events. If the event is to quit the game,
        True is returned, and False is returned otherwise. The keys from
        A-J each correspond to playing a certain sound when pressed.

        Args:
            screen: An object representing the screen display.

        Returns:
            True if the event is to quit the game, False otherwise.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    SoundObjects.play_sound(SoundObjects.cowbell, 0.3)
                    Display.color_change(screen)
                elif event.key == pygame.K_s:
                    SoundObjects.play_sound(SoundObjects.hihat, 0.3)
                    Display.color_change(screen)
                elif event.key == pygame.K_d:
                    SoundObjects.play_sound(SoundObjects.kick, 0.3)
                    Display.color_change(screen)
                elif event.key == pygame.K_f:
                    SoundObjects.play_sound(SoundObjects.openhat, 0.3)
                    Display.color_change(screen)
                elif event.key == pygame.K_g:
                    SoundObjects.play_sound(SoundObjects.ride, 0.3)
                    Display.color_change(screen)
                elif event.key == pygame.K_h:
                    SoundObjects.play_sound(SoundObjects.snare, 0.3)
                    Display.color_change(screen)
                elif event.key == pygame.K_j:
                    SoundObjects.play_sound(SoundObjects.tom, 0.3)
                    Display.color_change(screen)

        return False


def main():
    # set up the screen display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Drum Machine")

    done = False

    # create objects
    view = Display()
    sounds = SoundObjects
    controller = Controller()
    
    # display the screen background
    view.display_background(screen)

    while not done:
        # play metronome continuously
        SoundObjects.play_sound(SoundObjects.metronome, 0.5)

        # process events
        done = controller.process_events(screen)

    # exit the window
    pygame.quit()


if __name__ == '__main__': main()