.DEFAULT_GOAL := check
PYTHON_INTERPRETER = python3
PROJECT_NAME := mentor-optimization
BLUE = \033[0;34m
DEFAULT = \033[0m
RED = \033[0;31m
WHITE = \033[1;37m
GENERATIONS = 15
POPULATION = 10
################################################################################
# COMMANDS                                                                     #
################################################################################


install: ##Installation method. Creates folder named as 'dirs' and conda environment with dependences. \n\
		Run verification and configuration steps for requisites.
install: test_environment dirs
	@echo "---> Running setup ..."
	@conda env create -q -f environment.yml --name $(PROJECT_NAME) > /dev/null
	@echo "---> To complete setup please run: conda activate $(PROJECT_NAME)"


test_environment: ##Run verification step for requisites
	@echo "---> Verifying if requisites are already installed"
	@$(PYTHON_INTERPRETER) test_environment.py


update: ##Update method to change dependences.
	@echo "---> Updating dependencies"
	@conda env update -q -f environment.yml


dirs:	## Make command to create folder for results dataframes.
	@echo "---> Creating data folder for results"
	@mkdir -p data/results
	@echo "----> Done"


genetic: ##Method to run genetic optimizatino for a certain trajectory.
	@echo "---> Running Genetic Algorithms to Optimize Trajectory Planning"
	@$(PYTHON_INTERPRETER) src/api/genetic.py --population $(POPULATION) --generations $(GENERATIONS)


help:	## Help method to list all available make commands.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
 

clean:	## Method for removing cached and .pyc or .pyo files.
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete