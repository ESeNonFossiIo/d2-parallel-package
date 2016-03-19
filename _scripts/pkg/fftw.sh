SRC=fftw-3.3.4
REV=3.3.4

if [ ! -d $SRC ]; then 
    wget http://www.fftw.org/$SRC.tar.gz
    tar xvfz $SRC.tar.gz
fi

DST_INST=$OPT_INST/$SRC

cd $SRC
make clean
./configure --prefix=$DST_INST \
    --enable-mpi \
    --enable-threads \
    --enable-shared

make -j$NP
make install
