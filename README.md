# HAKE: Hierarchy-Aware Knowledge Graph Embedding
This is the code of a development of paper [**Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction**](https://arxiv.org/abs/1911.09419) AAAI 2020.  

## Dependencies
- Python 3.6+
- [PyTorch](http://pytorch.org/) 1.0+


## Running the code 

### Create Env
```
conda create -n 3DHAKE
conda activate 3DHAKE
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

### Usage
```
bash runs.sh {train | valid | test} {ModE | HAKE | HAKE1 ... and so on} {wn18rr | FB15k-237 | YAGO3-10} <gpu_id> \
<save_id> <train_batch_size> <negative_sample_size> <hidden_dim> <gamma> <alpha> \
<learning_rate> <num_train_steps> <test_batch_size> [modulus_weight] [phase_weight]
```
- `{ | }`: Mutually exclusive items. Choose one from them.
- `< >`: Placeholder for which you must supply a value.
- `[ ]`: Optional items.

**Remark**: `[modulus_weight]` and `[phase_weight]` are available only for the `HAKE` model.

To reproduce the results of HAKE and ModE, run the following commands.

### HAKE
```
# WN18RR
bash runs.sh train HAKE wn18rr 0 0 512 1024 500 6.0 0.5 0.00005 80000 8 0.5 0.5

# FB15k-237
bash runs.sh train HAKE FB15k-237 0 0 1024 256 1000 9.0 1.0 0.00005 100000 16 3.5 1.0

# YAGO3-10
bash runs.sh train HAKE YAGO3-10 0 0 1024 256 500 24.0 1.0 0.0002 180000 4 1.0 0.5
```

### ModE
```
# WN18RR
bash runs.sh train ModE wn18rr 0 0 512 1024 500 6.0 0.5 0.0001 80000 8 --no_decay

# FB15k-237
bash runs.sh train ModE FB15k-237 0 0 1024 256 1000 9.0 1.0 0.0001 100000 16

# YAGO3-10
bash runs.sh train ModE YAGO3-10 0 0 1024 256 500 24.0 1.0 0.0002 80000 4

# explain
bash runs.sh train ModE wn18rr <gpu_id>0 <save_id>0 <train_batch_size>512 <negative_sample_size>1024 <hidden_dim>500 <gamma>6 <alpha>0.5 \
<learning_rate>0.0001 <num_train_steps>80000 <test_batch_size>8 [modulus_weight]❌ [phase_weight]❌
```


## Acknowledgement
I refer to the code of [HAKE](https://github.com/MIRALab-USTC/KGE-HAKE). Thanks for their contributions.
```
@inproceedings{zhang2020learning,
  title={Learning Hierarchy-Aware Knowledge Graph Embeddings for Link Prediction},
  author={Zhang, Zhanqiu and Cai, Jianyu and Zhang, Yongdong and Wang, Jie},
  booktitle={Thirty-Fourth {AAAI} Conference on Artificial Intelligence},
  pages={3065--3072},
  publisher={{AAAI} Press},
  year={2020}
}
```