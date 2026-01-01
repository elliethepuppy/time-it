#!/usr/bin/python

import time
import subprocess
import sys
from datetime import datetime
from pathlib import Path

home = Path.home()

def time_it(exe: str, times: int = 10) -> tuple[str, str]:
    total_times: list[float] = []
    all_times: str = ""
    avg_time: float = 0.0
    tmp: float = 0.0

    for i in range(times):
        start = time.time()
        subprocess.run([exe])
        end = time.time()
        total_times.append(end - start)

    for i in range(len(total_times) - 1):
        tmp += total_times[i]
    avg_time = tmp / len(total_times)

    for i in range(len(total_times) - 1):
        all_times += f"run #{i + 1}: {total_times[i]:6f}\n"

    return (f"average time: {avg_time:6f}", f"{all_times}")


def main(args: list[str]) -> None:
    log = False
    if len(args) < 2:
        print("too few arguments.")
        print("try 'time-it ./[executable in this directory] [optional number of times]'")
        exit(-1)


    if "./" not in args[1]:
        if args[1] == "-h" or args[1] == "--help":
            print("time-it: a simple executable timer")
            print(
                "usage: place time-it in the same directory as the",
                "executable you wish to time, then call:"
            )
            print("'./time-it ./[executable you wish to time] [optional number of runs] [optional logging flag]")
            print(
                "NOTE: if timing a script, you should place a shebang operator",
                "at the top of your script for the interpreter you intend to use,",
                "then mark it as executable.\n"
            )
            print("ex. for bash: #!/usr/bin/bash")
            exit(1)

        if args[1] == "-cl" or args[1] == "--clear-log":
            try:
                with open(home / ".config" / "time-it.log", "w") as f:
                    f.write("")
            except FileNotFoundError:
                print("no logs to wipe")

            exit(1)

        print(f"{args[1]} is not an executable in this directory")
        print(f"try 'time-it ./{args[1]}'")
        exit(-1)
    elif len(args) == 2:
        result = time_it(args[1])
    elif len(args) > 2:
        if "-l" in args[2::]:
            log = True
        if "--log" in args[2::]:
            log = True
        if args[2].isdigit():
            result = time_it(args[1], int(args[2]))
        else:
            result = time_it(args[1])

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
