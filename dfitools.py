#!/usr/bin/env python
"""
DFI Tools 
=========

Description
-----------
Suite of tools for DFI Analysis

"""

def make_fafsta(name,df_dfi):
    """
    name: name of fasta index
    df_dfi: df of dfi profile
    must have sequence under 
    column R 
    """
    seq = ''.join(df_dfi.R.values)
    print ">%s"%name
    print seq
