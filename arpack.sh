SRC=arpack-ng

REV=`cd $SRC; git branch -v | head -n 1 | awk '{print $3}'`

cd $SRC
DST_INST=$OPT_INST/$SRC-$REV

./configure \
  --prefix=$DST_INST \
  --enable-mpi 

make -j$NP install
