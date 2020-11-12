# Genetic Algorithms for Trajectory Optimization

Here we submitted all code snippets to help with artificial intelligence coding to deal with an 
optimization problem, where the trajectory planning of a didactic robot is tackled.

## Setup your base-repo

`$ git remote add base git@github.com:oscarkremer/mentor.git`

To update and get latest features

`$ git pull --rebase base master`

## Install

```bash
$ make
$ make install
```

See: `Makefile` to know other commands.

## Artificial Intelligence Project

==============================

Pipeline to generate trajectories for Mentor didactic robot using artificial intelligence optimization algorithms

## Project Organization

==============================


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make kinematics` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── processed      <- The final, canonical data sets for modeling.The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > environment.yml`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        │
        ├── __init__.py    <- Makes src a Python module
        │
        ├── api           <- Scripts for main code
        │   │
        │   ├── kinematics.py      <- Run kinematics and inverse kinematics
        │   │
        │   └── train.py           <- Run genetic algorithm
        │
        ├── mentor         <- Define mentor class
        │   │   
        │   ├── __init__.py
        │   │
        │   └── mentor.py
        │
        ├── models         <- Define populaion class, and population element class
        │   │   
        │   ├── __init__.py    
        │   │
        │   ├── model.py
        │   │
        │   └── node
        │       │   
        │       ├── __init__.py
        │       │
        │       └── node.py  
        │
        ├── polinomy         <- Define Polinomy class
        │   │   
        │   ├── __init__.py
        │   │
        │   └── model.py
        │
        └── utils  <- Scripts to insert data, constants and numerical manipulations
            │   
            ├── __init__.py    <- Makes src a Python module
            │
            ├── constants.py
            │
            ├── input.py
            │
            └── numerical.py

-------
