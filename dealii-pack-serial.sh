SRC=dealii

REV=`cd $SRC; git branch -v | grep \* | awk '{print $3}'`

export CC=`which cc`
export CXX=`which c++`

if [ ! -d $SRC/build-pack-serial ]; then
    mkdir $SRC/build-pack-serial
fi

cd $SRC/build-pack-serial
DST_INST=${OPT_INST/opt/}

cmake \
-GNinja \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
-DDEAL_II_COMPONENT_PACKAGE:BOOL=ON \
..

ninja -j$NP package
# ninja -j$NP setup_tests
# ctest -j$NP -V -S ../tests/run_testsuite.cmake 
