# Description

`time-it` is a simple script to time a program that takes no args. it takes one mandatory argument in the form of an executable file you wish to time, and prints the average time of completion over some number of runs (9 by default[1]), and each individual run's time, numbered and separated by linebreaks.

# Installation

you can simply call `time-it` using your favorite python interpreter. by default, if making the .py script executable, it will use whatever python interpreter you have installed at `/usr/bin/python`

you can also re-name or cat the file to a file called simply `time-it` and mark that as executable using:

``` sh
touch time-it && cat time-it.py > time-it && chmod +x time-it
```

# Usage

this usage section assumes you chose to have a standalone `time-it` executable file. replace references to `./time-it` with the appropriate method you are using to call the script in the following section, and all in-app help documentation (i.e., what you see when using the `--help` flag). 

place `time-it.py` in the same directory as the program you wish to time, then call `./time-it ./[name of program you wish to time] [OPTIONAL: number of runs]`

### footnotes

[1] the default number in the function call is 10, but range(10) is 0..9
