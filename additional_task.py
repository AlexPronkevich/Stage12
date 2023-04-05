# The Exam Resuults

# Данная программа обрабатывает результаты экзамена

def create_list(size, value=0):
    ls = []
    for _ in range(size):
        ls.append(value)
    return ls


def count_fives(ls, size):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] == 5:
            count += 1
        # percent =  count / size * 100
    return count / size * 100


def count_fours(ls):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] == 4:
            count += 1
        return count


def count_three(ls):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] == 3:
            count += 1
        return count


def count_twos(ls):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] == 2:
            count += 1
        return count


def count_units(ls):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] == 1:
            count += 1
        return count


def count_zeros(ls):
    count = 0
    for index in range(len(ls) - 1):
        if ls[index] == 0:
            count += 1
        return count


def main():
    size = int(input("Введите размер списка: "))
    ls = create_list(size)

    print(f"пятерок -   {count_fives(ls, size)} %")
    # print(f"четверок -   {count(count_fours(ls)) / size * 100} %")
    # print(f"троек -   {count(count_three(ls)) / size * 100} %")
    # print(f"двоек -   {count(count_twos(ls)) / size * 100} %")
    # print(f"единиц -   {count(count_units(ls)) / size * 100} %")
    # print(f"нулей -   {count(count_zeros(ls)) / size * 100} %")

if __name__ == "__main__":
    main()
