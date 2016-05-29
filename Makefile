all: cleanpyc install tests
cleanpyc:
	find ./ -iname '*.pyc' -type f -delete
install:
	pip install -r requirements.txt
	pip install -U nltk
	python -m nltk.downloader wordnet
	python -m nltk.downloader verbnet
	python -m nltk.downloader stopwords
	python -m nltk.downloader punkt
	python -m nltk.downloader maxent_treebank_pos_tagger
	python -m nltk.downloader averaged_perceptron_tagger
	python setup.py install
tests:
	nosetests
docs:
	sphinx-apidoc -e --private -F -s 'md' -A 'Chris Tabor' -H 'namebot' -o docs namebot tests/
	cp _sphinx_conf.py docs/conf.py
	cd docs && make html
clean: cleanpyc
	rm -r docs
testdocs:
	rm -r docs && make docs && open docs/_build/html/index.html
