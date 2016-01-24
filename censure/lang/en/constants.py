# -*- coding: utf-8 -*-
# based on the words from http://www.noswearing.com/dictionary/

from __future__ import unicode_literals


EXCLUDES_DATA = {

}


EXCLUDES_CORE = {

}

FOUL_CORE = {
    'fuck': 'fuck',
    # a
    'arse': '^arse((hole)|$)',
    'ass': '^ass((butt)|(idiot)|(hat)|(jabber)|(pirate)|(bag)|(banger)|'
           '(bandit)|(bite)|(clown)|(cock)|(cracker)|(es)|(face)|(goblin)|'
           '(hat)|(head)|(hole)|(hopper)|(jacker)|(lick)|(licker)|(monkey)|'
           '(munch)|(nigger)|(hit)|(sucker)|(ucker)|(wad)|(wipe)|$)',

    # b
    'bampot': '^bampot',
    'bastard': '^bastar[dt]',
    'beaner': '^beaner',
    'bitch': '^bitch',
    'blow': '^blow(job)*',
    'bollo': '^bollo(x|cks)',
    'boner': '^boner$',
    # brotherfucker - fuck root
    'bullshit': '^bullshit$',
    # bumblefuck - fuck root
    'butt': '^butt((plug)|(pirate)|($))',

    # c
    'cameltoe': '^cameltoe$',
    'carpetmuncher': '^carpetmuncher',
    'chesticle': '^chesticle',
    'chinc': '^chin[ck]$',
    'choad': '^choad$',
    'chode': '^chode$',
    'clit': '^clit(($)|(or)|(face))',
    # clusterfuck - fuck root
    'cock': '^cock($|(ass)|(bite)|(burger)|(face)|(head)|(jockey)|(knoker)|'
            '(master)|(mong(ler|ruel))|(monkey)|(muncher)|(nose)|'
            '(nugget)|(shit)|(smith)|(smoke)|(sniffer)|(sucker)|(waffle))',
    'coochie': '^cooch(ie|y)$',
    'coon': '^coon$',
    'cooter': '^cooter$',
    # cracker - Caucasian
    'cum': '^cum(($)|(bubble)|(dumpster)|(guzzler)|(jockey)|(slut)|(tart))',
    'cunni': '^cunni(($)|(e)|(lingus))',
    'cunt': '^cunt(($)|(ass)|(face)|(hole)|(licker)|(rag)|(slut))$',
}
#    'cum': '^cum(($)|(bubble)|(dumpster)|()|()',
FOUL_DATA = {
    'a': [
        '^anus',
        '^axwound',
    ]
}


BAD_PHRASES = (
    'suckmydick',
    'sickmyduck',
    'camel toe',
)

TRANS_TAB = {}
