.DEFAULT_GOAL := check
PYTHON_INTERPRETER = python3
PROJECT_NAME := mentor

################################################################################
# COMMANDS                                                                     #
################################################################################

setup: check_environment
	@echo "---> Running setup.."
	@conda env create -q -f environment.yml --name $(PROJECT_NAME) > /dev/null
	@cp -n .env.example .env
	@echo "---> To complete setup please run \n---> source activate $(PROJECT_NAME)"

install:
	@echo "---> Installing dependencies.."
	@conda env update -q -f environment.yml --name $(PROJECT_NAME) > /dev/null

dirs:
	@echo "---> Creating data dirs"
	@mkdir -p data/logs
	@mkdir -p data/binary/models
	@mkdir -p data/processed
	@mkdir -p data/predicted
	@mkdir -p data/raw
	@echo "---> Done"

kinematics:
	@echo "---> Running Kinematics-Algorithms"
	@$(PYTHON_INTERPRETER) src/api/kinematics.py 

train:
	@echo "---> Running Genetic Algorithms to Optimize Trajectory Planning"
	@$(PYTHON_INTERPRETER) src/api/train.py 

help:
	@echo "--- List of Commands ---"
	@echo "--- install: Start installation of environment"
	@echo "--- setup: Check environment and setup variables"
	@echo "--- dirs: Create directory to save plots and .csv"
	@echo "--- help: See list of possible commands"
	@echo "--- kinematics: Run kinematics calculations for Mentor Robot"
	@echo "--- train: Start running genetic algorithm for trajectory optimization"
	@echo "--- clean: Remove unecessary files"
	@echo "--- dirs: Create directory to save plots and .csv"

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
