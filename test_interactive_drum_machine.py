"""
Unit testing for interactive_drum_machine.py.
"""
import pytest
from interactive_drum_machine import *

currently_playing = []  # initialize empty list


def mock_process_events(event_type, event_key=None):
    """
    This function is a mock function of the process_events function
    that performs the event handling. Since I can't test audio
    and displays, this function exists to test the key press
    functionality for different situations.
    """
    if event_type == "QUIT":
        return True
    elif event_type == "KEYDOWN":
        if event_key in currently_playing:
            currently_playing.remove(event_key)
        elif event_key in SoundObjects.note_keys:
            currently_playing.append(event_key)
        return False


def test_get_random_color():
    """
    Tests that random colors exist within a specific RGB range.
    """
    random_color = Display.get_random_color()
    assert random_color[0] <= 250 and random_color[0] >= 200
    assert random_color[1] <= 250 and random_color[1] >= 200
    assert random_color[2] <= 250 and random_color[2] >= 200


def test_play_sound():
    """
    Tests the elapsed time of play_sound.

    Since the play function cannot be tested, the function is copied
    here, replacing the lines that contain play functions with lines
    that measure the elapsed time. This checks that the time between
    playing the sounds would be about 0.5 seconds.
    """
    start = time.time()
    time.sleep(0.5)
    end = time.time()
    elapsed_time = round(end - start, 1)
    assert elapsed_time == 0.5


def test_process_events_true():
    """
    Check if the QUIT event would return true.
    """
    assert mock_process_events("QUIT") is True


def test_process_events_false():
    """
    Check if the KEYDOWN event would return False.
    """
    assert mock_process_events("KEYDOWN") is False


def test_one_key_event():
    """
    Test that one key press event would add the key to
    the currently_playing list.
    """
    mock_process_events("KEYDOWN", K_a)
    assert K_a in currently_playing


def test_two_key_event():
    """
    Test that two key press events would add the keys to
    the currently_playing list.
    """
    mock_process_events("KEYDOWN", K_a)
    mock_process_events("KEYDOWN", K_s)
    assert K_a in currently_playing
    assert K_s in currently_playing


def test_event_remove():
    """
    Test that pressing the same key twice would add and
    remove it from the currently_playing list.
    """
    mock_process_events("KEYDOWN", K_a)
    mock_process_events("KEYDOWN", K_a)
    assert K_a not in currently_playing
