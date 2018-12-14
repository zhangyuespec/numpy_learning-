import numpy as np

us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_video_data_numbers.csv'

# 加载国家数据
us_data = np.loadtxt(us_file_path, delimiter=',', dtype=int)
uk_data = np.loadtxt(uk_file_path, delimiter=',', dtype=int)

# 2添加国家信息
# 2.1构造全为0的数据
zero_data = np.zeros((us_data.shape[0], 1)).astype(int)
one_data = np.ones((uk_data.shape[0], 1)).astype(int)

# 2.2分别添加全为0和全为1的一列数据
us_data = np.hstack((us_data, zero_data))
uk_data = np.hstack((uk_data, one_data))

# 拼接两国数据
final_data = np.vstack((us_data, uk_data))
print(final_data)
