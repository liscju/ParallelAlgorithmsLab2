__author__ = 'liscju'

import sys

STAR_MASS_RANGE = (0, 50)
STAR_COORDS_RANGE = (0, 100)


def usage():
    print "Usage:"
    print "seq N"
    exit(-1)


class Star(object):
    def __init__(self, mass, coord):
        self.mass = mass
        self.coord = coord

    def __repr__(self):
        return "{Star: mass=(" + repr(self.mass) + "), " + \
                "coord=" + repr(self.coord) + "}"


def create_stars(count):
    stars = []
    for i in range(0, count):
        stars.append(Star(0, (0, 0, 0)))
    return stars


def run_simulation(args):
    if args[0] == "seq":
        if len(args) != 2:
            usage()

        n = int(args[1])

        print "Run sequence simulation with n=", n
        stars = create_stars(n)
        for star in stars:
            print repr(star)
    else:
        usage()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    run_simulation(sys.argv[1:])
