def sandwich(ingredient, **ingredients):
    ingredients[ingredient] = ingredient
    return ingredients


print(sandwich('subaru', color = 'blue', tow_package = True))