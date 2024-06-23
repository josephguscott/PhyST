# Runs lvb on simulated MSAs

date
time python3 src/main.py --msa simulated_matrix_100x1000_phylip.phy --init-software lvb --parallel 50
echo "EXIT STATUS: $?"
date
