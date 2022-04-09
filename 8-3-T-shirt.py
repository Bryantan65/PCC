#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of
#a message that should be printed on the shirt. The function should print a sentence
#summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by
#default with a message that reads I love Python. Make a large shirt and a medium
#shirt with the default message, and a shirt of any size with a different message.



def make_shirt(message = 'I love python', size = 'Large'):
    print(f'The shirt is {size} and the message is: {message}')

#size = medium, default message
make_shirt(size = 'Medium')

#large shirt, default message
make_shirt()

#custom size, custom message
make_shirt('I am quite interested in python', 'omegabig')