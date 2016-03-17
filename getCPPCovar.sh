#!/bin/bash 
PROG=$(basename $0)

usage="
CPPCovar
========

Usage
-----
getCPPCovar.sh name starttime endtime 

Description
------------
Creates and Runs a cpptraj script to extract a
covariance matrix out of 0.parm.parm7 and lowest 
replica

"

#input check 
if [ "$#" -ne 3 ]; then
    echo "Number of arguements: $#"
    echo "$usage"
    exit 1 
fi

title=$1
start=$2
end=$3

echo "Input Parameters"
echo "----------------"
echo "title: $title"
echo "start: $start"
echo "end: $end"
echo " "

script="parm 0.prmtop.parm7
trajin 0.mdtrj.crd.gz $start $end 1
center
rms first @CA,C,N
matrix mwcovar name mwcovarmat @CA out ${title}_${start}_${end}_mwcovarmat.dat
run
quit
"

echo "CPPTRAJ script"
echo "--------------"
echo "$script"

echo "$script" > ${title}_${start}_${end}_covar.cpptraj 

echo "Wrote out to: ${title}_${start}_${end}_covar.cpptraj"
echo "Running script"

cpptraj -i ${title}_${start}_${end}_covar.cpptraj
