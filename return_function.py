def get_formatted_name(f,l):
    full_name = f"{f} {l}"
    return full_name

musician = get_formatted_name('jimi' , 'hendrix')

print(musician)

def build_person(firstname, lastname, age=None):
    """Return a dict of information about a person"""
    person = {"first":firstname , "last":lastname}
    if age:
        person['Age'] = age
    return person

builtPerson = build_person('johny', 'silverhand', 69)

print(builtPerson)