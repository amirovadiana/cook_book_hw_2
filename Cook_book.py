from pprint import pprint


cook_book = dict()
with open('recipes.txt', encoding="utf8") as f:
    data = f.readlines()
    row = 0
    while row < len(data):
        dishes = data[row].strip()
        row += 1
        quantity_of_ingredients = int(data[row].strip())
        row += 1
        ingredients = []
        for el in range(quantity_of_ingredients):
            consist = data[row].strip().split('|')
            ingredient_name = consist[0]
            quantity = float(consist[1])
            measure = consist[2]
            consist_dict = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingredients.append(consist_dict)
            row += 1
        cook_book[dishes] = ingredients
        row += 1


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for el in cook_book[dish]:
            ingredient_name = el['ingredient_name']
            quantity = el['quantity'] * person_count
            measure = el['measure']

            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list


pprint(get_shop_list_by_dishes(['Брауни', 'Оладьи'], 3))
