from numpy import load
import matplotlib as plt
import argparse

parser = argparse.ArgumentParser(description='plot numpy .npz file')
parser.add_argument('input_files', type=str, nargs='+')
args = parser.parse_args()

for f in args.input_files:
    data = load(f)
    lst = data.files
    for item in lst:
        print(item)
