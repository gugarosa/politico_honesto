import pandas as pd


def load_csv(input_path, delimiter):
    """Loads a .csv file given an input path and a delimiter.

    Args:
        input_path (str): Input path to the .csv file.
        delimiter (str): Delimiter used in the .csv file.

    Returns:
        A dataframe holding the loaded .csv file.

    """

    print(f'Loading file from: {input_path}')

    # Loads a .csv using pandas
    df = pd.read_csv(input_path, delimiter=delimiter, encoding='ISO-8859-1')

    print('File loaded.')

    return df
