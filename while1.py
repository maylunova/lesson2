my_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while len(my_list) > 0:
    who_are_you = my_list.pop()
    if who_are_you == 'Валера':
        print('Валера нашелся')
        break