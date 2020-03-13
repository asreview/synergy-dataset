import os
import argparse

import pandas as pd
from RISparser import read


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Process RIS files into CSV ones.')
    parser.add_argument('input_fp', help='Input file location')
    parser.add_argument('output_fp', help='Export file location')
    args = parser.parse_args()
    return vars(args)


def parse_articles(filepath, encoding='utf-8'):
    """Parse an article in RIS format."""

    with open(filepath, 'r', encoding=encoding) as bibliography_file:
        filelines = bibliography_file.readlines()
        entries = list(read(filelines))

    return entries


def convert_ris_to_csv(input_fp, output_fp):
    print("Input file:", input_fp)

    # parse articles
    articles = parse_articles(input_fp)
    print("Number of articles:", len(articles))

    # make export dir
    if not os.path.exists(os.path.dirname(output_fp)):
        os.makedirs(os.path.dirname(output_fp))

    # export articles
    print("Export file:", output_fp)
    articles = pd.DataFrame(articles)

    if output_fp.endswith('.csv'):
        articles.to_csv(output_fp.replace('.txt', '.csv'), index=False)
    elif output_fp.endswith('.json'):
        articles.to_json(output_fp.replace('.txt', '.json'))
    else:
        raise ValueError("file format unknown")


if __name__ == '__main__':
    args = parse_arguments()
    convert_ris_to_csv(**args)
    input_fp = args.input_file
