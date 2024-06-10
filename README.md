# PHYST

### Introduction

The **PHY**logenetic **S**tarting **T**ree (PHYST) pipeline uses popular phylogenetic software packages to pass optimised parsimony trees to likelihood software.

PHYST is currently under development at the University of Edinburgh.

Current developers:
- [Joseph Guscott](https://github.com/josephguscott)
- [Daniel Barker](https://www.ed.ac.uk/profile/daniel-barker)

## Getting Started

PHYST is not reliant on any external python packages, but does require Python3.11 to run.

Dependent on program selection, PHYST is currently reliant on MPBoot, LVB, TNT, EMBOSS and IQ-Tree binaries, which are available from:

- MPBoot: http://www.iqtree.org/mpboot/ 
- LVB: https://lvb.bio.ed.ac.uk/
- TNT: https://www.lillo.org.ar/phylogeny/tnt/
- EMBOSS (if TNT used): https://emboss.sourceforge.net/download/
- IQ-Tree: http://www.iqtree.org/

All binaries are required within the 'lib/' folder.

Currently, PHYST is ran using the following command:
~~~~
python3.11 src/main.py --msa <msa>
~~~~

### Command-line options

Specify the software used for the Maximum Parsimony stage:
~~~~
--init-software <software name>
~~~~
Options: mpboot (default), lvb, tnt

Run PHYST with more or few initial trees:
~~~~
--init-trees <num of trees>
~~~~ 

Parallelisation can be achived through either specifying how many cores should be used:
~~~~
--parallel <num of cores>
~~~~

or using maximum cores:
~~~~
--max-parallel
~~~~

If using TNT for the Maximum Parsimony stage, intensity of search (0-10) can be specified:
~~~~
--tnt-level <level>
~~~~
Level 0 is fastest and least accurate, level 10 is slowest and most accurate. Default level=1.

Command-line options can be passed directly to IQ-Tree through PHYST:
~~~
-iqtree-options '<options>'
~~~
With options to be passed enclosed by quotations.

# Credit
The script used for TNT searching, 'TNTsearch.run' is a modified version of the script 'PhylogenomicSearch.run' from the following paper:
Parsimony analysis of phylogenomic datasets (I): scripts and guidelines for using TNT. Ambrosio Torres, Pablo A. Goloboff and Santiago A. Catalano (Cladistics. 2022) [https://onlinelibrary.wiley.com/doi/epdf/10.1111/cla.12477?af=R]

# Licence
APACHE License v2 (January 2004)

# Contact
Please direct any questions about PHYST to Joseph Guscott joseph.guscott@ed.ac.uk or Daniel Barker at daniel.barker@ed.ac.uk