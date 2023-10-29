# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


def search_binary(sorted_list: list[int], number: int):
    left_pos = 0
    right_pos = len(sorted_list) - 1

    while left_pos <= right_pos:
        medium_pos = (left_pos + right_pos) // 2
        medium = sorted_list[medium_pos]
        if number > medium:
            left_pos = medium_pos + 1
        elif number < medium:
            right_pos = medium_pos - 1
        else:
            return medium_pos
    else:
        return -1


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 12, 31, 55, 56, 70]
    print(search_binary(lst, 15))
