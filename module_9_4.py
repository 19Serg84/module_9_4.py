first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения букв в одной позиции
compare_letters = lambda f, s: f == s

# Применение lambda-функции через map
result = list(map(compare_letters, first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                f.write(f"{item}\n")  # Запись каждого элемента в новую строку
    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Может вывести: "Да"
print(first_ball())  # Может вывести: "Нет"
print(first_ball())  # Может вывести: "Наверное"