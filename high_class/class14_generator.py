from memory_profiler import memory_usage
import time
import os

'''
此結果範例是為了證明使用generator可以有效的控管memory
也就是說當為了避免類放既已體或是當記憶以有限的時候generator就會是一個很好的選擇
只是要注意風險是iterator只能用一次，所以需要使用新的變數去存取
如果用list去裝generator就是變回原來的for方法沒有意義

'''

# 使用傳統list的方式來進行讀檔
def read_file(file: str) -> list:
    data=[]
    with open(file, 'r') as f:
        for line in f:
            data.append(line)
    return data

# 使用generator的方式來進行讀檔
def read_file_gen(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

file_path = 'read/reviews.txt'

it = read_file_gen(file_path)
count = 0
sum_len = 0
for line in it:
    sum_len += len(line)
    count +=1
print('avg len = ', sum_len / count)

print(f'Memory: {memory_usage()} MB')
start = time.time()
# it = read_file(file_path)
it = read_file_gen(file_path)
print(next(it))
end = time.time()
print(f'Elapsed {end - start} seconds')
print(f'Mem: {memory_usage()} MB')