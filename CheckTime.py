import os
import logging
import time
from logging.handlers import RotatingFileHandler


def modification_checker(logger: logging.RootLogger):
    for file in ((open('tree.txt', 'r')).read()).split(';') :
        if file is not "" and "activity.log" not in file:
            if time.time() - 15 < os.path.getmtime(file):
                logger.info(file+"  Has been modified")