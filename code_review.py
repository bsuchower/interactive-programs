import pygame
import time
from pygame.locals import *

# Model
pygame.init() # initialize pygame
pygame.mixer.init() # initialize mixer

class SoundObjects:
    """
    Docstring
    """
    # creating a sound object for each drum sound
    cowbell = pygame.mixer.Sound("cowbell-808.wav")
    hihat = pygame.mixer.Sound("hihat-acoustic02.wav")
    kick = pygame.mixer.Sound("kick-acoustic02.wav")
    openhat = pygame.mixer.Sound("openhat-tight.wav")
    ride = pygame.mixer.Sound("ride-acoustic02.wav")
    snare = pygame.mixer.Sound("snare-vinyl02.wav")
    tom = pygame.mixer.Sound("tom-acoustic02.wav")

def play_sound(sound_object):
    """
    Docstring
    """
    sound_object.play()
    time.sleep(1) # wait and let the sound play for 1 second
    sound_object.stop()

"""
def key_press():
"""

# View
def display():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Caption Text")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Text", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    play_sound(SoundObjects.cowbell)
                if event.key == pygame.K_s:
                    play_sound(SoundObjects.hihat)
                if event.key == pygame.K_d:
                    play_sound(SoundObjects.kick)
                if event.key == pygame.K_f:
                    play_sound(SoundObjects.openhat)
                if event.key == pygame.K_g:
                    play_sound(SoundObjects.ride)
                if event.key == pygame.K_h:
                    play_sound(SoundObjects.snare)
                if event.key == pygame.K_j:
                    play_sound(SoundObjects.tom)

        screen.blit(background, (0, 0))
        pygame.display.flip()



def main():
    """
    Docstring
    """
    display()


if __name__ == '__main__': main()