responses = {}
polling_active = True

while polling_active:
    #Prompt for name and response
    name = input('\nWhat is your name?: ')
    response = input('\nWhich mountain would you like to climb some day? : ')

    # Insert (name = key : value = response) into responses dict.
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

for name, response in responses.items():
    print(f"{name} would like to climb {response}")