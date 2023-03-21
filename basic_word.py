"""
Создаю класс `BasicWord`.
Этот класс будет содержать в себе:
Поля:
- исходное слово,
- набор допустимых подслов.
Методы:
- проверку введенного слова в списке допустимых подслов (вернет bool),
- подсчет количества подслов (вернет int).
"""


class BasicWord:
    def __init__(self, words, subwords):
        self.word = words
        self.subwords = subwords

    def __repr__(self):
        return self.word, self.subwords

    def is_part_in_list(self, user_answer):
        """
        Делаем проверку введенного слова в списке
        допустимых подслов (вернет bool)
        """
        if user_answer.lower() in self.subwords:
            return True
        return False

    def count_subwords(self):
        """
        подсчет количества подслов (вернет int)
        """
        return len(self.subwords)
