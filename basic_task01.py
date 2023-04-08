# Vector of Ordered Values

# Данная программа проверяет, что все элементы находятся
# в упорядоченном виде (либо по возрастанию, либо по убыванию)

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 01.04.2023


def check_descending(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    if len(ls) == 0 or len(ls) == 1:
        return False

    flag = True
    for index in range(len(ls) - 1):
        if ls[index] < ls[index + 1]:
            flag = False
    return flag


def check_ascending(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    if len(ls) == 0 or len(ls) == 1:
        return False

    flag = True
    for index in range(len(ls) - 1):
        if ls[index] > ls[index + 1]:
            flag = False
    return flag


def check(ls):
    return check_descending(ls) or check_ascending(ls)


def test():
    print(check([1, -8, 76, -32, 7, 0, -12, 22, 6]) == False)  # Не упорядочены
    print(check([44, 32, 21, 12, 9, 5, 0, -5, -23, -54]) == True)  # По убыванию
    print(check([-32, -12, 0, 3, 7, 9, 12, 56, 78, 84]) == True)  # По возрастанию
    print(check([]) == False)
    print(check("kjjhcgcbgch") == False)
    print(check("099@#%^^%@334576") == False)
    print(check([8]) == False)


if __name__ == "__main__":
    test()
