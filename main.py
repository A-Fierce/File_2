import os

def sorted_files():
    list_name = os.listdir()
    dict = {}
    for name_txt in list_name:
        if name_txt.endswith('.txt') and name_txt != 'text.txt':
            with open(name_txt, encoding='utf-8') as read_list:
                dict[name_txt] = read_list.readlines()
    sorted_values = sorted(dict.values())
    sorted_dict = {}
    for sort_value in sorted_values:
        for sort_keys in dict.keys():
            if dict[sort_keys] == sort_value:
                sorted_dict[sort_keys] = dict[sort_keys]
                break

    with open('text.txt', 'w', encoding='utf-8') as sort_text:
        for key_text, value_text_list in sorted_dict.items():
            sort_text.write(f'{key_text}\n{len(value_text_list)}\n{"".join(value_text_list)}\n')
    print('Файл text.txt записан и отсортирован')

sorted_files()