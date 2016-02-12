# Py-Censure [![travis-ci.org](https://travis-ci.org/masteroncluster/py-censure.svg?branch=master)](https://travis-ci.org/masteroncluster/py-censure/)

=======
Obscene words detection library, written in Python
Check for profanity words and clean them then from phrases, text, and even html

## Features
- Supported languages: **Russian** / **English**, more on You to contribute


## Installation

```sh
pip install py-censure
```

## Examples
    censor = Censor.get(lang='ru')
    line = '<some text line>'
    line_info = censor.check_line(line)  # actually you can call .clean_line without .check_line
    if line_info['is_good']:
        # good line
    ...
    else:
        # bad line
        cleaned_line, bad_words_count, bad_phrases_count = censor.clean_line(line)
        ...
        
Check for more examples and usage in helper.py, show_examples function

## Contributing / Development

> (fork branch, fix a bug, update patterns or add a feature)
> (running tests)
```sh
python setup.py test
```
> (don't forget to 'make check' for pep-8)
> (submit merge request)


[1]: mailto:masteroncluster@gmail.com

## Copyright
> Copyright 2010, 2016, Master.Cluster
