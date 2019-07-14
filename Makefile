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
	@echo "---> Running Kinematics-Algorithms and Inverse Kinematics"
	@$(PYTHON_INTERPRETER) src/api/kinematics.py 

train:
	@echo "---> Running Genetic Algorithms to Optimize Trajectory Planning"
	@$(PYTHON_INTERPRETER) src/api/train.py 

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
