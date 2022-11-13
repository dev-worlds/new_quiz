def getListNumbers():
    string_numbers = input('Введите любые цифры через запятую: ')

    if '/' in string_numbers:
        string_numbers = string_numbers.split('/')
    if ';' in string_numbers:
        string_numbers = string_numbers.split(';')
    if ',' in string_numbers:
        string_numbers = string_numbers.split(',')
    return string_numbers


first_list_numbers = getListNumbers()
second_list_numbers = getListNumbers()

for num in second_list_numbers:
    if num in first_list_numbers:
        first_list_numbers.remove(num)

print(','.join(first_list_numbers))
