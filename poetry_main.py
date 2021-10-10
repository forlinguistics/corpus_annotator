from txt2json import tsa_json
from csv import reader
import argparse
import os

if __name__ == '__main__':
    corpus_dir = 'corpus'
    meta_dir = 'corpus\\meta.csv'
    texts = os.listdir(corpus_dir)
    with open(meta_dir, 'r') as read_obj:
        csv_reader = reader(read_obj)
        cnt = 0
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:

                if row[0] in texts:
                    tsa_json(row, corpus_dir)
