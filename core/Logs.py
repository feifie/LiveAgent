#!usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 8:11
# @Author  : 黑咖啡
# @Email   : webaa88@126.com
# @File    : log.py
# @Software: PyCharm


# 暂时没有启用
from config import settings
import logging




class Log(object):
    def __init__(self):
        self.run_log_file = settings.RUN_LOG_FILE
        self.err_log_file = settings.ERROR_LOG_FILE
        self.fmt= "%(asctime)s - %(levelname)s - %(message)s"

    def run_log(self, msg):
        logging.basicConfig(filename=self.run_log_file, level=logging.INFO, format=self.fmt)
        logging.info(msg)

    def err_log(self, msg):
        logging.basicConfig(filename=self.err_log_file, level=logging.DEBUG, format=self.fmt)
        logging.debug(msg)

    def agent_run(self,msg):
        self.run_log(msg)
        return msg

    def agent_err(self,msg):
        self.err_log(msg)
        return msg


if __name__ == '__main__':
    #obj = Log().agent_run('222')
    error = Log().agent_err('666')
    print(error)
    '''
    经测试，同时执行的时候，会有日志丢失！
    '''



