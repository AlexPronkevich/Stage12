# Even Vector Values

# Данная программа подсчитывает количество
# четных элементов

# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 04.04.2023


def count_even(ls):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] % 2 == 0:
            count += 1
    return count


def main():
    ls = [7, -8, 7, 7, 2, 7, 7, 7]  # Одинаковые элементы
    print(count_even(ls))


if __name__ == "__main__":
    main()
