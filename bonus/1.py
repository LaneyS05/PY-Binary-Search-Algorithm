def recursive_bsearch(arr, element):
    
    def _binary_search(arr, low, high, element):
        if low <= high:
            mid = (low + high) // 2

            if arr[mid] == element:
                return True

            elif arr[mid] > element:
                return _binary_search(arr, low, mid - 1, element)

            else:
                return _binary_search(arr, mid + 1, high, element)
        else:
            return False

    if len(arr) == 0:
        return False

    return _binary_search(arr, 0, len(arr) - 1, element)

arr = [2, 3, 4, 10, 40]
element = 10
result = recursive_bsearch(arr, element)
if result is True:
    print(f"Element {element} is present in the array.")
else:
    print(f"Element {element} is not present in the array.")
