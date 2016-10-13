#!/usr/bin/env python 
"""
Take Averages
-------------
./TakeAvg.py title 
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import dfi
import glob
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print __doc__
        exit()

    title = sys.argv[1]


    covar_files = glob.glob('*_mwcovarmat.dat')
    pdbfile = title+'.pdb'
    dfi_files = map(lambda x: x.replace('_mwcovarmat.dat','-dfianalysis.csv'),covar_files)
    
    for covarfname, dfifname in zip(covar_files,dfi_files):
        dfi.calc_dfi(pdbfile,covar=covarfname,writetofile=True,dfianalfile=dfifname)
    

    windows = map(lambda x: x.replace(title+'_','').replace('-dfianalysis.csv',''),dfi_files)
    data  = pd.concat([pd.read_csv(fname) for fname in dfi_files], keys=windows, names=['window'])
    dfx = pd.DataFrame()
    for win, df in data.groupby(level = 0):
        dfx[win] = df['pctdfi'].values


    def sort_windows(ls_windows):
        """
        Sort windows by numeric values. 
        
        Input
        -----
        ls_windows: ls
        List of window intervals
        
        Output
        ------
        ls_sorted_windows: ls
        Sorted window frames 
        """
        sort_dic = {}
        for win in ls_windows:
            start,end = win.split('_')
            start = int(start)
            end = int(end)
            sort_dic[start] = win 
        sorted_keys = np.sort(sort_dic.keys())
        return [sort_dic[key] for key in sorted_keys]


    dfx = dfx[ sort_windows( dfx.columns.tolist() ) ]


    dfx = dfx[ dfx.columns[-3:] ]


    first_window = windows[0]


    dfx['avg'] = dfx.mean(axis=1)



    dfx['R'] = data.loc[first_window].R.values
    dfx['ResI'] = data.loc[first_window].ResI.values


    dfx.to_csv(title+'-dfiavg.csv',index=False)


   
    dfx=dfx.set_index('ResI')




    sns.set_style("white")
    sns.set_context("poster", font_scale=2.25, rc={"lines.linewidth": 1.25,"lines.markersize":8})
    dfx[ dfx.columns.tolist()[:4] ].plot(figsize=(24,12),marker='o')
    plt.legend(bbox_to_anchor=(0., 1.005, 1., .102), loc=7,ncol=4, borderaxespad=0.)
    plt.ylabel('%DFI')
    plt.xlabel('Residue Index')
    plt.savefig(title+'-pctDFI.png')


# In[ ]:



