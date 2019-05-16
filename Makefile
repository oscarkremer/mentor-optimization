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

grid_search:
	@echo "---> Grid-searching models"
	@echo "---> It will find the best models for the recommendation algorithm"
	@read -p "---> Press Enter to continue. [ctrl-c to abort]" ok
	@$(PYTHON_INTERPRETER) src/api/grid_search.py --negatives $(NEGATIVES) --min-bought $(MIN_BOUGHT) --recommendation-number $(RECOMMENDATION_NUMBER)

kinematics:
	@echo "---> Running Recommendation-Algorithms"
	@$(PYTHON_INTERPRETER) src/api/kinematics.py 
