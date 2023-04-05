
# ls = (1, 0, -7, -55, 87,  6, 89, 54, 3, 97, - 9, 0, -54, 5)
#
# # def get_max_value(ls):
# print(f"Наибольший элемент = {max(ls)}")
# print(f"Наименьший элемент  = {min(ls)}")
# print(f"Среднеарифметическое  = {sum(ls) / len(ls)}")
#
# for index in range (1, )

def create_list(size, value=0):
    ls = []
    for _ in range(size):
        ls.append(value)
    return ls

def main():
    size = int(input("Введите размер списка: "))
    ls = create_list(size)
    print(ls)
    # print(f"пятерок -   {count(count_fives(ls)) / size * 100} %")
    # print(f"четверок -   {count(count_fours(ls)) / size * 100} %")
    # print(f"троек -   {count(count_three(ls)) / size * 100} %")
    # print(f"двоек -   {count(count_twos(ls)) / size * 100} %")
    # print(f"единиц -   {count(count_units(ls)) / size * 100} %")
    # print(f"нулей -   {count(count_zeros(ls)) / size * 100} %")

if __name__ == "__main__":
    main()

