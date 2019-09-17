from collections import OrderedDict

fav_langs = OrderedDict()
fav_langs['jen'] = 'python'
fav_langs['sarah'] = 'c'
fav_langs['edward'] = 'ruby'
fav_langs['phil'] = 'python'

for name, lang in fav_langs.items():
    print(name.title() + "'s favorite language is " + \
        lang.title() + '.')