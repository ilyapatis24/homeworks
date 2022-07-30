def my_cook_book():
    with open('cook.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li
    return cook_book

def get_shop_list_by_dishes(dishes,person_count):
    new_cook = {}
    cook_book = my_cook_book()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient['quantity'] *= person_count
                new_cook.setdefault(ingredient['ingredient_name'], ingredient)
   
    dic_dish = {}
    for value in new_cook.values():
        name = value['ingredient_name']
        del value['ingredient_name']
        dic_dish[name] = value
    print(dic_dish)
        
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'],2)