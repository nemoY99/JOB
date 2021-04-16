import os
def calc(ope,mas):
    return list({'*': (int(x[0]) * int(x[1])),
                 '/': (int(x[0]) / int(x[1])),
                 '+': (int(x[0]) + int(x[1])),
                 '-': (int(x[0]) - int(x[1]))}.get(ope) for x in mas)

mas = []
f = input("\n1. Если ваш файл находиться в папку с программой просто введите имя файла например 'file.txt'\n2. Если ваш файл не находиться в папку с программой тогда надо указать пут к файле например 'С:\\file.txt'\nВведите имя файла: ")
if not os.path.exists(f):
    result = (f"1. Ваш файл '{f}' не найдено\n2. Введите имя или пут файла привилно\n3. Запустите программу еще раз.")
else:
    with open(f, 'r') as file:
        for line in file.readlines():
            mas.append(line.split(' '))
    operation = input(''' Пожалуйста, выберите тип операции, которую вы хотите выполнить:
                [+]  для сложения
                [-]  на вычитание
                [*] для умножения
                [/]  для деления
               Ваш выбор --> ''')
    if operation not in ['+','-','*','/']:
        result = f'1. вибираный вами оператор [{operation}] не совпадаеть с этими [+] [-] [*] [/]\n2. Введите действующего оператора [+] [-] [*] [/]\n3. Запустите программу еще раз.'
    elif (operation == '/') and ('0' in mas[0] or mas[1]):
        result = f'1. Интерперетатор Python говорить что невозможно делить цифру на ноль потому что в вашем файле найдено цифра [0]\n2. Введите другого оператора [+] [-] [*] [/] или измените цифру [0] с другим числом чтобы делить\n3. Запустите программу еще раз.'
    else:
        lict = (calc(operation,mas))
        with open('negative.txt', 'w') as negative:
            for x in lict:
                if x < 0:
                    negative.write(str(f'{x}\n'))
        with open('positive.txt', 'w') as positive:
            for x in lict:
                if x > 0:
                    positive.write(str(f'{x}\n'))

        result = 'Процесс завершен посмотрите файлы:\n1. negative.txt\n2. positive.txt'
print(result)