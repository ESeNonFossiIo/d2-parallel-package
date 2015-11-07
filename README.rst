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

Order of installation
=====================

Copy in the directory $OPT_INST the file `external.conf`, and source it from 
your `.bashrc` or `.profile` (whichever is that your system uses).

If you already set MPI, then start with 

- petsc.sh

If you don't, then use 

- petsc-serial.sh

This will also download openmpi and attempt to configure it for you.

At every installation step, use a new terminal. This will ensure that `external.conf`
picks up all new libraries. Next step is 

- slepc.sh

The following can all be done in parallel:

- sundials.sh
- trilinos.sh
- oce.sh
- arpack.sh
- p4est.sh
- assimp.sh

Start another terminal. Then proceed with 

- dealii.sh
- deal2lkit.sh

If everything went well, then you should have in `summary.log` of deal.II and deal2lkit
almost all external libraries enabled.

Sundials has to be downloaded manually and extracted to the source directory.
