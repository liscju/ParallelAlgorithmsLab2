__author__ = 'liscju'

import random
import sys

from mpi4py import MPI

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
        stars.append(Star(i, mass, (coord_x, coord_y, coord_z)))
    return stars


def run_sequence_simulation(args):
    if len(args) != 1:
        usage()
    n = int(args[0])
    stars = create_stars(n)

    forces = calculate_forces(stars)
    print "Calculated forces: ", forces
    return forces


def _send_to_slaves_portions(comm, stars_chunks_to_send):
    for p, chunk in enumerate(stars_chunks_to_send, 1):
        comm.send(chunk, dest=p)


def divide_list_to_chunks(list_, n):
    return [list_[start::n] for start in range(n)]


def _initialize_master(comm, n, p):
    stars = create_stars(n)
    chunks = divide_list_to_chunks(stars, p)
    _send_to_slaves_portions(comm, chunks[1:])
    return chunks[0]


def run_master_proc(comm, n, p):
    chunk = _initialize_master(comm, n, p)


def _initialize_slave(comm):
    return comm.recv(source=0)


def run_slave_proc(comm, rank, n, p):
    chunk = _initialize_slave(comm)


def run_parallel_simulation(args):
    if len(args) != 1:
        usage()
    n = int(args[0])

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    p = comm.Get_size()


    if rank == 0:
        run_master_proc(comm, n, p)
    else:
        run_slave_proc(comm, rank, n, p)


def run_simulation(args):
    if args[0] == "seq":
        run_sequence_simulation(args[1:])
    elif args[0] == "par":
        run_parallel_simulation(args[1:])
    else:
        usage()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    run_simulation(sys.argv[1:])
