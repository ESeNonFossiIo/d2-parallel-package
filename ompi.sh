SRC=ompi

unset CXX
unset CC
unset F77
unset FC

REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

if [ ! -d $SRC/build-$REV ]; then
    mkdir $SRC/build-$REV
fi

cd $SRC/build-$REV
DST_INST=$OPT_INST/$SRC-$REV

cmake \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
..

make -j$NP install
# ninja -j$NP setup_tests
# ctest -j$NP -V -S ../tests/run_testsuite.cmake 
