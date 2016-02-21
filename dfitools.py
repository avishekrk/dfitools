#!/usr/bin/env python
"""
DFI Tools 
=========

Description
-----------
Suite of tools for DFI Analysis

"""

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
    
