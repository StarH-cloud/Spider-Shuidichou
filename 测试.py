import time

# 单层循环
start_time1 = time.time()
total = 0
for i in range(10000):
    total += i
end_time1 = time.time()
print("单层循环执行时间:", end_time1 - start_time1)

# 双层循环
start_time2 = time.time()
total = 0
for i in range(100):
    for j in range(100):
        total += i + j
end_time2 = time.time()
print("双层循环执行时间:", end_time2 - start_time2)