word_dict = {'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}

def num_translate(key):
    word_dict.get(key)
    if key.islower():
        print(key)
    elif key.istitle():
        print(key.title())
    else:
        print("Соблюдай регистр!")

    return


num_translate(input('Введите число на англиском -----> '))