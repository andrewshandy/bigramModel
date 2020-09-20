import re, pickle

#Считывает текст , приводит к lowercase и разбивает на слова
#Возвращает cписок слов
def prepare(input_path):
    # чтение текста
    file = open(input_path)
    text = file.read()

    # приведение к lowercase
    text = text.lower()

    # токенизация
    text = re.sub(r'[^a-zA-Z ^а-яА-Я ^0-9 ]', '', str(text))
    return text.split()


#fit создает словарь по которому в дальнейшем будет производиться генерация
#возвращает словарь
def fit(data , model = "storage"):
    func = {}

    # создание словаря(модели)
    for i in range(1, len(data)):
        if (data[i - 1] in func.keys()):
            func[data[i - 1]].append(data[i])
        else:
            func[data[i - 1]] = [data[i]]
    # сохрание
    filename = model
    outfile = open(filename, 'wb')
    pickle.dump(func, outfile)
    outfile.close()

    return func
