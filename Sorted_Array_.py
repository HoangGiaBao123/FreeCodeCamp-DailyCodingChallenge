def is_sorted(arr):
    if arr == sorted(arr, reverse=True):
        return 'Descending'
    elif arr == sorted(arr):
        return 'Ascending'
    else:
        return "Not sorted"
