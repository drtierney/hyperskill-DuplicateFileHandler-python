import os
import argparse
from os.path import getsize

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=None)
args = parser.parse_args()

if args.path is None:
    print("Directory is not specified")
else:
    print("Enter file format:")
    file_format = input()

    print("\nSize sorting options:")
    print("1. Descending")
    print("2. Ascending")

    print("\nEnter a sorting option:")
    size_sort = input()
    while size_sort not in ["1", "2"]:
        print("\nWrong option")
        size_sort = input()
    print()
    files_list = []
    for root, dirs, files in os.walk(args.path):
        if file_format == "":
            files_list.extend([(os.path.join(root, file),
                                getsize(os.path.join(root, file)))
                               for file in files])
        else:
            files_list.extend([(os.path.join(root, file),
                                getsize(os.path.join(root, file)))
                               for file in files if file.endswith(f".{file_format}")])

    size_dict = {}
    for pathname, size in files_list:
        size_dict.setdefault(size, []).append(pathname)

    if int(size_sort) == 1:
        size_keys = sorted(size_dict, reverse=True)
    else:
        size_keys = sorted(size_dict)

    for sk in size_keys:
        print(f"{sk} bytes")
        for v in size_dict[sk]:
            print(v)
        print()
