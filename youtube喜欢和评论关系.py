from matplotlib import pyplot as plt
import numpy as np

# us_file_path =
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# t_us = np.loadtxt(us_file_path, delimiter=',', dtype=int)

t_uk = np.loadtxt(uk_file_path, delimiter=',', dtype=int)

t_uk = t_uk[t_uk[:, 1] <= 10000]

t_uk_comment = t_uk[:, -1]
t_uk_like = t_uk[:, 1]

plt.figure(figsize=(20, 9), dpi=80)

plt.scatter(t_uk_like, t_uk_comment)

plt.show
