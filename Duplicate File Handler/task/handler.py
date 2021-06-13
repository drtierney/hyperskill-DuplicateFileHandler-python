import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=None)
args = parser.parse_args()

if args.path is None:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(args.path):
        for name in files:
            print(os.path.join(root, name))
