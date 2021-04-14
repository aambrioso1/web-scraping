# A program to demo command line arguments in Python from:
# https://realpython.com/python-command-line-arguments/

# main.py
import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>3}: {arg}")