# -*- encoding: gbk -*-

import sys, os

try:
    libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    ## 'os.path.join(path,name)����Ŀ¼���ļ���'
    ## 'os.path.dirname(path)�����ļ�·��'
    ## 'os.path.abspath(name)��þ���·��'
    sys.path.insert(0, libdir)
    ## 'sys.path.insert()��·����ӵ�sys.path'
except:
    sys.path.insert(0, os.path.join(sys.path[0], 'lib'))
    pass

import start
start.run()
