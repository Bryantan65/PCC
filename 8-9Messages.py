def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages,sent_message):
    # while should be used instead of for loop
    # this is because you cannot remove all elements in a list while using a for loop!
    while messages:
        current_message = messages.pop()
        print(current_message, "has been sent")
        sent_message.append(current_message)
    print(sent_message)
    print(messages)



messages = ['hello there', 'short message here, it is 27/3/2022', 'dont give up, nus/ntu boi']
sent_message = []


send_messages(messages[:], sent_message)
print(messages)
