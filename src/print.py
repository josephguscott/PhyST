class PhystPrint:
    def __init__(self) -> None:
        pass

    def printHeader():
        print("===============================")
        print("  PHYST Phylogenetic Pipeline  ")
        print("===============================")

        print("PHYST (v 1.0)")
        print("Developed by Joseph Guscott,")
        print("Barker Lab,")
        print("University of Edinburgh")
        print("Copyright (c) 2023 Joseph Guscott")

    def printSoftwareConfig(init_software, msa_path, init_tree_size, likelihood_software):
        print("===============================")
        print("PHYST configuration:")
        print("  Initial Trees")
        print("    Software:", init_software)
        print("    MSA:", msa_path)
        print("    Trees evaluated:", init_tree_size)
        print("    Trees retained: 5")
        print("")
        print("  Likelihood Analysis")
        print("    Software:", likelihood_software)
        print("")
        print("MPBoot provided by Hoang, et al., 2018; https://doi.org/10.1186/s12862-018-1131-3")
        print("IQ-Tree provided by Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015")
        print("===============================")
        print("")