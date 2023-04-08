# The Exam Resuults

# Данная программа обрабатывает результаты экзамена

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 07.04.2023

# def create_list(size, value=0):
#     ls = []
#     for _ in range(size):
#         ls.append(value)
#     return ls


def count_fives(ls):
    count = 0
    for index in range(len(ls)):
        if ls[index] == 5:
            count += 1
    return count


def count_fours(ls):
    count = 0
    for index in range(len(ls)):
        if ls[index] == 4:
            count += 1
    return count


def count_three(ls):
    count = 0
    for index in range(len(ls)):
        if ls[index] == 3:
            count += 1
    return count


def count_twos(ls):
    count = 0
    for index in range(len(ls)):
        if ls[index] == 2:
            count += 1
    return count


def count_units(ls):
    count = 0
    for index in range(len(ls)):
        if ls[index] == 1:
            count += 1
    return count


def count_zeros(ls):
    count = 0
    for index in range(len(ls)):
        if ls[index] == 0:
            count += 1
    return count


def main():
    ls = [5, 4, 5, 0, 1, 3, 4, 2, 4, 0, 2, 5, 4, 2, 3, 3, 5, 5, 4, 5]
    print("Исходные оценки:", *ls)
    print("Результаты экзамена:")
    count = count_fives(ls)
    print(f"пятерок - {count / len(ls) * 100} % ({count})")
    count = count_fours(ls)
    print(f"четверок - {count / len(ls) * 100} % ({count})")
    count = count_three(ls)
    print(f"троек - {count / len(ls) * 100} % ({count})")
    count = count_twos(ls)
    print(f"двоек - {count / len(ls) * 100} % ({count})")
    count = count_units(ls)
    print(f"единиц - {count / len(ls) * 100} % ({count})")
    count = count_zeros(ls)
    print(f"нулей - {count / len(ls) * 100} % ({count})")


if __name__ == "__main__":
    main()
