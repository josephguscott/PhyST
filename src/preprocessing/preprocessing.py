
from preprocessing.generate_initial_trees import GenerateInitialTrees, WriteInitialTrees
from preprocessing.filter_initial_trees import FilterInitialTrees

class Preprocessing:
    def __init__(self, INIT_TREE_SIZE: int, HARDWARE: int, INIT_SOFTWARE: str, MSA_PATH: str) -> None:
        self.INIT_TREE_SIZE = INIT_TREE_SIZE
        self.HARDWARE = HARDWARE
        self.INIT_SOFTWARE = INIT_SOFTWARE
        self.MSA_PATH = MSA_PATH

    def GenerateStartingTrees(self) -> None:
        print("Generating initial {} initial trees using {} cores".format(self.INIT_TREE_SIZE, self.HARDWARE))
        initial_trees = GenerateInitialTrees(self.INIT_SOFTWARE, self.MSA_PATH, self.INIT_TREE_SIZE, self.HARDWARE)
        WriteInitialTrees(initial_trees)

    def FilterStartingTrees(self) -> None:
        print("Obtaining the best {} initial trees".format("5"))
        FilterInitialTrees(self.MSA_PATH, self.HARDWARE)