favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

myset = {'python', 'ruby', 'python', 'c'}

for language in set(favorite_languages.values()):
    print(language)

print(myset)