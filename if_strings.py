# Сравнение строк

# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def is_equal(string_1, string_2):
    if string_1 == string_2:
        return 1
    else:
        if len(string_1) > len(string_2):
            return 2
        elif string_2 == "learn":
            return 3

string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")

print(is_equal(string_1, string_2))
