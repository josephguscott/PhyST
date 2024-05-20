# Written by David Bunn, 2024 (modified from mpboot.py)
# Generates LVB command for Maximum Parsimony stage
import re

def GenerateLVBCommand(initial_software: str, msa_path: str) -> str:
    software_path = f'{initial_software} '
    pass_msa_path = "-i " + msa_path

    file_extension = re.search(".(\w+)\Z", msa_path)
    formats = {'phy':'phylip','ph':'phylip','phylip':'phylip',
               'fa':'fasta','fasta':'fasta',
               'nex':'nexus','nxs':'nexus','nexus':'nexus',
               'aln':'clustal','clustal':'clustal'}
    if file_extension:
        msa_format = formats[file_extension[1].lower()]
        print(msa_format.upper() + ' format detected.')
    else: msa_format = 'phylip'

    command = software_path + pass_msa_path + ' -f ' + msa_format
    
    return command
