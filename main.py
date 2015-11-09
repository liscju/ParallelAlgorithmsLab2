__author__ = 'liscju'

import random
import sys

from calculations import Star, calculate_forces


STAR_MASS_RANGE = (0, 50)
STAR_COORDS_RANGE = (0, 100)


def usage():
    print "Usage:"
    print "seq N"
    exit(-1)


def create_stars(count):
    stars = []
    for i in range(0, count):
        mass = random.uniform(STAR_MASS_RANGE[0], STAR_MASS_RANGE[1])
        coord_x = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        coord_y = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        coord_z = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        stars.append(Star(mass, (coord_x, coord_y, coord_z)))
    return stars


def run_sequence_simulation(args):
    if len(args) != 1:
        usage()
    n = int(args[0])
    print "Run sequence simulation with n=", n
    stars = create_stars(n)
    for star in stars:
        print repr(star)

    forces = calculate_forces(stars)
    print "Calculated forces: ", forces
    return forces


def run_simulation(args):
    if args[0] == "seq":
        run_sequence_simulation(args[1:])
    else:
        usage()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    run_simulation(sys.argv[1:])
