COPYRIGHT
=========
Copyright (C) 2019- Andrea Sterbini <sterbini@di.uniroma1.it>, 
                    Angelo Monti <monti@di.uniroma1.it>, 
                    Matteo Neri <matteo2794@outlook.com>,
                    Andrei Laurentiu Lepadat <lepadat.1677093@studenti.uniroma1.it>,
                    Eduardo Rinaldi <rinaldi.1797800@studenti.uniroma1.it>,
                    Angelo Spognardi <spognardi@di.uniroma1.it>, 
                    Claudio Di Ciccio <diciccio@di.uniroma1.it>

All programs and files contained in this archive/directory are released under the GPL v.3 license. 
(https://www.gnu.org/licenses/gpl-3.0.en.html)

INSTRUCTIONS
==========
To do the exercise, edit the *program.py* file using a text editor such as Notepad++ or, preferably, an IDE like Spyder, Atom, or PyCharm. Please DO NOT use Notepad, Word, Wordpad or other document editors alike.

TEST
====
This directory contains the necessary files to verify that your program works correctly on at least three input examples. To run the tests, you should have installed Python and the necessary libraries on your system (please find further instructions below).

To check if your program works as expected on the sample data:
1. open an Anaconda Prompt window and set the current directory to the exercise directory (using the cd command);
2. execute the following command:
	python test.py
   or
	pytest test.py

To get more detailed information about the execution, with a time-performance analysis held on single sections of the program, execute the following command:
	pytest -v -rA --profile test.py

SOLUTION
=========
The directory contains a solution implemented by the instructors. We recommend you to examine it ONLY AFTER TRYING TO SOLVE THE EXERCISE ON YOUR OWN.

INSTALLATION
=============
To be able to perform the tests on this and other exercises, you should install the following packages on your PC:
- an Anaconda distribution that includes Python 3.x (from https://www.anaconda.com/distribution/);
- the pytest, ddt, pytest-timeout and pytest-profiling Python modules; to do so, open an Anaconda Prompt and run the following commands:
	conda install -c conda-forge pytest
	conda install -c conda-forge ddt
	conda install -c conda-forge pytest-timeout
	conda install -c conda-forge pytest-profiling
