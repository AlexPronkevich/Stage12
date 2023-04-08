# Even Vector Values

# Данная программа подсчитывает количество
# четных и нечетных элементов

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 04.04.2023


def count_even(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    if len(ls) == 0 or len(ls) == 1:
        return False

    count = 0
    for index in range(len(ls)):
        if ls[index] % 2 == 0 and ls[index] != 0:
            count += 1
    return count


def count_odd(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    if len(ls) == 0 or len(ls) == 1:
        return False

    count = 0
    for index in range(len(ls)):
        if ls[index] % 2 == 1:
            count += 1
    return count


def test():
    print(count_even([7, -8, 7, 7, 2, 0, -7, 7, -44, 7]) == 3)
    print(count_odd([7, -8, 7, 7, 2, 0, -7, 7, -44, 7]) == 6)
    print(count_even(["ooiyfxkgngng"]) == False)
    print(count_odd(["ooiyfxkgngng"]) == False)
    print(count_even(["$%^#$;'/'^"]) == False)
    print(count_odd(["$%^#$;'/'^"]) == False)
    print(count_even([]) == False)
    print(count_odd([]) == False)
    print(count_even([66]) == False)
    print(count_odd([66]) == False)


if __name__ == "__main__":
    test()
