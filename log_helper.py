import logging
import logging.config
import datetime

class LogHelper(object):
    def __init__(self):
        now = datetime.datetime.now()
        logging.config.fileConfig('logging.conf', defaults={'logfilename': "./logs/log_{0}_{1}_{2}.log".format(now.year, now.month, now.day)})  
    
    def getLogger(self, name):
        return logging.getLogger(name)
        