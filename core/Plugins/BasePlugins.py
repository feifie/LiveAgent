#!usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 21:25
# @Author  : 黑咖啡
# @Email   : webaa88@126.com
# @File    : BasePlugins.py
# @Software: PyCharm


import platform
import subprocess
from config import settings

# 导入Log模块
from core.Logs import Log


class BasePlugins(object):

    # 判断系统类型，linux执行linux方法，windows执行windows方法
    def perform(self):
        if platform.system() == 'Windows':
            return self.windows()
        elif platform.system() =='Linux':
            return self.linux()
        else:
            raise Exception('支持是windows和linux系统！')

    # 命令执行status[0]表示执行状态，0执行成功，其他未失败
    def run_cmdshell(self,cmd):
        if settings.MODE == True:
            self.status = False
            self.cmd = cmd
            output = subprocess.getstatusoutput(self.cmd)
            if output[0]==0:
                self.status = True
                # '执行成功写入run_log'
                Log().agent_run('shell:[%s] status:%s'%(self.cmd, self.status))
                return output[1]
            elif output[0] != 0:
                print(output)
                # 执行错误写入错误日志
                Log().agent_err('shell:[%s] status:%s'%(self.cmd, self.status))
                return output[1]
                #return output
        elif settings.MODE == False:
            pass




    def linux(self):
        raise Exception('----------')

    def windows(self):
        raise Exception('+++++++++++')