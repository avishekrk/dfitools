#!/bin/bash
#small script to run time series DFI 


for f in *_mwcovarmat.dat
do
    echo $f;
    prefix=$(echo $f | sed "s/_mwcovarmat.dat//g")
    echo $prefix
    ~/dfi/dfi.py --pdb bpti.pdb --hess $f
    mv -v bpti-dfianalysis.csv ${prefix}-dfianalysis.csv 

done
