# Возраст

# Попросить пользователя ввести возраст.
# По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
# Вывести занятие на экран.


age = float(input("How old are you? "))

if age < 0:
    print("You must enter a positive number!")
else:
    if 0 <= age < 7:
        print("You are attend kindergarden or sit at home with your mom")
    elif 7 <= age < 18:
        print("You are school student")
    elif 18 <= age < 21:
         print("You are university student")
    else: 
        print("You are working")