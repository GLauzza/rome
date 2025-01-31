#!/bin/bash 

#OAR -q production 
#OAR -p grappe
#OAR -l host=1
#OAR -l walltime=0:05:00

module load conda
# conda env create -f environment.yml
# conda activate rome
python3 oar.py