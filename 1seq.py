list_length = int(input('Введите количество элементов будущего списка: '))
new_list = []

for i in range(list_length):
    new_list.append(int(input(f'Введите {i + 1} элемент: ')))

new_list.sort()
print('Сортировка по возрастанию:', new_list)
