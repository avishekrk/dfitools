def makemutscript(mutationset,
                  resid='GNCA_resid', 
                  mutationtype='TEM1_Res',
                  pdbfile='1btl.pdb',
                  outfile='test.pdb'):
    """
    Outputs a PyMOL scripts for making mutations
    on a protein.
    
    mutationset: df
        Dataframe with the three-letter amino acid code
        of the protein, residue-index and three-letter
        amino acid code of the mutation
    resid: str
        columns name that contains the residue-index
    mutationtype: str 
        column that contains the three-letter amino 
        acid code for the mutation to make
    outfile: str
        name of outfile
    """
    
    begin="""
        load /tmp/{}
        """.format(pdbfile)
    print(begin) 
    for index, row in mutationset.iterrows():
        selection = '%d/'%(row[resid])
        mutations = row['TEM1_Res']
          
        script="""
        wizard mutagenesis 
        refresh_wizard 
        selection=\'%s\'
        mutation =\'%s\'
        cmd.get_wizard().do_select(selection)
        cmd.get_wizard().set_mode(mutation)
        cmd.get_wizard().apply()
        cmd.set_wizard()
        """%(selection,mutations)
        print (script) 
   
    lastpart="""
        cmd.save("{}")
        """.format(outfile)
    print(lastpart)
