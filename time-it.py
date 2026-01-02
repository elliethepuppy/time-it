#!/usr/bin/python

import time
import subprocess
import sys
from datetime import datetime
from pathlib import Path

home = Path.home()
HELP_MESSAGE = """
time-it: a simple executable timer
usage: place time-it in the same directory as the program you wish to time, then
run './time-it [optional logging and interpreter flags] [./<your program name>
or an appropriate script for your interpreter] [arguments for the timed program]

all available flags:
-h --help          display this help message
-cl --clear-log    delete the log file located at
                   ~/.config/time-it.log, if any
-l --log           write the generated output to
                   the log file located at
                   ~/.config/time-it.log
-i --interpreter   use an interpreter to run
                   the program, rather than
                   calling it inherently
"""
def print_help_and_exit(exit_code: int) -> None:
    print(HELP_MESSAGE)
    exit(exit_code)


def time_it(exe_with_args: str, times: int = 10) -> tuple[str, str]:
    total_times: list[float] = []
    all_times: str = ""
    avg_time: float = 0.0
    tmp: float = 0.0

    for i in range(times + 1):
        start = time.time()
        subprocess.run(exe_with_args.strip().split(" "))
        end = time.time()
        total_times.append(end - start)

    for i in range(len(total_times) - 1):
        tmp += total_times[i]
    avg_time = tmp / len(total_times)

    for i in range(len(total_times) - 1):
        all_times += f"run #{i + 1}: {total_times[i]:6f}\n"

    return (f"average time: {avg_time:6f}", f"{all_times}")


def main(args: list[str]) -> None:
    interpreter = ""
    prog = ""
    log = False
    clear_log = False
    help_ = False
    runs = 10
    exe_with_args = ""

    if len(args) < 2:
        print("too few arguments.")
        print("try 'time-it -h' for more information")
        exit(-1)

    for arg in args:
        if "./" in arg:
            prog = arg
        match arg:
            case "-h" | "--help":
                help_ = True
            case "-l" | "--log":
                log = True
            case "-i" | "--interpreter":
                interpreter = args[args.index(arg) + 1]
                prog = args[args.index(arg) + 2]
            case "-cl" | "--clear-log":
                clear_log = True
            case "-r" | "--runs":
                if args[args.index(arg) + 1].isdigit():
                    runs = int(args[args.index(arg) + 1])

    if help_:
        print_help_and_exit(1)

    if clear_log:
        try:
            with open(home / ".config" / "time-it.log", "w") as f:
                f.write("")
        except FileNotFoundError:
            print("no logs to wipe")

        exit(1)

    if interpreter != "":
        exe_with_args += f"{interpreter}"
    exe_with_args += f" {prog}"
    for arg in args[args.index(prog)::]:
        exe_with_args += f" {arg}"

    result = time_it(exe_with_args, runs)

    if log:
        try:
            with open(home / ".config" / "time-it.log", "a") as out:
                out.write(f"times for {args[1]} on {datetime.today().strftime("%Y-%m-%d %H:%M:%s")}\n")
                out.write(f"{result[0]}\n")
                out.write(f"{result[1]}\n")
        except FileNotFoundError:
            with open(home / ".config" / "time-it.log", "x") as out:
                out.write(f"times for {args[1]} on {datetime.today().strftime("%Y-%m-%d %H:%M:%s")}\n")
                out.write(f"{result[0]}\n")
                out.write(f"{result[1]}\n")

    print(result[0])
    print(result[1])


if __name__ == "__main__":
    main(sys.argv)
