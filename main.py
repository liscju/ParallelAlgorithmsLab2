__author__ = 'liscju'

import math
import random
import sys

G = 6.67

STAR_MASS_RANGE = (0, 50)
STAR_COORDS_RANGE = (0, 100)


def usage():
    print "Usage:"
    print "seq N"
    exit(-1)


def vectors_distance(v1, v2):
    return math.sqrt(sum([(v2[i]-v1[i])**2 for i in range(0, 3)]))


class Star(object):
    def __init__(self, mass, coord):
        self.mass = mass
        self.coord = coord

    def __repr__(self):
        return "{Star: mass=(" + repr(self.mass) + "), " + \
                "coord=" + repr(self.coord) + "}"

    def x(self):
        return self.coord[0]

    def y(self):
        return self.coord[1]

    def z(self):
        return self.coord[2]

    def calculate_force(self, star):
        acceleration = self._calculate_acceleration(star)
        return (self.mass * acceleration[0],
                self.mass * acceleration[1],
                self.mass * acceleration[2])

    def _calculate_acceleration(self, star):
        return (G * (star.mass / (vectors_distance(star.coord, self.coord)**3)) *
                    (star.x() - self.x()),
                G * (star.mass / (vectors_distance(star.coord, self.coord)**3)) *
                    (star.y() - self.y()),
                G * (star.mass / (vectors_distance(star.coord, self.coord)**3)) *
                    (star.z() - self.z()))


def create_stars(count):
    stars = []
    for i in range(0, count):
        mass = random.uniform(STAR_MASS_RANGE[0], STAR_MASS_RANGE[1])
        coord_x = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        coord_y = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        coord_z = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        stars.append(Star(mass, (coord_x, coord_y, coord_z)))
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
