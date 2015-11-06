SRC=deal2lkit

REV=`cd $SRC; git branch -v | grep \* | awk '{print $3}'`

if [ ! -d $SRC/build ]; then
    mkdir $SRC/build
    fi

    cd $SRC/build
    DST_INST=$OPT_INST/$SRC-dev

    cmake \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
    ..

    ninja -j$NP install
    # ctest -j40 -V -S ../tests/run_testsuite.cmake 
