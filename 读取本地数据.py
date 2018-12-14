import numpy as np

us_file_path = './youtube_video_data/US_video_data_numbers.csv'
uk_file_path = './youtube_video_data/GB_data_numbers.csv'

t1 = np.loadtxt(us_file_path, delimiter=',', dtype=np.int, unpack=True)  # 以逗号进行分割
# t2 = np.loadtxt(us_file_path, delimiter=',', dtype=np.int, unpack=False)  # 以逗号进行分割,unpack是转置

t1.astype('float')
nan_count=t1.nonzero(t1!=t1)
print(nan_count)

print(t1)
#
# print(t2[2:, :])

# t3=np.hstack(t1,t2)
# print(t3)