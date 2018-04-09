#!usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 21:23
# @Author  : 黑咖啡
# @Email   : webaa88@126.com
# @File    : settings.py
# @Software: PyCharm


import os
import sys

#-----------------agent--conf---start------------------

# 设置程序目录
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)


# 插件配置


PLUGINS = {

    'disk':'core.plugins.disk.DiskPlugins',
    'cpu':'core.plugins.cpu.CpuPlugins',
    'mem':'core.plugins.mem.MemPlugins',
    'nic':'core.plugins.nic.NicPlugins',
    'plate':'core.plugins.plate.PlatePlugins',

}

#API 认证信息
KEY = 'w1u8s2u1h0u1a1-1w7o9x8ingni'
AUTH_KEY_NAME = 'auth-key' # 不能使用下划线
#http的请求头不能使用下划线,可以使用-。


# 设置模式True为生产模式，False为测试模式

MODE = False



#设置日志级别：

Log_Level=['logging.DEBUG','logging.ERROR']

'''
日志等级：使用范围

FATAL：致命错误
CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
ERROR：发生错误时，如IO操作失败或者连接问题
WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误
INFO：处理请求或者状态变化等日常事务
DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态
'''


# 设置日志文件路径

ERROR_LOG_FILE = os.path.join(BASEDIR,'log','error.log')
RUN_LOG_FILE = os.path.join(BASEDIR,'log','run.log')


# 设置本地唯一标识路径
CERT_FILE_PATH = os.path.join(BASEDIR,'conf','ServerNid')



# 设置接口地址
API = 'http://192.168.1.112:8000/api/client-api'


if __name__ == '__main__':
    print(CERT_FILE_PATH)
    print(ERROR_LOG_FILE)
    print(Log_Level[0])
    print(PLUGINS)