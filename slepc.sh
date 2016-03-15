SRC=slepc

REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

unset SLEPC_DIR

cd $SRC
DST_INST=$OPT_INST/$SRC-$REV

./configure --prefix=$DST_INST
make SLEPC_DIR=`pwd` 
make SLEPC_DIR=`pwd` install
make SLEPC_DIR=$DST_INST test
