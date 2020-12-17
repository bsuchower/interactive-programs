import pygame
import time
import random
from pygame.locals import *

pygame.init()  # initialize pygame
pygame.mixer.init()  # initialize pygame mixer module

# initialize global constants
black = (0, 0, 0)
white = (255, 255, 255)
screen_width = 500
screen_height = 500


class SoundObjects:
    """
    This class creates a sound object for each drum sound, using the
    built-in Sound class in Pygame. The list note_keys contains each
    key on the keyboard that can be used to play a sound. Each sound
    object is added to the dictionary called notes, which maps each key
    to the sound it is supposed to play.
    """
    note_keys = [K_a, K_s, K_d, K_f, K_g, K_h, K_j]
    notes = {}

    # create Sound objects
    notes[K_a] = pygame.mixer.Sound("sounds/cowbell-808.wav")
    notes[K_s] = pygame.mixer.Sound("sounds/hihat-acoustic02.wav")
    notes[K_d] = pygame.mixer.Sound("sounds/kick-acoustic02.wav")
    notes[K_f] = pygame.mixer.Sound("sounds/openhat-tight.wav")
    notes[K_g] = pygame.mixer.Sound("sounds/ride-acoustic02.wav")
    notes[K_h] = pygame.mixer.Sound("sounds/snare-vinyl02.wav")
    notes[K_j] = pygame.mixer.Sound("sounds/tom-acoustic02.wav")
    metronome = pygame.mixer.Sound("sounds/perc-808.wav")

    @staticmethod
    def play_sound(sound_object):
        """
        This method takes in an argument sound_object, which represents an
        object associated with a certain sound. It plays the sound for a
        specified amount of time, and then stops the sound.

        Args:
            sound_object: An object representing the name of the sound in the
            SoundObjects class.

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

        The screen fills with the preferred color and the text is displayed
        in the center of the screen each time this function is called.
        Nothing is returned, but the method blits the updates to
        the screen.

        Args:
            screen: An object representing the screen display.
            color: A tuple representing the RGB coordinates. Its default
            is set to white as the screen initializes.
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

        The range for each RGB color value is set between 200 and 250 for
        red, green, and blue. The function random.randint chooses a random
        integer between the two specified values. A tuple containing all
        three random RGB values is returned.

        Returns:
            A random RGB color code, as a tuple.
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
        a random color.

        By calling the display_background method and setting the
        color argument to the get_random_color method, the background
        color changes randomly each time this method is called.

        Args:
            screen: An object representing the screen display.
        """
        Display.display_background(screen, Display.get_random_color())


class Controller:
    """
    This class controls the user input and event handling.
    """
    def __init__(self):
        """
        Initializes the currently_playing list to an empty list.
        """
        self.currently_playing = []

    def process_events(self, notes, screen):
        """
        This method handles the events. If the event is to quit the game,
        True is returned, and False is returned otherwise. The keys from
        A-J each correspond to playing a certain sound when pressed.

        If a key is pressed, this method adds the event key to the
        currently_playing list and continues to loop the sound. If the key
        is pressed again, this method checks if the event key is in the
        currently_playing list, and stops the sound if not. The event key
        is also removed from the list so it can be played again. Each time
        a new sound is played by a key press, the display changes color by
        calling the color_change method from the Display class.

        Args:
            notes: A dictionary containing each key and its corresponding
            sound object.
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
                    self.currently_playing.remove(event.key)
                elif event.key in SoundObjects.note_keys:
                    self.currently_playing.append(event.key)
                    SoundObjects.notes[event.key].play(-1)
                    Display.color_change(screen)

        return False


def main():
    """
    The main function continuously runs the game until told to quit.

    This function first sets done to False. While done is false, the metronome
    sound is played continuously, and the game continuously runs by calling the
    process_events method from the Controller class. When the user quits the
    game, done is set to true, so the loop ends and the window closes.
    """
    # set up the screen display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Interactive Drum Machine")

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


if __name__ == '__main__':
    main()
