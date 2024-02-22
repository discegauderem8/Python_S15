# 📌Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл, ○ флаг каталога, ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import os
from collections import namedtuple
import logging


logger = logging.getLogger(__name__)
my_format = '{levelname:<10} - {asctime:<20}: {msg}'
logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
                    level=logging.INFO, style='{', format=my_format)

def get_dir_info(path: str) -> [namedtuple]:

    result = []
    FileData = namedtuple("FileData", ["name", "extension", "parent_dir"])

    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            item = FileData(dirname, "folder", full_path.split("\\")[-2])
            result.append(item) #Прим: "\\" означает \
            # (В питоне нельзя написать просто "\", так это символ экранирования (регулярные выражения)
            logger.info(f"Обнаружен каталог {item.name} в директории {item.parent_dir}")

        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            item = FileData(filename.split(".")[0], full_path.split(".")[-1], full_path.split("\\")[-2])
            result.append(item)
            logger.info(f"Обнаружен файл {item.name} c разрешением {item.extension} в директории {item.parent_dir}")

    return result


parser = argparse.ArgumentParser(description="Парсер аргументов")
parser.add_argument("path", metavar=".../.../.../target_folder или ./target_folder", type=str, nargs=1,
                    help="Для корректной работы программы вызовите ее из терминала,"
                         "и через пробел укажите путь до папки")

parsed_args = parser.parse_args()
PATH = parsed_args.path[0]

(f"В скрипт передано {PATH}")

get_dir_info(PATH)

# py S15_HW.py ..\S15
