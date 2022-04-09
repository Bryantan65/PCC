favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

mustDo = ['phil', 'jen', 'edward', 'obama']

for name in mustDo: #this won't work because it loops thru names of those who have done it, and compares against who must do
                                        # obama doesn't get picked up by this
    if name in favorite_languages.keys():  # this will work 
        print(f'Thanks {name} for participating')
    else:
        print(f'{name} has not completed the survey')



