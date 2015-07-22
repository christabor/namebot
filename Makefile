all:
	echo 'Running Namebot tests...'
	nosetests namebot/tests
cleanpyc:
	find . -iname '*.pyc' -type f -delete
install:
	pip install -r requirements.txt
	pip install -U nltk
	python -m nltk.downloader wordnet
	python setup.py install
tests:
	nosetests namebot/
