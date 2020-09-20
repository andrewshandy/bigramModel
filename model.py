import train
import generate
import argparse, pickle


class BigramModel:
    def __init__(self):
        self.func = {}
        self.result = ""
    # обучение модели
    def fit(self , input_path , model):
        data = train.prepare(input_path)
        self.func = train.fit(data , model)
        return self.func
    # генерация
    def generate(self , model = "model", seed = "the" , length = 5):
        self.result = generate.generate(model , seed , length)
        return self.result
    # очистка результата
    def clear(self):
        self.result =[]


if __name__ == '__main__':

    input_path = "data.txt"
    model_path = "model"

    #cоздание модели
    model = BigramModel()
    model.fit(input_path , model_path) # обучение созданной модели
    str = model.generate(model_path , "the" , 20) # генерация нового текста
    print(str)

    # генерация новых строк , если требуется
    ans = input("Do you want to generate more y/n ")
    while (ans == "y"):
        model.clear()
        length = int(input("Enter length "))
        seed = input("Enter seed ")
        new_str = model.generate(model_path, seed, length)
        print(new_str)
        ans = input("Do you want to generate more y/n ")
    # cохранение обучненной модели
    outfile = open(model_path, 'wb')
    pickle.dump(model, outfile)
    outfile.close()
