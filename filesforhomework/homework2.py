import os
from pprint import pprint

def get_list_file(path):
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    return text_files

def read_files(fl):
    result = {}
    for file in fl:
        with open(file, encoding='utf-8') as f:
            text = f.readlines()
            result[file] = text
    result = sorted(result.items(), key=lambda x: len(x[1]))
    return result

def write_file(file):
    with open(os.path.join('/Users/komarovaaleksandra/PycharmProjects/'
                           'pythonProject3/filesforhomework/resfile/', 'result.txt'), "wt") as res_file:
        counter = 0
        for file_name, cont in file:
            if counter == 0:
                res_file.write(file_name + '\n')
            else:
                res_file.write('\n' + file_name + '\n')
            res_file.write(str(len(cont)) + '\n')
            for el in cont:
                res_file.write(el)
            counter += 1
    return True



a = get_list_file(os.getcwd())
b = read_files(a)
write_file(b)
