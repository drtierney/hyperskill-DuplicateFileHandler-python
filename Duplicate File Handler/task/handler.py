import os
import argparse
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=None)
args = parser.parse_args()

if args.path is None:
    print("Directory is not specified")
    exit()

print("Enter file format:")
file_format = input().lower()

files_list = []
dupe_list = []
free_space = 0
for root, dirs, files in os.walk(args.path):
    files_list.extend([(os.path.join(root, file),
                        os.path.getsize(os.path.join(root, file)))
                       for file in files])

if file_format != "":
    files_list = [file for file in files_list if file[0].lower().endswith(f".{file_format}")]

print("\nSize sorting options:")
print("1. Descending")
print("2. Ascending")

print("\nEnter a sorting option:")
size_sort = input()
while size_sort not in ["1", "2"]:
    print("\nWrong option")
    size_sort = input()
print()

size_dict = {}
for pathname, size in files_list:
    size_dict.setdefault(size, []).append(pathname)

size_keys = sorted(size_dict, reverse=True) if int(size_sort) == 1 else sorted(size_dict)

for sk in size_keys:
    print(f"{sk} bytes")
    for v in size_dict[sk]:
        print(v)
    print()

print("\nCheck for duplicates?")
check_dupes = input()
while check_dupes not in ["yes", "no"]:
    print("Wrong option")
    check_dupes = input()
    print()
if check_dupes == "no":
    exit()

counter = 1
for sk in size_keys:
    hash_dict = {}
    hash_set = set()

    print(f"{sk} bytes")
    for v in size_dict[sk]:
        with open(v, "rb") as f:
            file_hash = hashlib.md5()
            file_hash.update(f.read())
            hash_dict.setdefault(file_hash.hexdigest(), []).append(v)
        for hash_value in hash_dict.keys():
            if len(hash_dict[hash_value]) > 1 and hash_value not in hash_set:
                print(f"Hash: {hash_value}")
                for filepath in hash_dict[hash_value]:
                    print(f"{counter}. {filepath}")
                    dupe_list.append([filepath, sk])
                    counter += 1
                hash_set.add(hash_value)
    print()

print("Delete files?")
delete_files = input()
while delete_files not in ["yes", "no"]:
    print("Wrong option")
    delete_files = input()
    print()
if delete_files == "no":
    exit()

print("Enter file numbers to delete:")
file_numbers = [x for x in input().split()]
while len(file_numbers) < 1 or any(not x.isdigit() for x in file_numbers):
    print("wrong format")
    file_numbers = [x for x in input().split()]
while max(int(x) for x in file_numbers) > (len(dupe_list)):
    print("wrong format")
    file_numbers = [x for x in input().split()]

for file_num in file_numbers:
    full_path = dupe_list[int(file_num) - 1][0]
    os.remove(full_path)
    free_space += dupe_list[int(file_num) - 1][1]

print(f"Total freed up space: {free_space} bytes")
