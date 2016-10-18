from os import walk, path
from collections import defaultdict
import argparse


def get_file_list(folder):
    file_list = defaultdict(list)
    for root, dirs, files in walk(folder):
        for file in files:
            file_list[file].append(root)
    return dict((k, v) for k, v in file_list.items() if len(v) > 1)


def convert_to_list(file_list):
    pair_list = []
    for file_name, dirs in file_list.items():
        file1 = path.join(dirs[0], file_name)
        file2 = path.join(dirs[1], file_name)
        pair_list.append([file1, file2])
    return pair_list


def compare_files(file1, file2):
    if path.getsize(file1) == path.getsize(file2):
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ищет дубликаты файлов в указанном каталоге')
    parser.add_argument('dirpath', help='укажите путь к каталогу')
    args = parser.parse_args()
    if path.isdir(args.dirpath):
        print('Ищем дубликаты файлов...')
        file_list = get_file_list(args.dirpath)
        pairs = convert_to_list(file_list)
        for pair in pairs:
            if compare_files(pair[0], pair[1]):
                print('Дубликаты: \n \t{} и {}'.format(pair[0], pair[1]))
