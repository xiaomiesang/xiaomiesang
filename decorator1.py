import time

def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the run time is %s' %(stop_time - start_time))
    return deco

@timer             # test1 = timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')
@timer
def test2(name):
    print('test2:',name)

test1()
test2()
# test1 = timer(test1)
# test1()
# test2()
