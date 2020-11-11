import argparse

import pandas as pd


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    # Creates the ArgumentParser
    parser = argparse.ArgumentParser(usage='Parses TSE data into a more readable .csv file.')

    parser.add_argument('input_file', help='Input file identifier (.csv)', type=str)

    parser.add_argument('output_file', help='Output file identifier (.csv)', type=str)

    parser.add_argument('-delimiter', help='Delimiter identifier', type=str, default=';')

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    input_file = args.input_file
    output_file = args.output_file
    delimiter = args.delimiter

    # Defines the columns to be extracted (will be fixed for now)
    columns = ['SG_UE', 'NM_UE', 'DS_CARGO', 'SQ_CANDIDATO', 'NR_CANDIDATO',
               'NM_CANDIDATO', 'NR_CPF_CANDIDATO', 'DT_NASCIMENTO', 'NM_EMAIL']

    # Loads the desired .csv file into a dataframe
    df = pd.read_csv(input_file, delimiter=delimiter, encoding='ISO-8859-1')

    # Gathers the desired set of columns
    parsed_df = df[columns]

    # Outputs the extracted dataframe to a new file
    parsed_df.to_csv(output_file, sep=delimiter, index=False)
