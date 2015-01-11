SRC=aspect

REV=`cd $SRC; git branch -v | head -n 1 | awk '{print $3}'`

if [ ! -d $SRC/build-$REV ]; then
    mkdir $SRC/build-$REV
fi

cd $SRC/build-$REV
DST_INST=$OPT_INST/$SRC-$REV

cmake \
-GNinja \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
..

ninja -j$NP
# ninja -j40 setup_tests
# ctest -j40 -V -S ../tests/run_testsuite.cmake 
