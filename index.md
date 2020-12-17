# Interactive Drum Machine
### Becca Suchower

### Project Goals
For my project, I wanted to create some kind of virtual instrument, since music and building instruments are passions of mine. I decided to create a virtal drum machine, which loops drum beats based on user input. I had three main goals for this project, listed below:

1. Create a looping drum machine with user interaction
2. Create a color-changing display to accompany the audio
3. Learn a new library (Pygame) that works with sounds and displays

### Features
- **Drum Beats** - Contains sound samples for a cowbell, hi-hat, kick, open hi-hat, ride, snare, and tom (free samples from 99Sounds).
- **Metronome** - Continuously plays a metronome sound to communicate the beat to the user.
- **Color Changing Display** - Changes the background of the display to a random color (within a specified RGB color range) with each key press.
- **User Input and Looping** - Pressing the keys on the home row (A-J) once starts looping the sound, and pressing it a second time stops the current looping.

### Installation Instructions
To run this program, you will first need to install Python and Pygame. The Python installation instructions can be found [here](https://www.python.org/downloads/). Follow the installation for your preferred operating system. This program uses the built in Python libraries *time* and *random*, which are both imported within the code.

The Pygame installation instructions can be found [here](https://www.pygame.org/wiki/GettingStarted), or you can run the command ```py -m pip install -U pygame --user``` in your command window.

### Project Download Links
To download this project, you can clone the repository by running the command ```git clone https://github.com/bsuchower/interactive-programs.git``` in your command window.

### Project GitHub Page
My project repository is located at https://github.com/bsuchower/interactive-programs. 

### About Me
I'm a mechanical engineering student and current junior at Olin College of Engineering! Olin was founded in 1997 with the mission to reinvent undergraduate engineering education. Our curriculum is interdisciplinary and project-based, and focuses on working in teams beginning in the first semester. This project was completed as a final project for an Olin course called Software Design.

My email is bsuchower@olin.edu. Feel free to contact me with any questions about this project! 

### Attribution
This project uses open-source drum samples from 99Sounds. This sound library is free to download at https://99sounds.org/drum-samples/.

Pygame's documentation was extremely helpful for this project, and is located at https://www.pygame.org/docs/.
