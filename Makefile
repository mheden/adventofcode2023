.SILENT:
# SHELL=cmd

.PHONY: all format check
all:
	for file in *.py ; do \
		python $$file ; \
	done

format:
	".venv/Scripts/black" *.py

check:
	".venv/Scripts/flake8" --max-line-length=88 --extend-ignore E203 *.py
