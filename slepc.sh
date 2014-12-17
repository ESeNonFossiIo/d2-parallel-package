SRC=slepc

REV=`cd $SRC; git branch -v | awk '{print $3}'`

unset SLEPC_DIR

cd $SRC
DST_INST=$MATHLAB/$SRC-$REV

./configure --prefix=$DST_INST
make SLEPC_DIR=`pwd` 
make SLEPC_DIR=`pwd` install
make SLEPC_DIR=$DST_INST test
