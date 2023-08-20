# Product Inspector

An implementation of anomalib. 

## Install

    bash ./product_inspector_setup.py

## Run

Make sure you are in the conda environment:

    conda activate anomalib_env

Run the program:

    python prod

## Train

Make sure you are in the conda environment:

    conda activate anomalib_env

Run the program:

    python product_inspector_train.py

## Adding a new dataset

Make a new folder in the datasets directory. In that folder make two folders, one called "good" where all the good images go, and, one called bad "bad" where all abnormal/bad images go. It should look something like this:

    new_dataset
    ├── bad
    │  ├── 00.jpg
    │  ├── 01.jpg
    │  ...
    ├── good
    │  ├── 00.jpg
    │  ├── 01.jpg
    │  ...

Then, see config_padim.yaml and modify according to instructions in the file. 
