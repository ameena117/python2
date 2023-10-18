
import timeit

def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# Measure the execution time of the function waste_some_time
execution_time = timeit.timeit("waste_some_time(100)", globals=globals(), number=1)
print(execution_time)

# Or, if you want to time a code snippet:
value2 = '''def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
'''
execution_time2 = timeit.timeit(stmt=value2, globals=globals(), number=1)
print(execution_time2)
