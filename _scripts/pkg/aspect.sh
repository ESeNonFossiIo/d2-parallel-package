SRC=aspect

REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

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
