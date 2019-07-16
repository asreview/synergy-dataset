import os
import argparse

import pandas as pd
from RISparser import read


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('input_file', help='Input file location')
parser.add_argument('export_file', help='Export file location')


def parse_articles(filepath, encoding='utf-8'):
    """Parse an article in RIS format."""

    with open(filepath, 'r', encoding=encoding) as bibliography_file:
        filelines = bibliography_file.readlines()
        entries = list(read(filelines))

    return entries


if __name__ == '__main__':

    args = parser.parse_args()

    # filepath = os.path.join('example_dataset_1', 'demo.txt')
    input_fp = args.input_file
    print("Input file:", input_fp)

    # parse articles
    articles = parse_articles(input_fp)
    print("Number of articles:", len(articles))

    # make export dir
    output_pf = args.export_file
    if not os.path.exists(os.path.dirname(output_pf)):
        os.makedirs(os.path.dirname(output_pf))

    # export articles
    print("Export file:", output_pf)
    articles = pd.DataFrame(articles)

    if output_pf.endswith('.csv'):
        articles.to_csv(output_pf.replace('.txt', '.csv'), index=False)
    elif output_pf.endswith('.json'):
        articles.to_json(output_pf.replace('.txt', '.json'))
    else:
        raise ValueError("file format unknown")
