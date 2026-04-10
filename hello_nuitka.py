#!/usr/bin/env python3

# python -m nuitka --mode=onefile --static-libpython=yes hello_nuitka.py

def talk(message):
    return "Nuitka Talk " + message


def main():
    print(talk("Hello World"))


if __name__ == "__main__":
    main()

