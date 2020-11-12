import argparse

import utils.extractor as e


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    # Creates the ArgumentParser
    parser = argparse.ArgumentParser(usage='Crawls information from a candidate.')

    parser.add_argument('id_city', help='City identifier', type=str)

    parser.add_argument('id_candidate', help='Candidate identifier', type=str)

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    id_city = args.id_city
    id_candidate = args.id_candidate

    # Extracts candidate's information
    e.crawl_candidate(id_city, id_candidate)
