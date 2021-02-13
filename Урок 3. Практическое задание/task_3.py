"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""


""
Задание 3.


# hash?
def count_uniq_substr(v_str):
    # v_str="рара" # входная строка
    v_len = len(v_str)
    v_set = set()
    for i in range(v_len):
        for j in range(i + 1, v_len + 1):
            if len(v_str[i:j]) < v_len:     # саму строку в список не вносим
                v_set.add(hash(v_str[i:j])) # добавляем хеш в множество, если такой уже есть - игнорируется
    return len(v_set)

while True:
    print(f"уникальных подстрок: {count_uniq_substr(input('поиск уникальных подстрок в строке. введите строку >>> '))}") 