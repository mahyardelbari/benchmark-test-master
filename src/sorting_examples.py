def bubble_sort(input_list: list[int]) -> list[int]:
    """
    Bubble sort algorithm.

    Args:
        input_list (list[int]): A list of numbers.

    Returns:
        list[int]: The sorted list.
    """
    indexing_length = len(input_list) - 1  # Length of list - 1
    sorted = False  # Create variable of sorted and set it equal to false

    while not sorted:
        sorted = True  # Break the while loop if sorted = True

        for i in range(0, indexing_length):  # For every value in the list
            if (
                input_list[i] > input_list[i + 1]
            ):  # If the value we are on is greater than the next value
                sorted = False  # Then the list is not sorted
                input_list[i], input_list[i + 1] = (
                    input_list[i + 1],
                    input_list[i],
                )  # Swap the values
    return input_list  # Return the sorted list


def quick_sort(input_list: list[int]) -> list[int]:
    """
    Quick sort algorithm.

    Args:
        input_list (list[int]): A list of numbers.

    Returns:
        list[int]: The sorted list.
    """
    length = len(input_list)
    if length <= 1:
        return input_list
    else:
        pivot = input_list.pop()

    items_greater = []
    items_lower = []

    for item in input_list:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def insertion_sort(input_list) -> list[int]:
    """
    Insertion sort algorithm.

    Args:
        input_list (list[int]): A list of numbers.

    Returns:
        list[int]: The sorted list.
    """
    indexing_length = range(1, len(input_list))
    for i in indexing_length:
        value_to_sort = input_list[i]

        while input_list[i - 1] > value_to_sort and i > 0:
            input_list[i], input_list[i - 1] = input_list[i - 1], input_list[i]
            i = i - 1

    return input_list