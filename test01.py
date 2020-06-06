"""
《剑指offer》当中的第一题～困难程度：中等偏上
80道题有关于数据结构与算法的题目
思路：考虑如何遍历数据的效率最高～分别从左上角，右上角，左下角，右下角去考虑～

题目：在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数:
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]
"""
a = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]
def fun01(array_temp, number):
    if array_temp == [] or array_temp[0] == []:
        return False
    last_array = array_temp[-1]
    if number < array_temp[0][0] or number > last_array[-1]:
        return False
    for i in array_temp:  # 第一次遍历的得到的i相当于是第一个一维数组
        # 5   [1, 3, 4]
        if number not in i and number > i[-1]:
            continue
        # 5   [1, 3, 5]
        for j in i:
            if j == number:
                return True
    return False

print(fun01(a, 5))  # Ture
print(fun01(a, 6))  # Ture
