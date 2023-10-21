
import time

class Print:
        physt_version = "1.0"

        def __init__(self, initial_software: str, msa_path: str, number_initial_trees: int, refinement_software: str, 
                     time_stamp: str, cores: int):
                self.initial_software = initial_software
                self.msa_path = msa_path
                self.number_initial_trees = number_initial_trees
                self.refinement_software = refinement_software
                self.time_stamp = time_stamp
                self.cores = cores

        def printStartup(self) -> None:
                self.__printHeader()
                self.__printSoftwareConfig()

        def __printHeader(self) -> None:
                print("===============================")
                print("  PHYST Phylogenetic Pipeline  ")
                print("===============================")

                print(f"PHYST ({self.physt_version})")
                print("Developed by Joseph Guscott,")
                print("Barker Lab,")
                print("School of Biological Science")
                print("University of Edinburgh")
                print("Copyright (c) 2023 Joseph Guscott")

        def __printSoftwareConfig(self) -> None:
                print("===============================")
                print("PHYST configuration:")
                print("  Initial Trees")
                print("    Software:", self.initial_software)
                print("    MSA:", self.msa_path)
                print("    Trees evaluated:", self.number_initial_trees)
                print("    Trees retained: 5")
                print("")
                print("  Likelihood Analysis")
                print("    Software:", self.refinement_software)
                print("")
                print("  Resources")
                print("    Cores:", self.cores)
                print("")
                print("Start time: ", self.time_stamp)
                print("")
                print("MPBoot provided by Hoang, et al., 2018; https://doi.org/10.1186/s12862-018-1131-3")
                print("IQ-Tree provided by Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015")
                print("===============================")
                print("")

        @staticmethod
        def printDictionary(dictionary: dict) -> None:
                for key in dictionary:
                        print (key,':',dictionary[key])

        @staticmethod
        def printRuntime(program_runtime) -> None:
                print("\nWall-clock time : ", time.strftime("%H:%M:%S", time.gmtime(program_runtime))) 