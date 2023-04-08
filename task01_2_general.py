# Данная программа находит экстремальные элементы заданной
# последовательности, среднеарифметическое, количество положительных,
# отрицательных и нулевых значений, а также меняет местами
# экстремальные значения

# Это вторая версия программы, где список мы задаем самостоятельно,
# и поэтому можем сделать проверочные тесты

# Version 2.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 06.04.2023


def get_max_value(ls):
    max_value = max(ls)
    return max_value


def get_min_value(ls):
    min_value = min(ls)
    return min_value


def get_average(ls):
    avg = sum(ls) / len(ls)
    return avg


def count_number_positive(ls):
    index = 0
    count_positive = 0
    while index < len(ls):
        if ls[index] > 0:
            count_positive += 1
        index += 1
    return count_positive


def count_number_negative(ls):
    index = 0
    count_negative = 0
    while index < len(ls):
        if ls[index] < 0:
            count_negative += 1
        index += 1
    return count_negative


def count_number_zero(ls):
    index = 0
    count_zero = 0
    while index < len(ls):
        if ls[index] == 0:
            count_zero += 1
        index += 1
    return count_zero


def max_value_index(ls):
    index = 0
    for i in range(len(ls)):
        if ls[index] < ls[i]:
            index = i
    return index


def min_value_index(ls):
    index = 0
    for i in range(len(ls)):
        if ls[index] > ls[i]:
            index = i
    return index


def swap_extreme_elements(ls):
    max_index = max_value_index(ls)
    min_index = min_value_index(ls)
    ls[max_index], ls[min_index] = ls[min_index], ls[max_index]
    return ls


def main():
    ls = [2, -23, 0, 34, 12, -4, 0, 45, -21, 7, -55]
    print("Последовательность начальная:", ls)
    max_value = get_max_value(ls)
    print("Наибольший элемент: ", max_value)
    min_value = get_min_value(ls)
    print("Наименьший элемент: ", min_value)
    avg = get_average(ls)
    print("Среднеарифметическое: ", avg)
    count_positive = count_number_positive(ls)
    print("Количество положительных элементов: ", count_positive)
    count_negative = count_number_negative(ls)
    print("Количество отрицательных элементов: ", count_negative)
    count_zero = count_number_zero(ls)
    print("Количество нулевых элементов: ", count_zero)
    swap_extreme_elements(ls)
    print("Новая последовательность: ", ls)


# if __name__ == "__main__":
#     main()


def test():
    ls = [2, -23, 0, 34, 12, -4, 0, 45, -21, 7, -55]
    print(get_max_value(ls) == 45)
    print(get_min_value(ls) == -55)
    print(get_average(ls) == -0.2727272727272727)
    print(count_number_positive(ls) == 5)
    print(count_number_negative(ls) == 4)
    print(count_number_zero(ls) == 2)
    print(swap_extreme_elements(ls) == [2, -23, 0, 34, 12, -4, 0, -55, -21, 7, 45])


test()
