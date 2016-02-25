#!/usr/bin/env python
"""
DFI Tools 
=========

Description
-----------
Suite of tools for DFI Analysis

"""
import pandas as pd 
import glob 
import numpy as np 

def make_fasta(name,df_dfi):
    """
    name: name of fasta index
    df_dfi: df of dfi profile
    must have sequence under 
    column R 
    """
    import textwrap
    seq = ''.join(df_dfi.R.values)
    nameline=">%s\n"%name
    seqline = textwrap.fill(seq,80)
    return nameline+seqline 
    
def glob_df(pdbid,parm,chainA=False):
    "Take a bunch of dataframe and combine them"
    csvfiles = glob.glob(pdbid+'*.csv')
    titles = map(lambda x: x.replace(pdbid+'_','').replace('-dfianalysis.csv',''),csvfiles)
    data = pd.concat( [pd.read_csv(fname, index_col='ResI') for fname in csvfiles], keys=titles, names=['window','ResI'])
    if chainA:
        data = data[data.ChainID=='A']
    df_windows = pd.DataFrame()
    for win, df_dfi in data.groupby(level=0):
        df_windows[win] = df_dfi.reset_index().set_index('ResI')[parm]
    return df_windows 

def getavg(df_windows,pdbid):
    "get the average of all frames execpt ENM"
    df_windows = glob_df(pdbid,'pctdfi')
    cols = [col for col in df_windows.columns if not(col == "ENM")]
    df_windows['md_avg'] = df_windows[cols].mean(axis=1)    
    df_windows['md_std'] = df_windows[cols].var(axis=1).map(np.sqrt)
    return df_windows 

def calc_avg(pdbid,parm):
    "grab all dataframes avg them and output the outfile"
    df_windows = glob_df(pdbid,parm,chainA=False)
    df_windows = getavg(df_windows,pdbid)
    outfile = '_'.join([pdbid,parm,'avg-dfianalysis.csv'])
    df_windows.to_csv(outfile)
    print "Wrote out to %s"%(outfilename)