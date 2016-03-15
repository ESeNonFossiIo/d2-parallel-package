REV=2.0
SRC=gsl-$REV

if [ ! -d $SRC ]; then 
    wget http://ftp.gnu.org/gnu/gsl/$SRC.tar.gz
    tar xvfz $SRC.tar.gz
fi

DST_INST=$OPT_INST/$SRC

cd $SRC
make clean
./configure --prefix=$DST_INST 

make -j$NP
make install
