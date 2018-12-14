import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置字体
my_font = font_manager.FontProperties(fname='C:\Windows\Fonts/STKAITI.TTF')

# 设置框图大小
plt.figure(figsize=(20, 8), dpi=80)

# 本地文件数据输入
x1_file_path = './youtube_video_data/US_video_data_numbers.csv'
x2_file_path = './youtube_video_data/GB_video_data_numbers.csv'
xx1_file_path = './youtube_video_data/USvideos.csv'
xx2_file_path = './youtube_video_data/GBvideos.csv'
x1 = np.loadtxt(x1_file_path, delimiter=',', dtype=np.int)
x2 = np.loadtxt(x2_file_path, delimiter=',', dtype=np.int)
xx1 = np.loadtxt(xx1_file_path, delimiter=',')
xx2 = np.loadtxt(xx2_file_path, delimiter=',')

# 绘制
plt.plot(x1, xx1)

# 设置x轴


# 设置y轴


# 保存图片

# show
plt.show()
