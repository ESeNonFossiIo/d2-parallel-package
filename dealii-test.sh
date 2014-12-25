SRC=dealii

REV=`cd $SRC; git branch -v | grep \* | awk '{print $3}'`

if [ ! -d $SRC/build-$REV ]; then
    mkdir $SRC/build-$REV
fi

cd $SRC/build-test-$REV
DST_INST=$MATHLAB/$SRC-$REV

cmake \
-GNinja \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
..

ctest -j$NP -V -S ../tests/run_testsuite.cmake 
