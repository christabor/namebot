dependencies:
	cd web && sudo pip install -r requirements.txt

tests:
	echo 'Running Namebot tests...'
	nosetests web/namebot/tests/
