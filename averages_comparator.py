# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.
#
# Важно:
# Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.
# Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют правильность работы программы. Тесты должны учитывать различные сценарии использования вашего приложения.
# Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
# Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.


class AveragesComparator:
    """
    This class compares the averages of two lists of numbers.
    """

    def __init__(self, list1, list2):
        """
        Initialize the class with two lists of numbers.
        """
        self.list1 = list1
        self.list2 = list2

    def get_average_lists(self) -> tuple[float, float]:
        """
        Calculate the average value of a list.
        """
        avg1 = 0
        if self.list1:
            avg1 = sum(self.list1) / len(self.list1)

        avg2 = 0
        if self.list2:
            avg2 = sum(self.list2) / len(self.list2)

        return avg1, avg2

    def compare_lists(self):
        """
        Comparing the averages of two lists.
        """
        avg1, avg2 = self.get_average_lists()

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg1 < avg2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
