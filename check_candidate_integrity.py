import argparse

import utils.downloader as d
import utils.loader as l


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Checks a candidate integrity.')

    parser.add_argument('input_json', help='Input crawled candidate .json file', type=str)

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    input_json = args.input_json

    # Defines some common use variables
    base_url = 'https://divulgacandcontas.tse.jus.br/'

    # Loads the input .json file
    data = l.load_json(input_json)

    # Iterates over every possible file
    for archive in data['arquivos']:
        # Creates the file's URL
        url = base_url + archive['url'] + archive['nome']

