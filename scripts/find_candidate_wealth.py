import argparse
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    # Creates the ArgumentParser
    parser = argparse.ArgumentParser(usage='Uses the parsed data to find candidates wealth.')

    parser.add_argument('input_parsed_file', help='Input parsed file identifier (.csv)', type=str)

    parser.add_argument('-delimiter', help='Delimiter identifier', type=str, default=';')

    return parser.parse_args()


def get_candidate_wealth(driver, id_city, id_candidate, sleep_time=5):
    """Gets the candidate wealth through a crawling process with selenium.

    Args:
        driver (webdriver): An webdriver child instance.
        id_city (str): The city's identifier.
        id_candidate (str): The candidate's identifier.
        sleep_time (int): Amount of time to sleep.

    Returns:
        The wealth of the searched candidate.

    """

    # Creates the URL to be requested
    url = f'http://divulgacandcontas.tse.jus.br/divulga/#/candidato/2020/2030402020/{id_city}/{id_candidate}/bens'

    # Gets the URL using the driver
    driver.get(url)

    # Sleeps a desired amount of time
    # This is a caveat for waiting the website loading time
    time.sleep(sleep_time)

    # Gathers the desired element
    wealth = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/section[3]/div/div/div[5]/div/div/span[1]')

    return wealth.get_attribute('innerHTML')


if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    input_parsed_file = args.input_parsed_file
    delimiter = args.delimiter

    # Loads the desired .csv file into a dataframe
    df = pd.read_csv(input_parsed_file, delimiter=delimiter, encoding='ISO-8859-1')

    # Instanciates the webdriver
    driver = webdriver.Firefox()

    # Applies an operation to every dataframe row
    df['BENS_CANDIDATO'] = df.apply(lambda row: get_candidate_wealth(driver, row['SG_UE'], row['SQ_CANDIDATO']),
                                    axis=1)

    # Outputs the post-processed dataframe to a new file
    df.to_csv(input_parsed_file, sep=delimiter, index=False)
