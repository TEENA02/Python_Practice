import time
# /Users/teenasajwan/Documents/PYTHON_Practice/iteration_tool.py
def for_example(n):
    start = time.perf_counter()
    for i in range(n):
        print(f"for loop iteration: {i}")
        time.sleep(0.5)
    print(f"for_example completed in {time.perf_counter() - start:.3f} seconds\n")
    for_example(5)
# >>> f_op.__next__()
# 'import time\n'
# >>> f_op.__next__()
# '# /Users/teenasajwan/Documents/PYTHON_Practice/iteration_tool.py\n'
# >>> f_op.__next__()
# 'def for_example(n):\n'
# >>> f_op.__next__()
# '    start = time.perf_counter()\n'
# >>> f_op.__next__()
# '    for i in range(n):\n'
# >>> f_op.__next__()
# '        print(f"for loop iteration: {i}")\n'
# >>> f_op.__next__()
# '        time.sleep(0.5)\n'
# >>> f_op.__next__()
# '    print(f"for_example completed in {time.perf_counter() - start:.3f} seconds\\n")\n'
# >>> f_op.__next__()
# '    for_example(5)\n'
# >>> f_op.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     f_op.__next__()
#     ~~~~~~~~~~~~~^^
# StopIteration