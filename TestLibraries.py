# ----------------------------
# Part 1 - import library
# 			and constant value
# -----------------------

# system library
import os
import sys
import begin
import argparse
from termcolor import colored
import logging
from logging.handlers import RotatingFileHandler


# constant


# ----------------------------
# Part 2 - all functions
#
# -----------------------

def test_os_library(curDir: str, deep: int):
    tabulation = ""
    for i in range(0, deep):
        tabulation += "-"

    if deep == 0:
        print(colored('Actual position : ' + curDir, 'red'))

    f = open('.test.txt', 'w')
    f.close()
    with os.scandir(curDir) as it:
        for entry in it:
            f = open('.test.txt', 'a')
            if not entry.name.startswith('.'):
                if entry.is_dir():
                    print(colored(tabulation + entry.name, 'blue'))
                    f.write(tabulation + entry.name)
                    f.close()
                    test_os_library(curDir + "/" + entry.name, 1 + deep)
                else:
                    print(colored(tabulation + entry.name, 'green'))
                    f.write(tabulation + entry.name)
                    f.close()


def test_logging_library():
    # création de l'objet logger qui va nous servir à écrire dans les logs
    logger = logging.getLogger()

    # on met le niveau du logger à DEBUG, comme ça il écrit tout
    logger.setLevel(logging.DEBUG)

    # création d'un formateur qui va ajouter le temps, le niveau
    # de chaque message quand on écrira un message dans le log
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # création d'un handler qui va rediriger une écriture du log vers
    # un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
    file_handler = RotatingFileHandler(log_file, 'a', 1000000, 1)

    # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
    # créé précédement et on ajoute ce handler au logger
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # création d'un second handler qui va rediriger chaque écriture de log
    # sur la console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    # Après 3 heures, on peut enfin logguer
    # Il est temps de spammer votre code avec des logs partout :
    logger.info('Hello')
    logger.warning('Testing %s', 'foo')


def test_file():
    if os.path.isfile('test.txt'):
        f = open('test.txt', 'r')
    else:
        f = open('test.txt', 'x')

    f_bis = open('test1.txt', 'r')

    print(f.read() == f_bis.read())
    f.close()
    os.remove('test.txt')
    f_bis.close()


# -----------------------
# Part 3 - main entry
# -----------------------
@begin.start
@begin.convert(refresh_time=int, max_deep=int, debug_mode=bool)
def run(log_file, refresh_time=15, max_deep=5, debug_mode=False):
    """
    """
    print(sys.version)
    test_os_library(os.getcwd(), 0)

    if (open('.test.txt', 'r')).read() == (open('test.txt', 'r')).read():
        print(colored('##############', 'green'))
        print(colored('Same file tree', 'green'))
        print(colored('##############', 'green'))
    else:
        print(colored('##############', 'red'))
        print(colored('File tree has change', 'red'))
        print(colored('##############', 'red'))
        (open('test.txt', 'w')).write((open('.test.txt', 'r').read()))
    os.remove('.test.txt')
    # test_file()



        # création de l'objet logger qui va nous servir à écrire dans les logs
    logger = logging.getLogger()

    # on met le niveau du logger à DEBUG, comme ça il écrit tout
    logger.setLevel(logging.DEBUG)

    # création d'un formateur qui va ajouter le temps, le niveau
    # de chaque message quand on écrira un message dans le log
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # création d'un handler qui va rediriger une écriture du log vers
    # un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
    file_handler = RotatingFileHandler(log_file, 'a', 1000000, 1)

    # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
    # créé précédement et on ajoute ce handler au logger
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # création d'un second handler qui va rediriger chaque écriture de log
    # sur la console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

    # Après 3 heures, on peut enfin logguer
    # Il est temps de spammer votre code avec des logs partout :
    logger.info('Hello')
    logger.warning('Testing %s', 'foo')

