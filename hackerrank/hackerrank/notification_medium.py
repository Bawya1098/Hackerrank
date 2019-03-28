# from math import floor
#
#
# def activityNotifications(expenditure, d):
#     print(expenditure)
#     median_list = []
#     sorted_list = []
#     mid_value = floor(d / 2)
#     notice_count = 0
#     print("mid_value:", mid_value)
#
#     for index in range(0, len(expenditure)):
#         slice_range = index + d
#         slice_object = slice(index, slice_range)
#         value = expenditure[slice_object]
#         if len(value) == d:
#             median_list.append(expenditure[slice_object])
#         for element in range(0, len(median_list)):
#             sorted_value = sorted(median_list[element])
#             sorted_list.append(sorted_value)
#             median = sorted_list[element][mid_value]
#             print("median:", median)
#         print("sorted list:", sorted_list)
#         print(median_list)
#
#
# #
# # if __name__ == '__main__':
# #     nd = input().split()
# #
# #     n = int(nd[0])
# #
# #     d = int(nd[1])
# #
# #     expenditure = list(map(int, input().rstrip().split()))
# #
# #     result = activityNotifications(expenditure, d)
#
# activityNotifications([1, 2, 3, 4, 4], 4)


