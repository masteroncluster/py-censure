ENVIRONMENT?=development


check-pep8:
	find ./censure -name '*.py' -type f | xargs pep8 --max-line-length=99 --ignore=E121,E402

check: check-pep8


clean:
	find . -name '*.py[cod]' -delete
