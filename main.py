# ls = (1, 0, -7, -55, 87,  6, 89, 54, 3, 97, - 9, 0, -54, 5)
#
# # def get_max_value(ls):
# print(f"Наибольший элемент = {max(ls)}")
# print(f"Наименьший элемент  = {min(ls)}")
# print(f"Среднеарифметическое  = {sum(ls) / len(ls)}")
#
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


def main():
    # ls[1, -5, 2, 0, 0, -5, 9]
    print(count_odd([-7, -8, 7, -7, 2, 0, -7, 7, 5, -44, 3]))


if __name__ == "__main__":
    main()
