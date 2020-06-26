import os
import psutil
import time


def genfibonacci(n):
    a = 1
    b = 1
    for i in range(0,n):
        yield a
        c = a + b
        a = b
        b = c


n = 1000000
print("Generating {} Fibonacci numbers. Please wait!!".format(n))
process = psutil.Process(os.getpid())
mem1 = process.memory_info().rss/1000000

# Start generation of Fibonacci
t1 = time.process_time()
for i in genfibonacci(n):
    pass # Just generate, don't print or do anything else to know actual time taken for generation
# All n Fibonacci numbers generated

t2 = time.process_time()
mem2 = process.memory_info().rss/1000000
print('Memory used to generate {} Fibonacci numbers: {:.2f} MB'.format(n, mem2 - mem1))
# Calculate Time taken
print('Time taken to generate {} Fibonacci number: {} seconds'.format(n, t2-t1))