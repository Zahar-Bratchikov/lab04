def count_common_elements(*lists):
    """
    Функция принимает N списков и возвращает количество одинаковых элементов в них.
    """
    # Преобразуем все списки в множества
    sets = [set(lst) for lst in lists]

    # Найдем пересечение всех множеств
    common_elements = set.intersection(*sets)

    # Возвращаем количество общих элементов
    return len(common_elements)


# Пример использования функции
if __name__ == "__main__":
    list1 = [1, 2, 5, 4, 6]
    list2 = [4, 5, 6, 7, 8]
    list3 = [0, 5, 4, 6]

    result = count_common_elements(list1, list2, list3)
    print(f"Количество одинаковых элементов: {result}")
