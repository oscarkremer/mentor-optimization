.DEFAULT_GOAL := check
PYTHON_INTERPRETER = python3
PROJECT_NAME := mentor-optimization
BLUE = \033[0;34m
DEFAULT = \033[0m
RED = \033[0;31m
WHITE = \033[1;37m
GENERATIONS = 15
POPULATION = 4
################################################################################
# COMMANDS                                                                     #
################################################################################

setup: check_environment
	@echo "---> Running setup.."
	@conda env create -q -f environment.yml --name $(PROJECT_NAME) > /dev/null
	@cp -n .env.example .env
	@echo "---> To complete setup please run \n---> source activate $(PROJECT_NAME)"


install:	## Installation method. Creates folder named as 'dirs' and conda environment with dependences.
install: dirs
	@echo "---> Installing dependencies"
	@conda env update -f environment.yml


dirs:
	@echo "---> Creating data folder for results"
	@mkdir -p data/results
	@echo "---> Done"

kinematics:
	@echo "---> Running Kinematics-Algorithms"
	@$(PYTHON_INTERPRETER) src/api/kinematics.py 

genetic: ##test
	@echo "---> Running Genetic Algorithms to Optimize Trajectory Planning"
	@$(PYTHON_INTERPRETER) src/api/genetic.py --population $(POPULATION) --generations $(GENERATIONS)


help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
 
# Everything below is an example
 
target00:       ## This message will show up when typing 'make help'
	@echo does nothing
 
target01:       ## This message will also show up when typing 'make help'
	@echo does something
 
# Remember that targets can have multiple entries (if your target specifications are very long, etc.)
target02:       ## This message will show up too!!!
target02: target00 target01
	@echo does even more


clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
