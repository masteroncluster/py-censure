# -*- coding: utf-8 -*-
from __future__ import unicode_literals


EXCLUDES_DATA = {

}


EXCLUDES_CORE = {

}

FOUL_CORE = {
    'fuck': 'fuck',
    'arse': '^arse((hole)|$)',
    'ass': '^ass[\-]*((butt)|(idiot)|(hat)|(jabber)|(pirate)|(bag)|(banger)|'
           '(bandit)|(bite)|(clown)|(cock)|(cracker)|(es)|(face)|(goblin)|'
           '(hat)|(head)|(hole)|(hopper)|(jacker)|(lick)|(licker)|(monkey)|'
           '(munch)|(nigger)|(hit)|(sucker)|(wad)|(wipe)|$)'
}


FOUL_DATA = {
    'a': [
        '^anus',
        '^axwound',
    ]
}


BAD_PHRASES = (
    'suckmydick',
    'sickmyduck'
)

TRANS_TAB = {}