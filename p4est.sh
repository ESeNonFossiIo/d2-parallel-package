SRC=p4est

REV=`cd $SRC; git branch -v | head -n 1 | awk '{print $3}'`

cd $SRC
DST_INST=$OPT_INST/$SRC-$REV

./configure \
  --prefix=$DST_INST \
  --enable-mpi \
  --without-blas \
  --disable-vtk-binary \
  --without-lapack 
make -j$NP install
