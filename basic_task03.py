# Vector with the Same Values

# Данная программа проверяет, что все элементы
# вектора одинаковы

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 03.04.2023


def compare_elements(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    if len(ls) == 0 or len(ls) == 1:
        return False

    flag = True
    for index in range(len(ls) - 1):
        if ls[index] != ls[index + 1]:
            flag = False
    return flag


def test():
    print(compare_elements([7, 7, 7, 7, 7, 7, 7, 7]) == True)
    print(compare_elements([44, 32, 21, 12, 9, 5, 5, 5]) == False)
    print(compare_elements(["deadfdgffdvgcgvm"]) == False)
    print(compare_elements(["$%^#$=';'';^"]) == False)
    print(compare_elements([]) == False)
    print(compare_elements([675]) == False)


if __name__ == "__main__":
    test()
