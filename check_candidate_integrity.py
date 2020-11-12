import argparse

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

    # Loads the input .json file
    data = l.load_json(input_json)
