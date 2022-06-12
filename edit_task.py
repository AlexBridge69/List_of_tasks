'''
Спрашиваем у пользователя, какой файл открыть?
Открываем нужный файл.
Выводим в консоль пронумерованное построчно содержимое файла.
Пользователь указывает номер задачи, которую нужно отредактировать.
Возвращаем пользователю нужную строку: дату и название задачи.
Пользователь вводит новые значения
Записывем новые данные по индексу в список.
Возвращаем список.
'''


def edit_task(file_now, file_past):
    file_select = input("Введите номер файла, с которым будем работать: ")
    file_flag = []
    if file_select == '1':
        file_flag.append(file_now)
    elif file_select == '2':
        file_flag.append(file_past)
    with open(file_flag[0], 'r') as read_data:
        list_task = read_data.readlines()
    new_list = list(enumerate(list_task))
    print(f'№ \t задача')
    for i in new_list:
        print(f'{i[0]} \t {i[1]}')
    what_is_task = int(input("Введите номер задачи: "))
    edit_line = (new_list[what_is_task])[1]
    list_task[what_is_task] = input(f"Измените задачу {edit_line}") + "\n"
    return list_task