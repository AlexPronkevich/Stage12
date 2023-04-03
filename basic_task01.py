# Vector of Ordered Values

# Данная программа проверяет, что все элементы находятся
# в упорядоченном виде (либо по возрастанию, либо по убыванию)

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 01.04.2023

ls = (1, -8, 76, -32, 7, 0, -12, 22, 6,)  # Не упорядочены


def check_descending(ls):
    flag = True
    for index in range(len(ls) - 1):
        if ls[index] < ls[index + 1]:
            flag = False
    return flag


def check_ascending(ls):
    flag = True
    for index in range(len(ls) - 1):
        if ls[index] > ls[index + 1]:
            flag = False
    return flag


lst = (44, 32, 21, 12, 9, 5, 0, -5, -23, -54)  # По убыванию


def check_descending(lst):
    flag = True
    for index in range(len(lst) - 1):
        if lst[index] < lst[index + 1]:
            flag = False
    return flag


def check_ascending(lst):
    flag = True
    for index in range(len(lst) - 1):
        if lst[index] > lst[index + 1]:
            flag = False
    return flag


list = (-32, -12, 0, 3, 7, 9, 12, 56, 78, 84)  # По возрастанию


def check_descending(list):
    flag = True
    for index in range(len(list) - 1):
        if list[index] < list[index + 1]:
            flag = False
    return flag


def check_ascending(list):
    flag = True
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            flag = False
    return flag


def main():
    print(check_descending(ls) or check_ascending(ls))
    print(check_descending(lst) or check_ascending(lst))
    print(check_descending(list) or check_ascending(list))


if __name__ == "__main__":
    main()
