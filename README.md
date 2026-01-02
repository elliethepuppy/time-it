# Description

`time-it` is a simple script to time a program. it takes one mandatory argument in the form of an executable file you wish to time, and prints the average time of completion over some number of runs (10 by default), and each individual run's time, numbered and separated by linebreaks.

# Installation

no installation is strictly necessary. just place the script in the same directory as the program you want to time, then you can simply call `time-it` using your favorite python interpreter. by default, if making the .py script executable, it will use whatever python interpreter you have installed at `/usr/bin/python`

you can also re-name the script or cat the file to just `time-it`, then mark that as executable using:

``` sh
touch time-it && cat time-it.py > time-it && chmod +x time-it
```

# Usage


this usage section assumes you chose to have a standalone `time-it` executable file. replace references to `./time-it` with the appropriate method you are using to call the script in the following section, and all in-app help documentation (i.e., what you see when using the `--help` flag). 

place `time-it.py` in the same directory as the program you wish to time, then call `./time-it [optional logging and interpreter flags] [./<your program name here>, or an appropriate script for your chosen interpreter] [args for the program you're timing]`

note: arguments must be supplied in *exactly* the order described, but flags can be entered in any order[1]. an interpreter cannot be used when calling an executable with `./`. doing anything else is UNTESTED and UNDEFINED behavior, and is your concern, not mine.

if using the `--log` flag, the log will be written to `~/.cache/time-it.log`, and will always append the newest results.

note: these instructions are for linux (probably posix/unix-like systems in general). if you're on windows, trial and error, and if you want to contribute a more effective windows implementation, submit a pr.

### footnotes

[1] e.g., `./time-it -r 10 -i python -l [prog]`, `./time-it -i python -l -r 10 [prog]`, `./time-it -l -r 10 -i python [prog]` and any other variation thereof are all equivalent, but `./time-it [prog] [flags]` is **not** allowed, and *will* result in undefined behavior.
