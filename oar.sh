#!/bin/bash 

#OAR -q production
#OAR -n Evaluate ModelEdit
#OAR -l host=1/gpu=1, walltime=1
#OAR -O ./OAR_logs/OAR_%jobid%.out
#OAR -E ./OAR_logs/OAR_%jobid%.out

export PATH=/home/glauzzana/miniconda3/bin:$PATH

conda activate rome
module load cuda/12.2.1_gcc-10.4.0
nvcc --version
which nvcc
export CUDA_PATH=/grid5000/spack/v1/opt/spack/linux-debian11-x86_64_v2/gcc-10.4.0/cuda-12.2.1-ihyafmkgj5fmsodkl5bavcwjh564cqhd/bin/nvcc
module load gcc/10.4.0_gcc-10.4.0
nvidia-smi

# for i in $(seq 25 48)
# do
#     python3 -m experiments.evaluate --alg_name="ModelEdit" --model_name="Qwen/Qwen2.5-0.5B" --hparams_fname="Qwen_Qwen2.5-0.5B_$i.json" --dataset_size_limit=50
# done
# for i in $(seq -f "%03g" 1 49)
# do
#     python3 -m experiments.summarize --dir_name="ModelEdit" --runs="run_$i"
# done
python3 -m experiments.evaluate --alg_name="ModelEdit" --model_name="Qwen/Qwen2.5-0.5B" --hparams_fname="Qwen_Qwen2.5-0.5B.json" --dataset_size_limit=1