.PHONY: *

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

install:
	pip install -e .

test: install
	pytest

build: install
	python -m build

publish: build
	python3 -m twine upload dist/*