favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil', 'jen']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        langauge = favorite_languages[name]
        print(f"{name.title()}, I see you love {langauge}")

