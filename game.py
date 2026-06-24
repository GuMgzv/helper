import random

zagadano = random.randint(1, 100)
popytki = 0

while True:
    dogadka = int(input("Угадай число от 1 до 100: "))
    popytki = popytki + 1

    if dogadka < zagadano:
        print("Загаданное число больше")
    elif dogadka > zagadano:
        print("Загаданное число меньше")
    else:
        print("Угадала! Попыток:", popytki)
        break