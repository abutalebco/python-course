import sys
import getopt

# Usage: arg_parse.py -f [FILENAME] -m [MESSAGE]

filename = "test.txt"
message = "MEOW"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

try:
    with open(filename, 'w+') as f:
        f.write(message)
    print(f"Text {message} Added to the file {filename}") # Text MEOW Added to the file test.txt
except SystemError as e:
    print(e)


def arg(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(kwargs["ONE"])
    print(kwargs["TWO"])
    return "Arguments processed"

print(arg(True, "python", 99, ONE=1, TWO=2))

# Usage: arg_parse.py [ARGUMENT]

print(sys.argv) # ['arg_parse.py', 'Hello', 'What Are You Doing']


# Usage: arg_parse.py [FILENAME] [ARGUMENT]

fn = sys.argv[1]
ctx = sys.argv[2]

with open(fn, 'w+') as f:
    f.write(ctx)

"""
Challenge: how to write multiple words in an argument?
E.g. What Are You Doing
"""