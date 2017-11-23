
# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            break

ask_user()