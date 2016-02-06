# -*- coding: utf-8 -*-
# based on the words from http://www.noswearing.com/dictionary/

from __future__ import unicode_literals


EXCLUDES_DATA = {

}


EXCLUDES_CORE = {

}

#    'cum': '^cum(($)|(bubble)|(dumpster)|()|()',
FOUL_DATA = {
    'a': [
        '^anus',
        '^axwound',
    ]
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

    'damn': '^damn$',
    'dick': '^dick[\-s]*((bag)|(beaters)|(face)|(head)|(hole)|'
            '(juice)|(milk)|(monger)|(slap)|(suck(er|in))|'
            '(tickler)|(wad)|(weasel)|(weed)|(wod))',
    'dike': '^d[iy]ke$',
    'dildo': 'dildo',
    'dipshit': 'dipshit',
    'doochbag': 'doochbag',
    'dookie': 'dookie',
    'douche': 'douche[\-]*((fag)|(bag)|(waffle))',
    'dumb': 'dum[b\-]($|(ass)|(fuck)|(shit))',

    'fag': 'fag($|(bag)|(g[io]t)|(tard)|(ass))',
    'fellatio': 'fellatio',
    'feltch': 'feltch',
    'flamer': 'flamer',
    'fuck': 'fuck|(^fuk$)',
    'fudgepacker': 'fudgepacker',

    'gay': 'gay((ass)|(bob)|(do)|(lord)|(tard)|(wad))',
    'goddamn': 'god[\-]*dumn',

    'gooch': 'gooch',
    'gook': 'gook',

    'hadjob': 'hadjob',
    'hardon': 'hard(on)*',
    'homodumbshit': 'homodumbshit',
    'humping': 'humping',

    'jackass': 'jackass',
    'jagoff': 'jagoff',
    'jerk': 'jerk((o[f]+)|(ass))',
    'jizz': 'jizz',

    'kooch': 'koo[t]*ch',
    'kunt': 'kunt',

    'lameass': 'lameass',
    'lardass': 'lardass',
    'lesbian': '^lesb(ian|o)',
    'lezzie': '^lezzie',

    'mcfagget': 'mcfagget',
    'minge': 'minge',
    'mothafucka': 'm[oa](th|z)afuck(a|in[g]*|er)',

    'muff': '^muff(diver)*',
    'munging': 'munging'
}


BAD_PHRASES = (
    'suckmydick',
    'sickmyduck',
    'camel toe',
)

TRANS_TAB = {}
