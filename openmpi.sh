REV=1.10.2
SRC=openmpi-$REV

if [ ! -d $SRC ]; then 
    wget http://www.open-mpi.de/software/ompi/v1.10/downloads/$SRC.tar.gz 
    tar xvfz $SRC.tar.gz
fi

unset CC
unset CXX
export FC=`which gfortran`
unset F77
unset F90

DST_INST=$OPT_INST/$SRC

cd $SRC
make clean
./configure --prefix=$DST_INST

make -j$NP
make install
