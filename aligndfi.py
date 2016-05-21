

def aligndfi(pdbID):
    """
    Align DFI. Given a pdbID this function
    will return a dataframe of an aligned sequence. 
    """
   
    import dfi 
    import dfi.fastaseq
    import dfi.fasta_convert
    from clustalo import clustalo
    import numpy as np
    import pandas as pd
    remove_header = lambda x:''.join([s for s in x.split('\n') if not(s.startswith('>'))])    
    
    seqfasta=dfi.fastaseq.get_fastaseq(pdbID)
    #pdbseq=dfi.fasta_convert.fafsa_format(pdbID+'.pdb')
    pdbseq=dfi.fastaseq.get_fastaseq('P04062')

    pdb=remove_header(pdbseq)
    fasta=remove_header(seqfasta)
    input = {'pdbseq':pdb,'fastaseq':fasta}
    aligned = clustalo(input,seqtype=3)
 
    df_dfi = dfi.calc_dfi(pdbID+'.pdb')
    df_dfi['pctfdfi'] = len(df_dfi)*np.nan
    pctdfi = df_dfi['pctdfi']
    chainIDs = df_dfi['ChainID']
    ResIDs = df_dfi['ResI']
    pctfdfi = df_dfi['pctfdfi']
    
    df_aligned = pd.DataFrame()
    df_aligned['fastaseq'] = [s for s in aligned['fastaseq']]
    df_aligned['pdbseq'] = [s for s in aligned['pdbseq']]

    i = 0 
    align_pctdfi = []
    align_chain = []
    align_resi = []
    align_pctfdfi = []
    for site in df_aligned['pdbseq']:
        if i >= len(pctdfi):
            break 
        print 'site',site
    
        if site == '-':
            print np.nan
            align_pctdfi.append(np.nan)
            align_chain.append(np.nan)
            align_resi.append(np.nan)
            align_pctfdfi.append(np.nan)
        else:
            print pctdfi[i]
            align_pctdfi.append(pctdfi[i])
            align_chain.append(chainIDs[i])
            align_resi.append(int(ResIDs[i]))
            align_pctfdfi.append(pctfdfi[i])
            i += 1
    while len(align_pctdfi) < len(df_aligned['pdbseq']):
        print np.nan
        align_pctdfi.append(np.nan)
        align_chain.append(np.nan)
        align_resi.append(np.nan)
        align_pctfdfi.append(np.nan)

    print len(align_pctdfi), len(align_chain), len(align_resi)

    df_aligned['pctdfi'] = align_pctdfi
    df_aligned['ChainID'] = align_chain
    df_aligned['ResI'] = align_resi
    df_aligned['ind'] = range(1,len(align_pctdfi)+1)
    df_aligned['pctfdfi'] = align_pctfdfi
    df_aligned.to_csv(pdbID+'-dfialigned.csv')
