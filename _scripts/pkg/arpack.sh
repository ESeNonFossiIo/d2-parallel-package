SRC=arpack-ng

REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

cd $SRC
DST_INST=$OPT_INST/$SRC-$REV

./configure \
  --prefix=$DST_INST \
  --enable-mpi 

make -j$NP install
