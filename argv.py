# argv.py
import sys


try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <string1 string2 ... stringn>")
print(arg[::-1])

# sys.argv is a global variable but be careful not to change it in a long program.
# args = sys.argv[1:] # Use this to preserve original values and avoid programs.
# sys.argv.pop() 
print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")
print(f"The first argument reversed : {sys.argv[1][::-1]}")