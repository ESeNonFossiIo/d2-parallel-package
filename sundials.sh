REV=2.6.2
SRC=sundials-$REV

# REV=`cd $SRC; git branch -v | grep \* | awk '{print $3}'`

if [ ! -d $SRC/build-$REV ]; then
    mkdir $SRC/build-$REV
fi

cd $SRC/build-$REV
DST_INST=$OPT_INST/$SRC-$REV

cmake \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
-DLAPACK_ENABLE:BOOL=ON \
-DMPI_ENABLE:BOOL=ON \
-DPTHREAD_ENABLE:BOOL=ON \
..

make -j$NP install
# ninja -j$NP setup_tests
# ctest -j$NP -V -S ../tests/run_testsuite.cmake 
