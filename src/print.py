def printPHYSTHeader():
    print("===============================")
    print("  PHYST Phylogenetic Pipeline  ")
    print("===============================")

    print("PHYST version 1.0 built for Linux 64-bit")
    print("Developed by Joseph Guscott,")
    print("Barker Lab,")
    print("University of Edinburgh")
    print("Copyright (c) 2023 Joseph Guscott")
    print("")
    
def printCommandLineOptionsTreeEvaluation(args):
    print("Tree Evaluation Options: ")
    print("  Alignment file: %s" % args.msa)
    print("  Starting treefile %s" % args.treefile)

    if args.seed is not None:
        print("  Seed: %i" % args.seed)

    print("\nTree evaluations carried out using IQ-Tree (Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015\n")
