import json
from random import shuffle

from basic_word import BasicWord


def load_word(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_random_word(word_list):
    """
    Функция получает список слов.
    :param word_list: Список слов
    :return: Случайное слово из списка.
    """
    shuffle(word_list)
    for w in word_list:
        """
        Создаем экземпляр класса
        """
        word = BasicWord(
            words=w["word"],
            subwords=w["subwords"]
        )
        return word
