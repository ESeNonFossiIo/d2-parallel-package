SRC=p4est

REV=`cd $SRC; git branch -v | awk '{print $3}'`

cd $SRC
DST_INST=$MATHLAB/$SRC-$REV

./configure \
  --prefix=$DST_INST \
  --enable-mpi \
  --without-blas \
  --without-lapack 
make -j12 install
