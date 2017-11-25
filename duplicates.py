import os
import hashlib
import sys


def find_duplicates(folder):
    duplicates = {}
    for dirs, subdirs, files in os.walk(folder):
        for name in files:
            full_path_file = os.path.join(dirs, name)
            file_hash = hashlib.md5(open(full_path_file, 'rb').read()).digest()
            duplicat = duplicates.get(file_hash)
            if duplicat:
                try:
                    duplicates[file_hash][name].append(full_path_file)
                except KeyError:
                    duplicates[file_hash][name] = [full_path_file]
            else:
                duplicates[file_hash] = {name: [full_path_file]}
    return duplicates


def print_dublicates(dublicates):
    for file_hash in duplicates:
        for full_path_file in duplicates[file_hash]:
            if len(duplicates[file_hash][full_path_file]) > 1:
                print('Duplicate files: {}'.format(
                    ', '.join(duplicates[file_hash][full_path_file])))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Enter the directory: ')

    duplicates = find_duplicates(input_file_name)
    print_dublicates(duplicates)
