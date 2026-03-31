import time
from random import randint


def big_list():
    lst = []
    for i in range(10000):
        random_number = randint(0, 10000)
        lst.append(random_number)
    return lst


def small_list():
    lst = []
    for i in range(20):
        random_number = randint(0, 10000)
        lst.append(random_number)
    return lst


def bubble_sort(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    swapped = True
    last_part_array = -1
    while swapped:
        swapped = False
        last_part_array += 1
        for i in range(len(array) - 1 - last_part_array):
            if array[i] > array[i + 1]:
                swap(i, i + 1)
                swapped = True

    return array


def choices_sort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array


def insert_sort(array):
    for i in range(len(array)):
        cursor = array[i]
        pos = i
        while pos > 0 and array[pos - 1] > cursor:
            array[pos] = array[pos - 1]
            pos = pos - 1
        array[pos] = cursor
    return array


def merge(left, right):
    lst = []
    left_cursor = 0
    right_cursor = 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            lst.append(left[left_cursor])
            left_cursor += 1
        else:
            lst.append(right[right_cursor])
            right_cursor += 1
    lst.extend(left[left_cursor:])
    lst.extend((right[right_cursor:]))
    return lst


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def quick_sort(array):
    if len(array) <= 1:
        return array
    orientir = array[len(array) // 2]
    left = list(filter(lambda x: x < orientir, array))
    center = [i for i in array if i == orientir]
    right = list(filter(lambda x: x > orientir, array))

    return quick_sort(left) + center + quick_sort(right)


def sorting_time(input_function, array):
    time_start = time.time()
    result = input_function(array)
    time_end = time.time()
    time_result = (time_end - time_start) * 1000
    # print(f'Время работы сортировки составило: {(time_end - time_start) * 1000:.3f} милисекунд')
    return time_result


def comparsion(bubble, choises, insert, merge, quick):
    some_dict = [{"name": "bubble sort algoritm", "time": bubble},
                 {"name": "choises sort algoritm", "time": choises},
                 {"name": "insert sort algoritm", "time": insert},
                 {"name": "merge sort algoritm", "time": merge},
                 {"name": "quick sort algoritm", "time": quick}]

    best = min(some_dict, key=lambda x: x['time'])
    return best


unsorted_big_list = big_list()
unsorted_small_list = small_list()

sorted_bubble_big_list = sorting_time(bubble_sort, unsorted_big_list.copy())

sorted_bubble_small_list = sorting_time(bubble_sort, unsorted_small_list.copy())

sorted_choices_big_list = sorting_time(choices_sort, unsorted_big_list.copy())

sorted_choices_small_list = sorting_time(choices_sort, unsorted_small_list.copy())

sorted_insert_big_list = sorting_time(insert_sort, unsorted_big_list.copy())

sorted_insert_small_list = sorting_time(insert_sort, unsorted_small_list.copy())

sorted_merge_big_list = sorting_time(merge_sort, unsorted_big_list.copy())
sorted_merge_small_list = sorting_time(merge_sort, unsorted_small_list.copy())

sorted_quick_big_list = sorting_time(quick_sort, unsorted_big_list.copy())
sorted_quick_small_list = sorting_time(quick_sort, unsorted_small_list.copy())

big_lists = comparsion(sorted_bubble_big_list, sorted_choices_big_list, sorted_insert_big_list, sorted_merge_big_list,
                       sorted_quick_big_list)
small_lists = comparsion(sorted_bubble_small_list, sorted_choices_small_list, sorted_insert_small_list,
                         sorted_merge_small_list, sorted_quick_small_list)
print(
    f'Скорость сортировки большого списка данных посредством алгоритма bubble_sort равнa {sorted_bubble_big_list:.3f} милисекунд')
print(
    f'Скорость сортировки большого списка данных посредством алгоритма choices_sort равнa {sorted_choices_big_list:.3f} милисекунд')
print(
    f'Скорость сортировки большого списка данных посредством алгоритма insert_sort равнa {sorted_insert_big_list:.3f} милисекунд')
print(
    f'Скорость сортировки большого списка данных посредством алгоритма merge_sort равнa {sorted_merge_big_list:.3f} милисекунд')
print(
    f'Скорость сортировки большого списка данных посредством алгоритма quick_sort равнa {sorted_quick_big_list:.3f} милисекунд')

print(
    f'Самый быстрый алгоритм сортировки больщих списков является: {big_lists["name"]} - {big_lists["time"]:.3f} секунд')

print(
    f'Скорость сортировки маленького списка данных посредством алгоритма bubble_sort равнa {sorted_bubble_small_list:.3f} милисекунд')
print(
    f'Скорость сортировки маленького списка данных посредством алгоритма choices_sort равнa {sorted_choices_small_list:.3f} милисекунд')
print(
    f'Скорость сортировки маленького списка данных посредством алгоритма insert_sort равнa {sorted_insert_small_list:.3f} милисекунд')
print(
    f'Скорость сортировки маленького списка данных посредством алгоритма merge_sort равнa {sorted_merge_small_list:.3f} милисекунд')
print(
    f'Скорость сортировки маленького списка данных посредством алгоритма quick_sort равнa {sorted_quick_small_list:.3f} милисекунд')

print(
    f'Самый быстрый алгоритм сортировки маленьких списков является: {small_lists["name"]} - {small_lists["time"]:.3f} милисекунд')

""" Из результата выяснилось, что при больших входных данных алгоритм merge sort показал себя быстрее всех. 
Однако подозреваю, что реализация моего quick sort довольно громоздка — иначе зачем называть его quick sort?:D
Если исходить сугубо из моей реализации, то merge обгоняет за счёт того, что quick создаёт много новых списков через filter. 
Merge, в свою очередь, просто работает через циклы с условиями, не генерируя дополнительных данных. 
Думаю, отсюда и будет более высокая скорость сортировки.
На больших списках обсуждать bubble sort, insertion sort и selection sort не имеет никакого смысла: 
они прогоняют каждый элемент через цикл, что тратит огромное количество времени. 
В моём коде получается, что они делают 10 000 проходов.

В работе с маленькими списками ситуация интересная: merge и quick уже не доминируют. 
Всё дело в рекурсии — обращаться к своей функции снова и снова ради 5 элементов не имеет никакого смысла, 
это очень затратно по сравнению с обычным циклом.
Если сделать много прогонов, то каждый раз результат разный — bubble, insertion и selection работают 
практически с одинаковой скоростью."""
