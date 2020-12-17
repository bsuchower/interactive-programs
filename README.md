# Interactive Drum Machine
The purpose of this project was to create an interactive drum machine program using the Pygame library. The keys on the home row from A-J each control the looping for a specific drum beat sound. Pressing the key once will start the looping, and pressing it again will stop the sound. A metronome set at 120 BPM plays continuously to communicate the beat to the user. The Pygame display window also changes color each time a key is pressed.

To run this program, you will first need to install Python and Pygame. The Python installation instructions can be found [here](https://www.python.org/downloads/). Follow the installation for your preferred operating system. This program uses the built in Python libraries *time* and *random*, which are both imported within the code.

The Pygame installation instructions can be found [here](https://www.pygame.org/wiki/GettingStarted), or you can run the command ```py -m pip install -U pygame --user``` in your command window.

To download this project, you can clone the repository by running the command ```git clone https://github.com/bsuchower/interactive-programs.git``` in your command window. Within this repository, the sound files are contained within the ```/sounds``` folder. The ```/review_deliverables``` contains previous code and architecture reviews, and the ```/previous_versions``` folder contains previous versions of the code. To use this project, simply run the ```interactive_drum_machine.py``` file in VSCode or in the command window.

This project will not work within Windows Subsystem for Linux due to complications with the Pygame display and audio handling. It will also have significant sound delays and errors within other virtual machines. I recommend that you run this project within Windows or Linux, without using any kind of virtual machine for best results.
