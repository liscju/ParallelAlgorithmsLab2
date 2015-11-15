__author__ = 'liscju'

import random
import sys

from mpi4py import MPI

from calculations import Star, calculate_forces, calculate_force

STAR_MASS_RANGE = (0, 50)
STAR_COORDS_RANGE = (0, 100)


def usage():
    print "Usage:"
    print "seq N"
    exit(-1)


def create_stars(count):
    stars = set()
    for i in range(0, count):
        mass = random.uniform(STAR_MASS_RANGE[0], STAR_MASS_RANGE[1])
        coord_x = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        coord_y = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        coord_z = random.uniform(STAR_COORDS_RANGE[0], STAR_COORDS_RANGE[1])
        stars.add(Star(i, mass, (coord_x, coord_y, coord_z)))
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
    list_ = list(list_)
    return [set(list_[start::n]) for start in range(n)]


def _initialize_master(comm, n, p):
    stars = create_stars(n)
    chunks = divide_list_to_chunks(stars, p)
    _send_to_slaves_portions(comm, chunks[1:])
    return chunks[0]


def run_master_proc(comm, n, p):
    chunk = _initialize_master(comm, n, p)
    run_main_parallel_algorithm(comm, 0, n, p, chunk)


def _initialize_slave(comm):
    return comm.recv(source=0)


def run_slave_proc(comm, rank, n, p):
    chunk = _initialize_slave(comm)
    run_main_parallel_algorithm(comm, rank, n, p, chunk)


def _calculate_send_recv_rank_index(rank, p):
    """ Calculate send and recv proc for given rank
        Returns (recv_rank, send_rank)
    """
    if rank == 0:
        return p - 1, 1
    elif rank == p - 1:
        return p - 2, 0
    else:
        return rank - 1, rank + 1


def run_main_parallel_algorithm(comm, rank, n, p, my_chunk):
    print "Run main parallel with rank=", rank, "n=", n, "p=", p, \
        "chunks=", [star.id for star in my_chunk]

    forces = calculate_forces(my_chunk)
    chunk_to_send = my_chunk

    recv_rank, send_rank = _calculate_send_recv_rank_index(rank, p)

    for _ in range(p - 1):
        comm.send(chunk_to_send, dest=send_rank)
        recv_chunk = comm.recv(source=recv_rank)

        print "Process rank=", rank, "received chunk=", \
            [star.id for star in recv_chunk]

        for star in my_chunk:
            star_current_force = forces[star.id]
            star_update_force = calculate_force(star, recv_chunk)
            forces[star.id] = (star_current_force[0] + star_update_force[0],
                               star_current_force[1] + star_update_force[1],
                               star_current_force[2] + star_update_force[2])
        chunk_to_send = recv_chunk

    print "Process rank=", rank, "calculated force=", forces


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
