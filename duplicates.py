from os import walk, path
from collections import defaultdict


def get_file_list(folder):
    f_list = defaultdict(list)
    for root, dirs, files in walk(folder):
        for file in files:
            f_list[file].append(root)
    same = []
    for key in f_list:
        if len(f_list[key]) > 1:
            same.append(are_files_duplicates(path.join(f_list[key][0], key),
                                             path.join(f_list[key][1], key)))
    return same


def are_files_duplicates(file_path1, file_path_2):
    if path.getsize(file_path1) == path.getsize(file_path_2):
        return [file_path1, file_path_2]


if __name__ == '__main__':
    pass
