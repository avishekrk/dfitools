#!/usr/bin/env python 
"""
Makecpptraj
===========

Usage
-----
./makecpptraj.py title trajlen interval parm traj 

"""
import sys 


def getwindow(trajlen,interval=2000):
    i = trajlen
    timewindows=[]
    while i > 0:
        timewindows.append(i)
        i = i - interval 
    timewindows.append(0)
    return timewindows[::-1]

def makecpptrajscript(title,start,end,parm="0.prmtop.parm7",traj="0.mdtrj.crd.gz"):
    cpptrajdic={'title':title, 'start':start, 'end':end, 'parm':parm, 'traj':traj}
    cppscript="""
    parm {parm}
    trajin {traj} {start} {end} 1
    center
    rms first @CA,C,N
    matrix mwcovar name mwcovarmat @CA out {title}_{start}_{end}_mwcovarmat.dat
    analyze matrix mwcovarmat name evecs out {title}_{start}_{end}_evecs.dat vecs 30 
    run
    quit
    """
    return cppscript.format(**cpptrajdic)


def outputcpptrajscript(title,trajlen,interval=2000,parm="0.prmtop.parm7",traj="0.mdtrj.crd.gz"):
    trajcuts = getwindow(trajlen,interval=interval)
    for i in range(len(trajcuts)):
        if i+1 >= len(trajcuts):
            break
        fname="{title}_{start}_{end}.cpptraj".format(title=title,start=trajcuts[i],end=trajcuts[i+1])
        with open(fname,'w') as outfile:
            print "Writing out to:",fname
            outfile.write( makecpptrajscript(title,trajcuts[i], trajcuts[i+1],parm,traj) )

if __name__ == "__main__":

    if(len(sys.argv)) < 2:
        print __doc__
        sys.exit()
    
    title=sys.argv[1]
    trajlen=int(sys.argv[2])
    interval=int(sys.argv[3]) 

    if(len(sys.argv)) > 4:
        parm = sys.argv[4]
        traj = sys.argv[5]
        outputcpptrajscript(title,trajlen,interval,parm,traj)
    else:
        outputcpptrajscript(title,trajlen,interval)

