# The Mirror Vector

# Данная программа проверяет, что все элементы вектора
# расположены в зеркальном виде относительно его середины

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 02.04.2023


def check_specularity(ls):
    copy_ls = ls[:]
    ls.reverse()

    flag = True
    for index in range(len(ls) - 1):
        if ls[index] != copy_ls[index]:
            flag = False
    return flag


def check_specularity(lst):
    copy_lst = lst[:]
    lst.reverse()

    flag = True
    for index in range(len(lst) - 1):
        if lst[index] != copy_lst[index]:
            flag = False
    return flag


def main():
    ls = [1, -8, 76, 0, 7, 0, 76, -8, 1]      # зеркальные элементы
    lst = [-6, 55, 0, 6, -2, 46, -11, 1, 7]   # вектор не зеркальный
    print(check_specularity(ls))
    print(check_specularity(lst))


if __name__ == "__main__":
    main()
