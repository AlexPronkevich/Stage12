# The Mirror Vector

# Данная программа проверяет, что все элементы вектора
# расположены в зеркальном виде относительно его середины

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 02.04.2023


def check_specularity(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    if len(ls) == 0 or len(ls) == 1:
        return False

    copy_ls = ls[:]
    ls.reverse()

    flag = True
    for index in range(len(ls) - 1):
        if ls[index] != copy_ls[index]:
            flag = False
    return flag


def test():
    print(check_specularity([1, -8, 76, 0, 7, 0, 76, -8, 1]) == True)
    print(check_specularity([1, -8, 76, 0, 7, 7, 0, 76, -8, 1]) == True)
    print(check_specularity([-6, 55, 0, 6, -2, 46, -11, 1, 7]) == False)
    print(check_specularity(["kkhfflhghjloklkfgcgvm"]) == False)
    print(check_specularity(["$%^#$*&^"]) == False)
    print(check_specularity([]) == False)
    print(check_specularity([-5]) == False)


if __name__ == "__main__":
    test()
