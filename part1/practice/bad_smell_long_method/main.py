# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def read_str():
    data = {}
    for line in csv.split('\n'):
        name, age = line.split(';')
        data[name] = int(age)
    return data

def sort_by_ages(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1])
    return dict(sorted_data)

def filter(data: dict):
    keys_to_remove = []
    for key in data.keys():
        if data[key] < 10:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        data.pop(key)
    return data



if __name__ == '__main__':
    data = read_str()
    data = sort_by_ages(data)
    print(filter(data))
