import pickle, random

def generate(model = "storage" , seed = "the", length = 5):
    # загрузка модели
    infile = open(model, 'rb')
    dict = pickle.load(infile)
    infile.close()

    # генерация
    str_pred = seed + " "
    for i in range (1 , length):
        next_state = random.choice(dict[seed])
        str_pred += next_state + " "
        seed = next_state

    return str_pred
