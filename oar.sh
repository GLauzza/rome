#!/bin/bash 

#OAR -q production 
#OAR -p grappe
#OAR -n Evaluate ModelEdit
#OAR -l host=1, walltime=50
#OAR -O ./OAR_logs/OAR_%jobid%.out
#OAR -E ./OAR_logs/OAR_%jobid%.errv

export PATH=/home/glauzzana/miniconda3/bin:$PATH

conda activate rome
for i in $(seq 0 29)
do
    python3 -m experiments.evaluate --alg_name="ModelEdit" --model_name="Qwen/Qwen2.5-0.5B" --hparams_fname="Qwen_Qwen2.5-0.5B_$i.json" --dataset_size_limit=50
done