# ----------------------------
# Part 1 - import library
# 			and constant value
# ----------------------------

# imports:
import os
from termcolor import colored


# constants:

# ----------------------------
# Part 2 - all functions
#
# ----------------------------

def run_tree_check():
    option_max_deep = 2

    set_new_tree(os.getcwd(), 0, option_max_deep)

    print()
    print()

    if (open('.test.txt', 'r')).read() == (open('test.txt', 'r')).read():
        print(colored('##############', 'green'))
        print(colored('Same file tree', 'green'))
        print(colored('##############', 'green'))
    else:
        print(colored('##############', 'red'))
        print(colored('File tree has change', 'red'))
        print(colored('##############', 'red'))

        for added_file in get_diff(((open('.test.txt', 'r')).read()).split(';'), ((open('test.txt', 'r')).read()).split(';')):
            print(colored(' + : '+added_file, 'green'))

        for removed_file in get_diff(((open('test.txt', 'r')).read()).split(';'), ((open('.test.txt', 'r')).read()).split(';')):
            print(colored(' - : '+removed_file, 'red'))

        os.remove('test.txt')
        (open('test.txt', 'w')).write((open('.test.txt', 'r').read()))

    os.remove('.test.txt')


def set_new_tree(curDir: str, deep: int, max_deep: int):
    if deep != max_deep:
        deep_separator = ""
        for i in range(0, deep):
            deep_separator += "-"

        if deep == 0:
            print(colored('Actual position : ' + curDir, 'red'))

        with os.scandir(curDir) as it:
            for entry in it:
                f = open('.test.txt', 'a')
                if not entry.name.startswith('.'):
                    if entry.is_dir():
                        print(colored(deep_separator + entry.name, 'blue'))
                        f.write(deep_separator + entry.name + ';')
                        f.close()
                        set_new_tree(curDir + "/" + entry.name, 1 + deep, max_deep)
                    else:
                        print(colored(deep_separator + entry.name, 'green'))
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
    run_tree_check()
