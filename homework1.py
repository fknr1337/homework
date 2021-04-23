from pprint import pprint
cookbook = {}
with open('recipes.txt', encoding = 'utf-8') as file:
    for line in file:
        dish_name = line.strip()
        ingridient_count = int(file.readline())
        list_ings = []
        cookbook[dish_name] = list_ings
        for i in range(ingridient_count):
            a, b, c = file.readline().strip().split('|')
            temp_dict = {}
            temp_dict['ingredient_name'] = a
            temp_dict['quantity'] = int(b)
            temp_dict['measure'] = c
            list_ings.append(temp_dict)
        file.readline()



def get_shop_list_by_dishes(dishes, person_count):
    dict = {}
    for dish in dishes:
        if dish in cookbook.keys():
            for i in cookbook[dish]:
                    if i['ingredient_name'] in dict:
                        quantity = i['quantity'] * person_count
                        dict[i['ingredient_name']]['quantity'] += quantity
                    else:
                        dict[i['ingredient_name']] = {
                            'quantity': i['quantity'] * person_count,
                            'measure': i['measure']
                        }

    return dict

pprint(get_shop_list_by_dishes(["Омлет", "Фахитос"], 2))


