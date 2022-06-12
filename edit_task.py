'''
1. запрос польз какой файл читать? !
2. Открываем нужный файл для чтения !
3. Превращаем текст в список построчно ! и спрашиваем  какую строку нужно редактировать по индексу
4. Возвращаем пользователю нужную строку: дату и название задачи.
5. пользователь вводит новые значения
6. Записывем новые данные по индексу в список.
7. Возвращаем список.
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


def task_was_run(file_now, file_past):
    file_flag = []
    file_flag.append(file_now)
    with open(file_flag[0], 'r') as read_data:
        list_task = read_data.readlines()
    new_list = list(enumerate(list_task))
    print(f'№ \t задача')
    for i in new_list:
        print(f'{i[0]} \t {i[1]}')
    what_is_task = int(input("Введите номер задачи, которая была выполнена: "))




edit_task('1.txt', '2.txt')
