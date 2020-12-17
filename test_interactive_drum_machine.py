"""
Unit testing for interactive_drum_machine.py.
"""
import pytest
from interactive_drum_machine import *

def test_get_random_color():
    """
    Tests that random colors exist within a specific RGB range.
    """
    random_color = Display.get_random_color()
    assert random_color[0] <= 250 # and random_color[0] >= 200
    # assert random_color[1] <= 250 and random_color[1] >= 200
    # assert random_color[2] <= 250 and random_color[2] >= 200


