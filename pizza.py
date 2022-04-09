def make_pizza(size, *toppings):
    print(f'making a pizza of size {size} with the following ingredients')
    for topping in toppings:
        print(f'- {topping}')

