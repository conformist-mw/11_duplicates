from os import walk, path, remove
from collections import defaultdict
import argparse


def get_file_list(folder):
    f_list = defaultdict(list)
    for root, dirs, files in walk(folder):
        for file in files:
            f_list[file].append(root)
    same = []
    for key in f_list:
        if len(f_list[key]) > 1:
            for f_path in f_list[key][1:]:
                same.append(are_files_duplicates(
                    path.join(f_list[key][0], key), path.join(f_path, key)))
    return same


def are_files_duplicates(file_path1, file_path_2):
    if path.getsize(file_path1) == path.getsize(file_path_2):
        return [file_path1, file_path_2]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ищет дубликаты файлов в указанном каталоге')
    parser.add_argument('dirpath', help='укажите путь к каталогу')
    args = parser.parse_args()
    if path.isdir(args.dirpath):
        print('Ищем дубликаты файлов...')
        lst = get_file_list(args.dirpath)
        for files in lst:
            print('Эти файлы одинаковы: {} и {}'.format(files[0], files[1]))
            print('Удаляем дубликат: {}'.format(files[1]))
            remove(files[1])
    else:
        print('{} не существует!'.format(args.dirpath))
