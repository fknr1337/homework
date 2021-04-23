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
            temp_dict['ingridient name'] = a
            temp_dict['quantity'] = int(b)
            temp_dict['measure'] = c
            list_ings.append(temp_dict)
        file.readline()
    pprint(cookbook)


def get_shop_list_by_dishes(dishes, person_count):
    dict = {}
    list = []
    for dish in dishes:
        if dish in cookbook.keys():
            for i in cookbook[dish]:
                i['quantity'] *= person_count
                list.append(i)
    for i in list:
        dict[i.pop('ingridient name')] = i
    pprint(dict)

get_shop_list_by_dishes(["Омлет","Запеченный картофель"], 2)























        # for i in range(ingridient_count):
        #     ings = {}
        #     a, b, c = file.readline().strip().split('|')
        #     print(a,b,c)
        #     ings['ingridient_name'] = a
        #     ings['quantity'] = int(b)
        #     ings['measure'] = c
        #     file.readline()
        # cookbook[dish_name] = ings
        # print(cookbook)













    # while True:
    #     name_of_dish = f.readline().strip()
    #     if not name_of_dish:
    #         break
    #     count = int(f.readline().strip())
    #     ingridients = []
    #     for i in range(count):
    #         temp_dict = {}
    #         ingridients = f.readline().strip()
    #         print(ingridients)
    #     f.readline().strip()
    #     cookbook[name_of_dish] = ingridients
