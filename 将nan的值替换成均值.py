import numpy as np


def file_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        nan_numbers = np.count_nonzero(temp_col != temp_col)
        if nan_numbers != 0:  # 不为0说明当前列有nan
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前列不为nan的数组
            col = temp_not_nan_col.mean()
            temp_col[np.isnan(temp_col)] = col  # 选中当前为nan的位置，把值赋值为不为nan的均值
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape(3, 4).astype('float')

    t1[1, 2:] = np.nan

    print(t1)

    file_ndarray(t1)

    print(t1)
