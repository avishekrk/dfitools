#!/usr/bin/env python
"""
MakePDB
---------
title parm mdtraj
"""

import sys

def makepdb(title,parm,traj):
    """
    Make pdb file from first frame of a trajectory
    """
    cpptrajdic ={'title':title,'parm':parm,'traj':traj}
    cpptrajscript="""parm {parm}
    trajin {traj} 0 1 1
    center
    rms first @CA,C,N
    strip :WAT
    strip :Na+
    strip :Cl-
    trajout {title}.pdb pdb 
    run
    exit"""
    
    return cpptrajscript.format(**cpptrajdic)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print __doc__
        exit()
    title = sys.argv[1]
    parm = sys.argv[2]
    mdtrj = sys.argv[3]
    script = makepdb(title,parm,mdtrj)
    with open('getpdb.cpptraj','w') as outfile:
        print "Writing getpdb file"
        outfile.write(script)
    
