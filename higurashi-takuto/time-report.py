import time
import subprocess
import os.path

number = input('No. ')

times = 10
sum_time = 0

for i in range(times):
    start = time.time()
    res = subprocess.run(
        ['python {}.py'.format(number)],
        cwd=os.path.dirname(__file__), shell=True
    )

    process_time = time.time() - start
    print('{} process_time: {}[sec]'.format(i+1, process_time))
    sum_time += process_time

print('average_process_time: {}[sec]'.format(sum_time/times))
