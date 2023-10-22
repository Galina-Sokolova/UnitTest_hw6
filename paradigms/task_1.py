def find_num(array, target):
    for i in array:
        if target == i:
            return print("Число найдено")
            break
    return print("Числа нет в массиве")


def ratios_array(lst):
    pos = len(list(filter(lambda x: x > 0, lst)))
    neg = len(list(filter(lambda x: x < 0, lst)))
    zero = len(list(filter(lambda x: x == 0, lst)))

    lst_len = len(lst)
    pos_ratio = pos / lst_len
    neg_ratio = neg / lst_len
    zero_ratio = zero / lst_len

    return pos_ratio, neg_ratio, zero_ratio


# init_list = [1, 2, -3, -4, 0]
# print(ratios_array(init_list))


############################################
def count_numbers1(arr):
    total = len(arr)
    if total == 0:
        raise ValueError('Array is empty')
    # positive = sum(1 for num in arr if num > 0)
    # zero = sum(1 for num in arr if num == 0)
    # negative = sum(1 for num in arr if num < 0)
    positive = sum(num > 0 for num in arr)
    zero = sum(num == 0 for num in arr)
    negative = sum(num < 0 for num in arr)
    return positive / total, zero / total, negative / total


# my_array = [-5, -1, 0, 1, 0, 5]
# print(count_numbers1(my_array))


##################################################


def find_fraction(lst):
    count_pos_num = 0
    count_null = 0
    count_negative_num = 0
    # for i in lst:
    #     if i > 0:
    #         count_pos_num += 1
    #     elif i == 0:
    #         count_null += 1
    #     else:
    #         count_negative_num += 1
    # if len(lst) != 0:
    #     fraction_pos = count_pos_num / len(lst)
    #     fraction_null = count_null / len(lst)
    #     fraction_negative = count_negative_num / len(lst)
    #     return fraction_pos, fraction_null, fraction_negative
    # else: return 0, 0, 0


# if __name__ == "__main__":
#     lst = [1, 2, 3, 4, 5, -2, -3, -5, -6, 0]
#     print(find_fraction(lst))
# arr = [[1, 2, 3],
#        [2, 5, 4],
#        [3, 4, 5]]
# sum = 0
# for i in range(len(arr)):
#     sum += arr[i][i]
# print(sum)
def conversion_number_system(num, n):
    count = 0
    while num != 0:
        rem = num % n
        num = num // 10
        num2 = count * 10
        num1 = f'{num2} + {rem}'
        count += 1
    return num1


if __name__ == "__main__":
    print(conversion_number_system(12, 2))

