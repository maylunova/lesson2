
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

answers = {
    "Привет": "Здравствуй!", 
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Работаю",
    "Пойдем гулять?": "С удовольствием!",
    "Пока": "Увидимся!"
}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    while True:
        user_input = input("Скажи что-нибудь: ")
        answer = get_answer(user_input, answers)
        print(answer)

        if user_input == "Пока":
            break

ask_user(answers)