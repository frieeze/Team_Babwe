# ----------------------------
# Part 1 - import library
# 			and constant value
# ----------------------------

# imports:
import os
import logging
import time
from logging.handlers import RotatingFileHandler


# constants:

# ----------------------------
# Part 2 - all functions
#
# ----------------------------

def run_tree_check(logger: logging.RootLogger, option_max_deep: int, option_exploration: str):

    set_new_tree(option_exploration, 0, option_max_deep)

    if (open('.tree.txt', 'r')).read() != (open('tree.txt', 'r')).read():
        logger.info('File tree has change')

        for added_file in get_diff(((open('.tree.txt', 'r')).read()).split(';'), ((open('tree.txt', 'r')).read()).split(';')):
            logger.info('+ : '+added_file)

        for removed_file in get_diff(((open('tree.txt', 'r')).read()).split(';'), ((open('.tree.txt', 'r')).read()).split(';')):
            logger.info('- : '+removed_file)

        os.remove('tree.txt')
        (open('tree.txt', 'w')).write((open('.tree.txt', 'r').read()))

    os.remove('.tree.txt')


def set_new_tree(curDir: str, deep: int, max_deep: int):
    if deep != max_deep:
        deep_separator = ""
        for i in range(0, deep):
            deep_separator += "-"

        with os.scandir(curDir) as it:
            for entry in it:
                f = open('.tree.txt', 'a')
                if not entry.name.startswith('.'):
                    if entry.is_dir():
                        f.write(deep_separator + entry.name + ';')
                        f.close()
                        set_new_tree(curDir + "/" + entry.name, 1 + deep, max_deep)
                    else:
                        f.write(deep_separator + entry.name + ';')
                        f.close()


def get_diff(tree1: [], tree2: []):
    file_diff = []
    for file in tree1:
        if file not in tree2:
            file_diff.append(file)
    return file_diff


# ----------------------------
# Part 3 - main entry
# ----------------------------

if __name__ == "__main__":
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

    for i in range(0, 10):
        run_tree_check(logger, 2, os.getcwd())
        time.sleep(15)
