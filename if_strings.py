string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")
if string_1 == string_2:
    print(1)
else:
    if string_2 == "learn":
        print(3)
    elif len(string_1) > len(string_2):
        print(2)