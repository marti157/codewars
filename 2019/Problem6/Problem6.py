from math import ceil
cakes = ceil(float(input()) / 5)
keys = ["natural yogurt.", "eggs.", "flour.!", "cocoa powder.!", "sugar.!", "olive oil.!", "packet of yeast."]
values = [1, 3, 250, 125, 250, 125, 1]
ingredients = dict(zip(keys, values))
for key in keys:
	append = "gr " + key[:-1] if key[-1] == "!" else " " + key
	print("- " + str(int(ingredients[key] * cakes)) + append)