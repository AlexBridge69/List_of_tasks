'''
Спрашиваем у пользователя, какой файл открыть?
Открываем нужный файл.
Выводим в консоль пронумерованное построчно содержимое файла.
Пользователь указывает номер задачи, которую нужно отредактировать.
Возвращаем пользователю нужную строку: название задачи и срок выполнения.
Пользователь вводит новые значения.
Уточняем, будем ли изменять срок выполнения.
При необходимости принимаем новый срок.
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
    print(f'№ \t задача \t срок')
    for i in new_list:
        print(f'{i[0]} \t {i[1]} \t {i[2]}')
    what_is_task = int(input("Введите номер задачи: "))
    edit_line = (new_list[what_is_task])[1]
    list_task[what_is_task] = input(f"Измените текст задачи {edit_line}") + "\n"
    change_date = input("Хотите изменить срок выполнения задачи? Ведите 'да' или 'нет': ")
    if change_date != 'нет' or change_date != 'no':
        edit_line = (new_list[what_is_task])[2]
        list_task[what_is_task] = input(f"Введите новый срок выполнения задачи {edit_line}") + "\n"
    return list_task
