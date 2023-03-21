class Player:
    def __init__(self, name):
        self.user_words = []
        self.name = name

    def __repr__(self):
        return self.user_words, self.name

    def quantity_words_user(self):
        """
        Метод считает кол-во использованных слов.
        :return: Возвращает кол-во использованных слов.
        """
        return len(self.user_words)

    def adding_word(self, us_word):
        """
        Метод добавляет введенные слова.
        :param us_word: Слова введенное пользователем.
        :return: Ничего не возвращает.
        """
        self.user_words.append(us_word)

    def checking_the_entered_word(self, us_word):
        """
        Метод проверяет введенное слово.
        :param us_word: Введенное слово.
        :return: Возвращает bool значение.
        """
        return us_word in self.user_words

