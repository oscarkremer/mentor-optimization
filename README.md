# Genetic Algorithms for Trajectory Optimization - Machine Learning Toolbox

Here we submitted all code snippets to help with machine learning coding to deal with an optimization problem, where the trajectory planning of a didactic robot is tackled.

## Golden Rule

#### THOU SHALT NEVER USE YOUR TESTING DATA FOR TRAINING

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

## Machine Learning Project

==============================

Pipeline to generate trajectories for robot mentor using artificial intelligence algorithms

## Project Organization

==============================


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > environment.yml`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── api           <- Scripts for main code
    │   │   │
    │   │   ├── kinematics.py      <- Run kinematics and inverse kinematics
    │   │   └── train.py           <- Run genetic algorithm
    │   │
    │   ├── models         <- Define generations, cross-validation, mutation and initialization
    │   │   └── model.py
    │   │
    │   └── utils  <- Scripts to create exploratory and results oriented visualizations
    │   │   ├── input.py       <- Define menu for input.
    │   │   ├── mentor.py      <- Define Mentor class for kinematics and inverse kinematics.
    │   │   ├── numerical.py   <- Define integration.
    │       └── polinomy.py    <- Define polinomial interpolation.
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------
