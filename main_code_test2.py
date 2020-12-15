import pygame
import time
import random
from pygame.locals import *

pygame.init() # initialize pygame
pygame.mixer.init() # initialize mixer module
pygame.key.set_repeat(0,500) # fixes echo

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
    # create Sound objects for the metronome
    note_keys = [K_a, K_s, K_d, K_f, K_g, K_h, K_j]
    notes = {}

    notes[K_a] = pygame.mixer.Sound("cowbell-808.wav")
    notes[K_s] = pygame.mixer.Sound("hihat-acoustic02.wav")
    notes[K_d] = pygame.mixer.Sound("kick-acoustic02.wav")
    notes[K_f] = pygame.mixer.Sound("openhat-tight.wav")
    notes[K_g] = pygame.mixer.Sound("ride-acoustic02.wav")
    notes[K_h] = pygame.mixer.Sound("snare-vinyl02.wav")
    notes[K_j] = pygame.mixer.Sound("tom-acoustic02.wav")
    metronome  = pygame.mixer.Sound("perc-808.wav")

    @staticmethod
    def play_sound(sound_object):
        """
        This method takes in an argument sound_object, which represents an
        object associated with a certain sound. It plays the sound for a
        specified amount of time, and then stops the sound.

        Args:
            sound_object: An object representing the name of the sound in the
            SoundObjects class.

            duration: An float representing the amount of time the sound plays.

            num: An int representing the channel number.

        Returns:
            Plays the sound for a specified amount of time.
        """
        sound_object.play()
        time.sleep(0.5)
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
    def __init__(self):
        self.currently_playing = []

    # @staticmethod
    def process_events(self, notes, screen):
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
                if event.key in self.currently_playing:
                    SoundObjects.notes[event.key].stop()
                elif event.key in SoundObjects.note_keys:
                    self.currently_playing.append(event.key)
                    SoundObjects.notes[event.key].play(-1)
                    Display.color_change(screen)
            #elif event.type == KEYUP:
                #if event.key in SoundObjects.note_keys:
                    #SoundObjects.notes[event.key].fadeout(500)

        return False


def main():
    # set up the screen display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Drum Machine")

    # initialize done to false
    done = False

    # create objects
    view = Display()
    sounds = SoundObjects()
    controller = Controller()
    
    # display the screen background
    view.display_background(screen)

    while not done:
        # play metronome continuously
        sounds.play_sound(sounds.metronome)

        # process events
        done = controller.process_events(sounds.notes, screen)

    # exit the window
    pygame.quit()


if __name__ == '__main__': main()