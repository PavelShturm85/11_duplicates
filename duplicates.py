import os
import hashlib
import sys
from collections import defaultdict


def get_all_files(folder):
    all_files = defaultdict(list)
    for dirs, subdirs, files in os.walk(folder):
        for name in files:
            full_path_file = os.path.join(dirs, name)
            file_hash = hashlib.md5(open(full_path_file, 'rb').read()).digest()
            all_files[(file_hash, name)].append(full_path_file)
    return all_files


def get_duplicates(all_files):
    duplicates = defaultdict(list)
    for key in all_files:
        if len(all_files.get(key)) > 1:
            duplicates[key].append(all_files[key])
    return duplicates


def print_dublicates(duplicates):
    for key in duplicates:
        print('Duplicate files:{} \t {}'.format(
            key[1], ', '.join(duplicates[key][0])))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Enter the directory: ')

    all_files = get_all_files(input_file_name)
    duplicates = get_duplicates(all_files)
    print_dublicates(duplicates)
