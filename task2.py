def binary_search(arr: list[float], x: float):
    """Perform a binary search on a sorted list to find the target value"""

    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції та повертаємо значення
        else:
            return iterations, arr[mid]

    # якщо елемент не знайдено, верхня межа буде low, якщо вона існує
    if low < len(arr):
        return iterations, arr[low]
    return iterations, None


if __name__ == "__main__":

    arr_for_search = [2.1, 3.2, 4.3, 10.4, 40.5]
    x = 3.1
    result = binary_search(arr_for_search, x)
    print(result)
