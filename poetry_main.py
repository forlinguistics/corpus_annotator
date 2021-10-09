from txt2json import tsa_json
from csv import reader
import argparse
import os
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus_dir", default='corpus')
    parser.add_argument("--meta_dir", default='corpus\\meta.csv')
    args = parser.parse_args()
    corpus_dir = args.corpus_dir
    meta_dir = args.meta_dir
    print(meta_dir)
    print(corpus_dir)
    texts = os.listdir(corpus_dir)
    with open(meta_dir, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                if row[0] in texts:
                    tsa_json(row, corpus_dir)

