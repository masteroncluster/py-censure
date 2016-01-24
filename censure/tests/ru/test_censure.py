# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from censure.tests.base import *


class TestCensor(TestCaseRu):
    def test_on_simple_obscene_words(self):
        for words in (
                self.data.SIMPLE_OBSCENE_WORDS,
                self.data.E_OBSCENE_WORDS,
                self.data.PI_OBSCENE_WORDS
        ):
            for line in words:
                cleaned_phrase, bad_words_count = self.censor.clean_line(line)
                self.assertEqual(cleaned_phrase, constants.BEEP)
                self.assertEqual(bad_words_count, 1)

                count = self._get_random_count()
                line_template = ' '.join(('{line}' for _ in range(count)))
                line_repeated = line_template.format(line=line)
                cleaned_phrase, bad_words_count = self.censor.clean_line(line_repeated)
                self.assertEqual(cleaned_phrase, line_template.format(line=constants.BEEP))
                self.assertEqual(bad_words_count, count)

    def test_on_simple_html(self):
        for (html, cleaned_html) in self.data.OBSCENE_HTML_LINES:
            result, bad_words_count = self.censor.clean_html_line(html)
            self.assertTrue(bad_words_count > 0)
            self.assertEqual(result, cleaned_html)

