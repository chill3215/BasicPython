class Ingredient:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name


class Donut:

    # # is equal to constructor and self is just like this
    # def __init__(self, name, price, calories, ingredients):
    #     self.name = name
    #     self.price = price
    #     self.calories = calories
    #     self.ingredients = ingredients
    #
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        if len(args) > 1:
            self.price = args[1]
        # if len(kwargs) > 0:
        #     self.calories = kwargs['calories']
        # if len(kwargs) == 2:
        #     self.ingredients = kwargs['ingredients']
        if kwargs.__contains__('calories'):
            self.calories = kwargs['calories']
        if kwargs.__contains__('ingredients'):
            self.ingredients = kwargs['ingredients']

    def __str__(self):
        return f'this is {self.name} donut, it costs {self.price} and has {self.calories} calories '

    def pick_donut(self):
        print(f"you have picked {self.name} donut with price ${self.price} and calories {self.calories}")

    def donut_info(self):
        print(f"{self.name} donut is made of {self.ingredients.describe()}")


#         one reason i dont like python: there is no way to define type of ingredients, so why writing, method of Ingredient wont be suggested
#         the type of attribute is defined when object is created


chocoDonut = Donut("Chocolatey", 1, calories=400, ingredients=Ingredient(["Flour"]))
fruitDonut = Donut("Fruity", 2, calories=350, ingredients=Ingredient(["Fruit"]))
# strawberryDonut = Donut("Strawberry", 3, 500, "strawberry")
# the string for ingredients doesnt have describe method

# keyword cant be omitted for calling a constructor
carrotDonut = Donut("Carrotey", 3, calories=400)
berlinerDonut = Donut("Berliner", 4, ingredients=Ingredient(["Marmelade"]))

print(chocoDonut.name)
fruitDonut.price = 1.5
print(fruitDonut.price)
print(carrotDonut.price)
berlinerDonut.donut_info()

fruitDonut.pick_donut()
print(chocoDonut.__str__())
chocoDonut.donut_info()
# strawberryDonut.donut_info()
