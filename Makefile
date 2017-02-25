.PHONY: install
install:
	pip install -U pip setuptools
	pip install -e .


.PHONY: docs
docs:
	make -C docs html
	@echo "open file://`pwd`/docs/_build/html/index.html"
