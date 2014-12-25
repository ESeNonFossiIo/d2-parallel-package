SRC=dealii

REV=`cd $SRC; git branch -v | grep \* | awk '{print $3}'`

if [ ! -d $SRC/build-$REV ]; then
    mkdir $SRC/build-$REV
fi

cd $SRC/build-$REV
DST_INST=$MATHLAB/$SRC-$REV

cmake \
-GNinja \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
..

ninja -j$NP install
# ninja -j$NP setup_tests
# ctest -j$NP -V -S ../tests/run_testsuite.cmake 
