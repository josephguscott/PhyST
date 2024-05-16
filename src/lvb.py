# Written by David Bunn, 2024 (modified from mpboot.py)
# Generates LVB command for Maximum Parsimony stage

def GenerateLVBCommand(initial_software: str, msa_path: str) -> str:
    software_path = f'{initial_software} '
    pass_msa_path = "-i " + msa_path
    command = software_path + pass_msa_path

    return command
