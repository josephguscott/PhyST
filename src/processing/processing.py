
from processing.refine_trees import RefineInitialTrees

class Processing:
    def __init__(self, HARDWARE: str, MSA_PATH: str, IQ_TREE_OPTIONS) -> None:
        self.HARDWARE = HARDWARE
        self.MSA_PATH = MSA_PATH
        self.IQ_TREE_OPTIONS = IQ_TREE_OPTIONS

    def RefineStartingTrees(self) -> None:
        RefineInitialTrees(self.MSA_PATH, self.HARDWARE, self.IQ_TREE_OPTIONS)