SRC=p4est

REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

cd $SRC
DST_INST=$OPT_INST/$SRC-$REV

autoconf 

git submodule init && git submodule update

./bootstrap

./configure \
  --prefix=$DST_INST \
  --enable-mpi \
  --without-blas \
  --disable-vtk-binary \
  --without-lapack 
make -j$NP install
