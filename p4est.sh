SRC=p4est

REV=`cd $SRC; git branch -v | head -n 1 | awk '{print $3}'`

cd $SRC
DST_INST=$MATHLAB/$SRC-$REV

./configure \
  --prefix=$DST_INST \
  --enable-mpi \
  --without-blas \
  --without-lapack 
make -j$NP install
