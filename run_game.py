# -*- encoding: gbk -*-

import sys, os

try:
    libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    ## 'os.path.join(path,name)连接目录与文件名'
    ## 'os.path.dirname(path)返回文件路径'
    ## 'os.path.abspath(name)获得绝对路径'
    sys.path.insert(0, libdir)
    ## 'sys.path.insert()将路径添加到sys.path'
except:
    sys.path.insert(0, os.path.join(sys.path[0], 'lib'))
    pass

import start
start.run()
