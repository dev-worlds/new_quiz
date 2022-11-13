string_numbers = input('Введите любые цифры через запятую: ')

if '/' in string_numbers:
    string_numbers = string_numbers.split('/')
if ';' in string_numbers:
    string_numbers = string_numbers.split(';')
if ',' in string_numbers:
    string_numbers = string_numbers.split(',')

string_numbers = list(set(string_numbers))
print(string_numbers)
