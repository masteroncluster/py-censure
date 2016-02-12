check-pep8:
	find ./censure -name '*.py' -type f | xargs pep8 --max-line-length=99 --ignore=E121,E402

check-flake8:
	flake8 .

check: check-pep8 check-flake8

clean:
	find . -name '*.py[cod]' -delete
