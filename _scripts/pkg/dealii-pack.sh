SRC=dealii

REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

if [ ! -d $SRC/build-pack$1 ]; then
    mkdir $SRC/build-pack$1
fi

cd $SRC/build-pack$1
DST_INST=${OPT_INST/opt/}

cmake \
-GNinja \
-DDEAL_II_CPACK_EXTERNAL_LIBS_TREE:PATH=$OPT_INST \
-DCMAKE_INSTALL_PREFIX:PATH=$DST_INST \
-DDEAL_II_COMPONENT_PACKAGE:BOOL=ON \
..

ninja -j$NP package
# ninja -j$NP setup_tests
# ctest -j$NP -V -S ../tests/run_testsuite.cmake 
