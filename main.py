dict1 = {'title': 'Ромео и Джульетта', 'genre': 'Драмма', 'issue': '2000', 'pages': '356', 'publishing': 'Украина'}
dict2 = {'title': 'Старик и море', 'genre': 'Роман', 'issue': '1998', 'pages': '544', 'publishing': 'Украина'}
dict3 = {'title': 'Том Сойер', 'genre': 'Классика', 'issue': '2020', 'pages': '368', 'publishing': 'Киев'}
dict4 = {'title': 'Моби Дик', 'genre': 'Классика', 'issue': '2015', 'pages': '128', 'publishing': 'киев'}
autherNames = {'William Shakespeare': dict1, 'Ernest Hemingway': dict2, 'Mark Twain': dict3, 'Herman Melville': dict4}
print(autherNames)


# Добавление новых даных в словарь
def addition():
    try:
        name = str(input("Введите автора: "))
        title = str(input("Введите название книги: "))
        genre = str(input("Введите жанр: "))
        issue = int(input("Введите год выпуска: "))
        pages = int(input("Введите количество страниц: "))
        publishing = str(input("Введите издательство: "))
        dict = {'title': title, 'genre': genre, 'issue': issue, 'pages': pages, 'publishing': publishing}
        autherNames.update({name: dict})
        print(autherNames)
        return autherNames
    except Exception:
        print("Не корректный ввод !")


# Удаление данных из словаря
def delete():
    print("Удалить автора - 0, Удалить информацию о книге - 1")
    question = int(input("Выберите действие: "))
    try:
        if question == 0:
            name = str(input("Введите автора: "))
            autherNames.pop(name)
    except Exception:
        print("Не корректный ввод !")
    try:
        if question == 1:                       # Удаление данных на выбор
            name = str(input("Введите автора: "))
            count = 0
            for key in autherNames[name]:
                count += 1
                print(count, ' - ', key, ' - ', autherNames[name][key])
            index = int(input("Введите значение для удаления [1] [2] [3] или [4]: "))
            key = ''
            count = 0
            for i in autherNames[name]:
                count += 1
                if count == index: key = i
            autherNames[name].pop(key)
        print(autherNames)
        return autherNames
    except Exception:
        print("Не корректный ввод !")