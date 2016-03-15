SRC=pfft
REV=`cd $SRC; git show-ref --hash --abbrev HEAD`

DST_INST=$OPT_INST/$SRC-$REV

cd $SRC
make clean
./configure --prefix=$DST_INST \
    --with-fftw3=$FFTW_DIR \
    --disable-shared

make -j$NP
make install
