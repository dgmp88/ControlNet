
1. Install miniconda

wget https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh
sh Miniconda3-py38_23.1.0-1-Linux-x86_64.sh

2. Install environment

`conda env create --file environment.yml`

3. Download models 

`sudo apt-get install aria2`
`HF_TOKEN=hf_*** python download_models.py`