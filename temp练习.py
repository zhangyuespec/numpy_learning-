import numpy as np


def main():
    # 创建数组
    a = np.random.randint(1, 100, (10, 10), int).astype('float')

    # 将数组第三行第一列往后改成nan
    print(a)
    a[3, 1:] = np.nan

    # 调用清洗数据的函数
    print(a)
    file_data_clear(a)

    # 打印
    print(a)


def file_data_clear(a):
    # 循环判断每一列
    for i in a.shape[0]:
        temp_col = a[:, i]
        temp_col_count = a.nonzero(np.isnan(temp_col))
        # 如果有nan就将这一列不为nan的数组元组取出来计算均值
        if temp_col_count != 0:
            temp_col_col = temp_col[temp_col == temp_col]
            temp = temp_col.mean(temp_col_col)

            # 替换nan
            temp_col[np.isnan(temp_col)] = temp
        # return
    return a


if __name__ == '__main__':
    main()
