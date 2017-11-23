
# Exception

# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

answers = {
    "Привет": "Здравствуй!", 
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Работаю", 
    "Пойдем гулять?": "С удовольствием!",
    "Пока": "Увидимся!"
}


def get_answer(question, answers):
    return answers[question]

def ask_user(answers):
    while True:
        try:
            user_input = input("Скажи что-нибудь: ")
            answer = get_answer(user_input, answers)
            print(answer)
            if user_input == "Пока":
                break
        except KeyError:
            print("Я не могу ответить на этот вопрос...")

        except KeyboardInterrupt:
            print("\nДо свидания!")
            break
        
    
ask_user(answers)
