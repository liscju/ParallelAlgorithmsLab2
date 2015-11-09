__author__ = 'liscju'

import sys


def usage():
    print "Usage:"
    print "seq N"
    exit(-1)


def run_simulation(args):
    if args[0] == "seq":
        if len(args) != 2:
            usage()

        n = args[1]

        print "Run sequence simulation with n=", n
    else:
        usage()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    run_simulation(sys.argv[1:])
