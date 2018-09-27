import begin
import logging
import FileTree
import time
from logging.handlers import RotatingFileHandler

@begin.start
@begin.convert(refresh_time=int, option_max_deep=int, debug_mode=bool)
def run(folder, logger, refresh_time=15, option_max_deep=5, debug_mode=False):
    """
    """
    open('tree.txt', 'w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    file_handler = RotatingFileHandler('activity.log', 'w', 1000000, 1)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    i = 0
    while i==0:
        FileTree.run_tree_check(logger, option_max_deep, folder)
        time.sleep(refresh_time)
