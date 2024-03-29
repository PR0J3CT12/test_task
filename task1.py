def find_triplets(nums):
    nums.sort()  # сортируем, чтобы не искать нули
    triplets = []
    N = len(nums)
    if nums[0]:  # если минимальный элемент списка != 0, то не получится никак сделать 0 в произведении
        return triplets
    # i двигать нет смысла, т.к. нужен минимум один 0, а триплеты должны быть уникальны с точностью до перестановок
    # поэтому в качестве i можно брать всегда только первый элемент списка(ноль)
    for j in range(1, N):
        k = N - 1
        if (nums[j] == nums[j-1]) and (j > 1):
            # для исключения дубликатов на j
            # j > 1, чтобы исключить вариант, когда будет 2 нуля после сортировки на первых двух элементах списка
            continue
        while j < k:
            if (nums[k] == nums[k-1]) and (j != k - 1):
                # для исключения дубликатов на k
                # j != k - 1, чтобы исключить вариант, когда повторяющиеся цифры в конце
                k -= 1
                continue
            triplets.append([nums[0], nums[j], nums[k]])
            k -= 1

    return triplets


if __name__ == '__main__':
    sequence = [1, 2, 0, 3, 0, 4]
    result = find_triplets(sequence)
    print(result)