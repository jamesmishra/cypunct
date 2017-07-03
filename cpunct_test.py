from cypunct import cpunct
from cypunct.unicode_classes import COMMON_SEPARATORS
import cypunct
import timeit
import re
splitter = re.compile(' ')

testcase = "James is the best person ever " * 9000
print(cpunct.split(testcase, set((' '))))

case1 = "cpunct.split(testcase, frozenset((' ')))"
case2 = "testcase.split()"
case3 = "splitter.split(testcase)"
case4 = "cypunct.split(testcase, frozenset((' ')))"

case5 = "cpunct.split(testcase, COMMON_SEPARATORS)"
case6 = "cypunct.split(testcase, COMMON_SEPARATORS)"

number = 1000
scene = locals()

def timer(case):
    print(case)
    t = timeit.Timer(stmt=case, setup='import gc; gc.enable()', globals=scene)
    print(min(t.repeat(3, number)))

timer(case1)
timer(case2)
timer(case3)
timer(case4)
print("\n\n")
timer(case5)
timer(case6)
"""
print(case1)
print(timeit.timeit(case1, globals=locals(), number=number))
print(case2)
print(timeit.timeit(case2, globals=locals(), number=number))
print(case3)
print(timeit.timeit(case3, globals=locals(), number=number))
print(case4)
print(timeit.timeit(case4, globals=locals(), number=number))
"""
