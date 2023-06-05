import linecache

class TreeScores:
    def __init__(self) -> None:
        pass

    def GetBestTreeScores(self, msa_path):
        # needs refactoring
        file = msa_path
        file = file + ".log"
        
        all_trees = []
        all_scores = []
        best_scores = []

        with open(file, "r") as fp:
            # for line in self.lines_that_start_with("Tree ", fp):
            for line in fp: 
                if line.startswith("Tree "):
                    all_trees.append(line)
                    score = line.split()
                    all_scores.append(score[-1]) 

        all_scores.sort()

        for i in range(5):
            best_scores.append(all_scores[i])

        return best_scores

    def GetBestTreesNumber(self, msa_path, best_scores):
        # needs refactoring
        file = msa_path
        file = file + ".log"

        best_trees = []
        best_trees_number = []

        with open(file, "r") as fp:
            lines = fp.readlines()
            for i in range(5):
                for line in lines:
                    if line.startswith("Tree "):
                        if best_scores[i] in line:
                            best_trees.append(line)
                            tree_number = line.split()
                            best_trees_number.append(tree_number[1])
                            lines.remove(line) # stops the same tree being repeatedly added
                            break # stops extra trees being assigned on last loop

        return best_trees_number

    def GetBestTrees(self, best_trees_number):
        # needs refactoring
        file = "parsimony.treefile"

        line_numbers = []
        lines = []

        for i in range(5):
            line_numbers.append(int(best_trees_number[i]))
        
        for i in line_numbers:
            x = linecache.getline(file, i).strip()
            lines.append(x)

        with open('parsimony.treefile_best_all', 'w') as fp:
            for i in lines:
                fp.write("%s\n" % i)

        for i in range(5):
            j = str(i + 1)
            file_name = "parsimony.treefile_best_"
            file_name = file_name + j

            with open(file_name, 'w') as fp:
                fp.write("%s\n" % lines[i])