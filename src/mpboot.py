def generateMPBootCommand(initial_software: str, msa_path: str) -> str:
        software_path = "./lib/{} ".format(initial_software)
        pass_msa_path = "-s " + msa_path       
        command = software_path + pass_msa_path
        command = command + " > /dev/null 2>&1"

        return command