Environment Variables Used
==========================

- OPT_INST: Where to install optional libraries
- NP: Number of available processors to compile
- MPI_HOME: home of mpi directory
- MKLROOT: home of MKL

It is expected that the following variables are picked up, and that 
all libraries are compiled with the same compilers:

- CC: current c compiler
- CXX: current c++ compiler
- FC: current fortran compiler
- F77: current fortran77 compiler
- F90: current fortran90 compiler

OpenMPI modules on most clusters export these to mpicc, mpic++, etc. Make
sure it happens on your configuration too...
