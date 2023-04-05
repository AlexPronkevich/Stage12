# Vector with the Same Values

# Данная программа проверяет, что все элементы
# вектора одинаковы

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 03.04.2023


def compare_elements(ls):
    flag = True
    for index in range(len(ls) - 1):
        if ls[index] != ls[index + 1]:
            flag = False
    return flag


def compare_elements(lst):
    flag = True
    for index in range(len(lst) - 1):
        if lst[index] != lst[index + 1]:
            flag = False
    return flag


def main():
    ls = [7, 7, 7, 7, 7, 7, 7, 7]  # Одинаковые элементы
    lst = [44, 32, 21, 12, 9, 5, 5, 5]  # Не одинаковые элементы
    print(compare_elements(ls))
    print(compare_elements(lst))


if __name__ == "__main__":
    main()
