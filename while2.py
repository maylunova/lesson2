my_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
    while len(my_list) > 0:
        who_are_you = my_list.pop()
        if who_are_you == name:
            return True
    return False

name = 'Валера'
if find_person(name):
    print(name + ' нашелся')
else:
    print(name + ' не в списке')