# (default target) Run the chosen target by default
default: push

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

config:
	git config --global user.email "$(EMAIL)"
	git config --global user.name "$(NAME)"

format:
	black */*/python/*.py
	black */*/simulations/*/*.py

# Remove temporary python files
clean:
	rm -rf **/__pycache__
	rm -rf *.pyc
	rm -rf *.pyd
	rm -rf *.py0
	
# List the targets that are not related to specific file timestamps
.PHONY: push, config, format
