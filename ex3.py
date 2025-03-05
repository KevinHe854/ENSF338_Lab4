# Question 1
# Memory will be allocated after the array so that the array grows by a certain factor. If there isn't enough space after the array to grow it, memory will be allocated somewhere else that will hold the expanded array, then all of the elements of the array will move there, then the old array is freed. The array's new capacity is (9 / 8) + 6, then truncated and rounded to the closest multiple of 4, rouding down if it's evenly between two multiples of 4.
#
# Question 5
# There is sometimes a difference in performance between measurement, where the time of growing the array from size S to size S+1 is greater than or equal to growing from size S-1 to size S. This is because when the array capacity is expanded, sometimes there is not enough space after the array in memory to expand, so the system needs to find another place in memory to move the elements and free up the old space. This doesn't happen if the capacity doesn't need to change, such as from S-1 to S.

import sys
import timeit
import numpy as np
from matplotlib import pyplot as plt

length = 0
arr = []

while length < 64:
    old = sys.getsizeof(arr) // 8 - 7
    arr.append(length)
    new = sys.getsizeof(arr) // 8 - 7
    
    if old != new:
        print("Capacity changed from {} to {} when appending {}".format(old, new, length))
    
    length += 1

S4setup = 'S4 = [i for i in range(0, 4)]'
S4stmt = 'S4.append(4)'
S8setup = 'S8 = [i for i in range(0, 8)]'
S8stmt = 'S8.append(8)'
S16setup = 'S16 = [i for i in range(0, 16)]'
S16stmt = 'S16.append(16)'
S24setup = 'S24 = [i for i in range(0, 24)]'
S24stmt = 'S24.append(24)'
S32setup = 'S32 = [i for i in range(0, 32)]'
S32stmt = 'S32.append(32)'
S40setup = 'S40 = [i for i in range(0, 40)]'
S40stmt = 'S40.append(40)'
S52setup = 'S52 = [i for i in range(0, 52)]'
S52stmt = 'S52.append(52)'
S64setup = 'S64 = [i for i in range(0, 64)]'
S64stmt = 'S64.append(64)'

R3setup = 'S3 = [i for i in range(0, 3)]'
R3stmt = 'S3.append(3)'
R7setup = 'S7 = [i for i in range(0, 7)]'
R7stmt = 'S7.append(7)'
R15setup = 'S15 = [i for i in range(0, 15)]'
R15stmt = 'S15.append(15)'
R23setup = 'S23 = [i for i in range(0, 23)]'
R23stmt = 'S23.append(23)'
R31setup = 'S31 = [i for i in range(0, 31)]'
R31stmt = 'S31.append(31)'
R39setup = 'S39 = [i for i in range(0, 39)]'
R39stmt = 'S39.append(39)'
R51setup = 'S51 = [i for i in range(0, 51)]'
R51stmt = 'S51.append(51)'
R63setup = 'S63 = [i for i in range(0, 63)]'
R63stmt = 'S63.append(63)'

S4_time = min(timeit.repeat(setup=S4setup, stmt=S4stmt, repeat=1000, number=1)) * 1000000000
S8_time = min(timeit.repeat(setup=S8setup, stmt=S8stmt, repeat=1000, number=1)) * 1000000000
S16_time = min(timeit.repeat(setup=S16setup, stmt=S16stmt, repeat=1000, number=1)) * 1000000000
S24_time = min(timeit.repeat(setup=S24setup, stmt=S24stmt, repeat=1000, number=1)) * 1000000000
S32_time = min(timeit.repeat(setup=S32setup, stmt=S32stmt, repeat=1000, number=1)) * 1000000000
S40_time = min(timeit.repeat(setup=S40setup, stmt=S40stmt, repeat=1000, number=1)) * 1000000000
S52_time = min(timeit.repeat(setup=S52setup, stmt=S52stmt, repeat=1000, number=1)) * 1000000000
S64_time = min(timeit.repeat(setup=S64setup, stmt=S64stmt, repeat=1000, number=1)) * 1000000000

R3_time = min(timeit.repeat(setup=R3setup, stmt=R3stmt, repeat=1000, number=1)) * 1000000000
R7_time = min(timeit.repeat(setup=R7setup, stmt=R7stmt, repeat=1000, number=1)) * 1000000000
R15_time = min(timeit.repeat(setup=R15setup, stmt=R15stmt, repeat=1000, number=1)) * 1000000000
R23_time = min(timeit.repeat(setup=R23setup, stmt=R23stmt, repeat=1000, number=1)) * 1000000000
R31_time = min(timeit.repeat(setup=R31setup, stmt=R31stmt, repeat=1000, number=1)) * 1000000000
R39_time = min(timeit.repeat(setup=R39setup, stmt=R39stmt, repeat=1000, number=1)) * 1000000000
R51_time = min(timeit.repeat(setup=R51setup, stmt=R51stmt, repeat=1000, number=1)) * 1000000000
R63_time = min(timeit.repeat(setup=R63setup, stmt=R63stmt, repeat=1000, number=1)) * 1000000000

S_times = [S4_time, S8_time, S16_time, S24_time, S32_time, S40_time, S52_time, S64_time]
R_times = [R3_time, R7_time, R15_time, R23_time, R31_time, R39_time, R51_time, R63_time]

br1 = np.arange(len(S_times))
br2 = [x + 0.25 for x in br1]

plt.bar(br1, S_times, color='r', width=0.25, label='S to S+1')
plt.bar(br2, R_times, color='b', width=0.25, label='S-1 to S')

plt.title('Appending to an array of size S')
plt.xlabel('Capacity of array before appending')
plt.ylabel('Time (nanoseconds)')
plt.xticks([r + 0.25 for r in range(len(S_times))], [4, 8, 16, 24, 32, 40, 52, 64])

plt.legend()
plt.show()