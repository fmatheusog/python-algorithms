def quick_sort(letters, start, end):
    if start < end:
        p = partition(letters, start, end) 
        quick_sort(letters, start, p - 1)
        quick_sort(letters, p + 1, end)

def partition(letters, start, end):
    pivot = letters[end]
    delimiter = start - 1

    for index in range(start, end):
        if letters[index] <= pivot:
          delimiter = delimiter + 1
          letters[index], letters[delimiter] = letters[delimiter], letters[index]

    letters[delimiter + 1], letters[end] = letters[end], letters[delimiter + 1]

    return delimiter + 1

def is_anagram(first_string, second_string):
    a = list(first_string.lower())
    b = list(second_string.lower())

    quick_sort(a, 0, len(a) - 1)
    quick_sort(b, 0, len(b) - 1)

    return a == b
