from players import Player
from utils import load_random_word, load_word

LISTWORD = "word.json"


def main():
    user_name = input("Введите имя пользователя\n").capitalize()
    player = Player(user_name)
    print(f"Привет {player.name}")
    question = load_random_word(load_word(LISTWORD))
    print(
        f"Составьте {question.count_subwords()} слов из слова {question.word.upper()}\n"
        f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
        f"Поехали, ваше первое слово?"
    )
    while player.quantity_words_user() < question.count_subwords():
        user_answer = input().lower()
        if user_answer in "stop":
            break
        elif len(user_answer) < 3:
            print("слишком короткое слово")
        elif player.checking_the_entered_word(user_answer):
            print("уже использовано")
        elif question.is_part_in_list(user_answer):
            print("верно")
            player.adding_word(user_answer)
        else:
            print("неверно")
    print(f"Игра завершена, вы угадали {player.quantity_words_user()} слов!")


if __name__ == '__main__':
    main()