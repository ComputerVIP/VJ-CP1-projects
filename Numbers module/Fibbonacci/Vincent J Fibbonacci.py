#Vincent Johnson P1 Fibonacci assignment

import time
tme = int(time.time())
print(tme)
fib = [0,1]
while True:
    tm = int(time.time())
    fib.append(fib[-2]+fib[-1])
    print(fib)
    if round(tm) >= round(tme+10):
        break