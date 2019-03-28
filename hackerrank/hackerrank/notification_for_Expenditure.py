def find_median(array):
    length = len(array)
    if length % 2 == 0:
        length_ = length // 2 - 1
        return (array[length_] + array[length_ + 1]) / 2
    else:
        i = int((length + 1) / 2)
        return array[i - 1]


def compare_notify(array, window, start_index=0):
    window_ = array[start_index: window + start_index]
    window_.sort()
    median_value = find_median(window_)
    if array[window] >= 2 * median_value:
        print("notify")


def compare_all_expenditure(array, window):
    length = len(array)
    for i in range(0, length):
        if window + i < length:
            compare_notify(array, window, i)


compare_all_expenditure([10, 34, 54, 56, 89, 99, 101, 102], 4)
