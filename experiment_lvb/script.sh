# Runs lvb-physt on simulated MSAs

date
time python3 src/main.py --msa ../sim_trees/alignment_$1_$2_$3_$4.phy --init-software lvb --parallel 50
echo "EXIT STATUS: $?"
date
