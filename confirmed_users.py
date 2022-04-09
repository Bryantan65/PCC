unconfirmed = ['jake' , 'paul' , 'tess']

confirmed = []

while unconfirmed:
    #Take current user as the one currently getting removed from list
    currentUser = unconfirmed.pop()
    print(f"Confirmig {currentUser}")
    confirmed.append(currentUser)

for confirmeduser in confirmed:
    print(confirmeduser)