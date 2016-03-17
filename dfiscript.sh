#!/bin/bash
#small script to run time series DFI 
#e.g., ./dfiscript.sh pdbid fdfiresidues 

if [ -z "${1}" ]
then
	echo "No input file";
	echo "./dfiscript pdbid fdfiresidues" 
	exit;
fi

pdbid=$1
file=${pdbid}.pdb
if [ -f "${file}" ]
then
	echo "Found the file $file"
else
	echo "Did not find the $file"
	exit 1 

fi 

fdfi="${@:2}"
echo $fdfi 



for f in *_mwcovarmat.dat
do
    #echo $f;
    prefix=$(echo $f | sed "s/_mwcovarmat.dat//g")
    #echo $prefix
    if [ -f ${prefix}-dfianalysis.csv ]
    then
	echo "${prefix}-dfianalysis.csv found" 
	continue 
    fi
    #check if the pctdfi file is already made 
    ~/dfi/dfi.py --pdb ${pdbid}.pdb --hess $f --fdfi ${fdfi}
    mv -v ${pdbid}-dfianalysis.csv ${prefix}-dfianalysis.csv 

done



~/dfi/dfi.py --pdb ${pdbid}.pdb --fdfi ${fdfi}
mv -v ${pdbid}-dfianalysis.csv ${pdbid}_ENM-dfianalysis.csv  
