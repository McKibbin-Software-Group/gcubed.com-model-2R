# Custom variable definitions
VERSION=2R
BUILD=191
ROOT_SYM_FILE=ggg-model.sym
SCRIPT=run_experiment_1.py

DATE_STAMP := $(shell date +"%Y-%m-%d %H:%M:%S")
SYM=sym
PYTHON=python
MODEL=$(VERSION)_$(BUILD)

# (default target) Run the chosen target by default
default: run

# Basic example of running a script
run:
	$(PYTHON) $(VERSION)/$(BUILD)/python/$(SCRIPT)

baseline:
	$(PYTHON) $(VERSION)/$(BUILD)/python/run_baseline.py

share:
	$(PYTHON) $(VERSION)/$(BUILD)/python/share_baseline_projections_with_experiments.py

format:
	black $(VERSION)/$(BUILD)/python/*.py

# Git staging of changes, commit, and push to remote repository on Github
push:
	@read -p "Enter commit message: " message; \
	echo "Adding changes..."; \
	git add .; \
	echo "Committing changes..."; \
	git commit -m "$$message"; \
	echo "Pushing to remote repository..."; \
	git push; \
	echo "Done"

# Add a note to a branch to describe it
desc:
	@read -p "Enter branch description: " description; \
	echo "Adding branch description..."; \
	git notes add -f -m "BRANCH_DESCRIPTION $(DATE_STAMP): $$description"; \
	echo "Done"

# Show the description of a branch
show:
	git notes show

# Generate html and sym files on MacOS for the model using the sym processor
sym:
	@echo "Running SYM processor for model $(VERSION) build $(BUILD) starting from $(ROOT_SYM_FILE) ..." ; \
	cd $(VERSION) && cd $(BUILD) && cd sym ;\
	rm -f *.html && rm -f *.csv && rm -f *.lis && rm -f *.py ;\
	$(SYM) -html $(ROOT_SYM_FILE) model_$(VERSION)_$(BUILD).html ;\
	$(SYM) -python $(ROOT_SYM_FILE) model_$(VERSION)_$(BUILD).py ;\
	echo "Updated files in $(VERSION)/$(BUILD)/sym:" ;\
	ls -la ;\
	cd ..  && cd .. && cd .. ;\
	echo "... The SYM processor has finished running. Check that a *.py file has been created and check that there is no rubbish.lis file." ;

# Remove temporary python files
clean:
	rm -rf **/__pycache__
	rm -rf *.pyc
	rm -rf *.pyd
	rm -rf *.py0
	
# List the targets that are not related to specific file timestamps
.PHONY: run, baseline, share, push, format, desc, show, sym, clean
