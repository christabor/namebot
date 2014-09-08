all:
	echo 'Running Namebot tests...'
	nosetests namebot/tests

cleanpyc:
	find . -iname '*.pyc' -type f -delete
