# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import os
import codecs

from censure.base import Censor


class CensorHelper:
    do_compile = True

    def __init__(self, lang='ru', do_compile=None):
        if do_compile is None:
            do_compile = self.do_compile
        self.lang = lang
        self.c = Censor.get(lang=lang, do_compile=do_compile)

    def censure_text(self, text):
        count = 0
        result = []
        for line in text.splitlines():
            new_line, bad_words_count = self.c.clean_line(line)
            count += bad_words_count
            result.append(new_line)
        return "\n".join(result), count

    def test(self):
        # u, j = self.c.clean_line('членоплет')
        # print (u)
        # return

        d = os.path.dirname(os.path.abspath(__file__))
        in_file = os.path.join(d, 'data', '{}_in.txt'.format(self.lang))
        out_file = os.path.join(d, 'data', '{}_out.txt'.format(self.lang))

        with codecs.open(in_file, 'r', 'utf-8') as in_fs, codecs.open(out_file, "w", 'utf-8') as out_fs:
            text = in_fs.read()
            cleaned_text, count = self.censure_text(text)
            print("Found and replaced count: {}".format(count))
            out_fs.write(cleaned_text)


def ru_just_test():
    c = CensorHelper(lang='ru', do_compile=False)
    c.test()

def en_just_test():
    c = CensorHelper(lang='en')
    c.test()


if __name__=="__main__":
    # ru_just_test()
    en_just_test()
    # from timeit import Timer
    # t = Timer("just_test()", "from __main__ import just_test")
    # print(t.timeit())

