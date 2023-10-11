# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def sorting_list(lst: [int]):
    length = len(lst)
    for i in range(length):
        for j in range(0, length - i - 1):
            if lst[j + 1] > lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sorting_list_declarative(lst: [int]):
    lst_sort = list(reversed(sorted(lst)))
    return lst_sort


if __name__ == "__main__":
    lst = [1, 12, 3, 41, 5, -12, -31, -5, -6, 0]
    print(sorting_list(lst))
    print(sorting_list_declarative(lst))
