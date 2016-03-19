unset PETSC_DIR
unset PETSC_ARCH
unset CC
unset CXX
unset F77
unset FC

cd petsc
export PETSC_ARCH="uly"
export REV=`cd $SRC; git show-ref --hash --abbrev HEAD`
export EXT=/home/heltai/src/petsc-external

./configure \
  --with-make-np=40 \
  --with-debugging=0 \
  --prefix=$OPT_INST/petsc-$REV \
  --with-mpi-dir=$MPI_HOME \
  --with-shared-libraries \
  --with-external-packages-dir=$EXT \
  --with-blas-lapack-dir=$MKLROOT/lib/intel64 \
  --download-sowing=$EXT/sowing-1.1.16i.tar.gz \
  --download-parmetis=$EXT/parmetis-4.0.2-p5.tar.gz \
  --download-metis=$EXT/metis-5.0.2-p3.tar.gz \
  --download-hypre=$EXT/hypre-2.9.1a.tar.gz \
  --download-mumps=$EXT/MUMPS_4.10.0-p3.tar.gz \
  --download-scalapack=$EXT/scalapack-2.0.2.tgz \
  --download-sundials=$EXT/sundials-2.5.0p1.tar.gz \
  --download-superlu=$EXT/superlu_4.3.tar.gz \
  --download-superlu_dist=$EXT/superlu_dist_3.3.tar.gz \
  --download-hdf5=$EXT/hdf5-1.8.12.tar.gz 

make PETSC_DIR=`pwd` PETSC_ARCH=uly all
make PETSC_DIR=`pwd` PETSC_ARCH=uly install
make PETSC_DIR=$OPT_INST/petsc-$REV PETSC_ARCH= test
make PETSC_DIR=$OPT_INST/petsc-$REV PETSC_ARCH= streams NPMAX=20
