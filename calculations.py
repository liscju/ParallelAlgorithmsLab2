__author__ = 'liscju'

import math


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


def calculate_force(star, other_stars):
    result_force = (0, 0, 0)
    for other_star in other_stars:
        force = star.calculate_force(other_star)
        result_force = (result_force[0] + force[0],
                        result_force[1] + force[1],
                        result_force[2] + force[2])
    return result_force


def calculate_forces(stars):
    forces = []
    for i in range(0, len(stars)):
        others = stars[:i] + stars[(i+1):]
        forces.append(calculate_force(stars[i], others))


G = 6.67