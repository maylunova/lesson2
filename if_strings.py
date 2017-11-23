# Сравнение строк

# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def is_it_the_same(string_1, string_2):
    if string_1 == string_2:
        print(1)
    else:
        if string_2 == "learn":
            print(3)
        elif len(string_1) > len(string_2):
            print(2)

string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")

it_is_the_same(string_1, string_2)
