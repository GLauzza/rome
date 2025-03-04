#!/bin/bash 
#OAR -q production
#OAR -n Evaluate ModelEdit
#OAR -l host=1/gpu=1, walltime=1
#OAR -O ./OAR_logs/OAR_%jobid%.out
#OAR -E ./OAR_logs/OAR_%jobid%.out

export PATH=/home/glauzzana/miniconda3/bin:$PATH

conda activate rome

# python ./gguf_to_hf.py

module load cuda/12.1.1_gcc-10.4.0    
nvcc --version
which nvcc
export CUDA_PATH=/grid5000/spack/v1/opt/spack/linux-debian11-x86_64_v2/gcc-10.4.0/cuda-12.1.1-fz46ojsingbat72bebi2smmc45vigivi/bin/nvcc
module load gcc/10.4.0_gcc-10.4.0
nvidia-smi

# python3 -m experiments.evaluate --dataset_size_limit=50 --alg_name="ModelEdit" --model_name="Qwen/Qwen2.5-0.5B" --hparams_fname="Qwen_Qwen2.5-0.5B.json" --skip_generation_tests

for i in $(seq 616 639) 
do
    mkdir ./results/ModelEdit/run_$i
    python3 -m experiments.evaluate --dataset_size_limit=10 --alg_name="ModelEdit" --model_name="Qwen/Qwen2.5-0.5B" --hparams_fname="Qwen_Qwen2.5-0.5B_$i.json" --skip_generation_tests --continue_from_run="run_$i"
    python3 -m experiments.summarize --dir_name="ModelEdit" --runs="run_$i"
done