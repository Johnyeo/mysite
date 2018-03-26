# coding:utf-8

# 递归
# ========== # ============== # =============== # =============== # ============
# 循环递归一个文件夹里的所有文件
import os
import threading

from multiprocessing import Process
from time import sleep

dist = os.getcwd()

def displayName(dis):
    for x in os.listdir(dis):
        # os.listdir输出的是str的文件名，因此需要os.path.join成路径之后才ok。
        if os.path.isdir(os.path.join(dis, x)):
            print(x)
            x = os.path.join(dis,x)
            # 这里递归
            displayName(x)
        else:
            print(x)

# 求一个数字的阶乘
# 这个问题经典的不行。原理就是1*2*3*n，可以简化成f(n-1)*n
def fact(n):
    # 确定递归停止的点
    if n == 1:
        x = 1
    else:
        x = n * fact(n - 1)
    return x

# 斐波那契数列 1 1 2 3 5 8
# a，b分别是前两个数。没有设置终点。
def fabonacci(a,b):
    print (a)
    print (b)
    c = a+b
    a = b
    b = c
    # 以上在ptyon里可以简写 a, b = b, a + b
    fabonacci(b,a+b)


# ========== # ============== # =============== # =============== # ============
# 装饰器
def log(func):
    def wrapper(*args,**kwargs):
        print (func.__name__)
        return func(*args,**kwargs)
    return wrapper()
#
# @log
# def testsomething():
#     print('im the thing')


# ========== # ============== # =============== # =============== # ============
# 继承和多态
# 注意super关键字，不能用在经典类里。 经典类就是继承自空。
# 注意super的顺序是按mro顺序来的,可以通过访问__mro__查看。
class human(object):
    def speak(self):
        print('human speaking')
    def pee(self):
        print('human peeing')

class royal(object):
    def cloth(self):
        print("nice suit")

class king(human, royal):
    def cloth(self):
        print('super fancy cloth')
    def pee(self):
        print('king peeing')
        super().cloth()



# ========== # ============== # =============== # =============== # ============
# 定制类
# __getattr__
# 很方便的例子 restful api
# 这里面又用到了递归
class Chain(object):
    def __init__(self,path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

# a = Chain().time.long.man
# print (a)

# ========== # ============== # =============== # =============== # ============
# 生成器
# yield
def odd():
    print('no 1')
    yield 'this is first'
    print('no 2')
    yield 'this is second'

o = odd()
'''
next(o)
next(o)
'''

# (x*x for i in range(10))
g = (x*x for x in range(10))
'''
print(next(g))
print(next(g))
'''

# 多进程
# ========== # ============== # =============== # =============== # ============
def worker(name,age):
    print('my name and age are %s %s im working and my pid is %s' % (name,age,os.getpid()))

'''
if __name__ == '__main__':
    print("im working as well and my pid is %s" % os.getpid())
    p = Process(target=worker,args=('allen','12'))
    print('child start')
    p.start()
    p.join()
    print('child finished')
'''

# 多线程
def hand():
    print('im running')
    sleep(1)
    print('1s past')
    sleep(1)
    print('2s past')

'''
print('kaishi')
t = threading.Thread(target=hand(),)
sleep(3)
t.start()
print('jieshu')
'''







