import os
import re
import time

from pdfminer.high_level import extract_text
from selenium import webdriver


def crawl_candidate(id_city, id_candidate, sleep_time=5):
    """Crawls candidate information based on its identifiers.

    Args
        id_city (str): The city's identifier.
        id_candidate (str): The candidate's identifier.
        sleep_time (int): Amount of time to sleep.

    """

    print(f'Crawling information from candidate: {id_candidate}')

    # Creates the crawling URL
    url = f'http://divulgacandcontas.tse.jus.br/divulga/#/candidato/2020/2030402020/{id_city}/{id_candidate}'

    # Instantiates the driver, gets the URL, sleeps and retrieves the information
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)
    data = driver.execute_script("return sessionStorage.getItem('ngStorage-candidato');")

    # Closes the driver
    driver.close()

    # Defines the output file
    output_file = f'{id_candidate}.json'

    # Outputs the information to a .json file
    with open(output_file, 'w') as writer:
        writer.write(data)

    print(f'Information dumped to: {output_file}')


def extract_pdf(url, timeout=3):
    """Extracts a .pdf file from given URL.

    Args:
        url (str): URL of the .pdf file to be extracted.
        timeout (int): Timeout between operations (in seconds).

    """

    print(f'Extracting PDF from: {url}')

    # Creates a webdriver profile and defines some base preferences
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.download.folderList', 2)
    profile.set_preference('browser.download.dir', os.getcwd())
    profile.set_preference('browser.download.manager.closeWhenDone', True)
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference('browser.download.manager.useWindow', False)
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
    profile.set_preference('plugin.disable_full_page_plugin_for_types', 'application/pdf')
    profile.set_preference('pdfjs.disabled', True)

    # Instantiates the webdriver with the defined profile
    driver = webdriver.Firefox(firefox_profile=profile)

    # Sets a timeout when loading pages
    # This is a caveat for multiple files download
    driver.set_page_load_timeout(timeout)

    # Tries to execute the following block
    try:
        # Gets the URL (automatically downloads the file)
        driver.get(url)

    # When timeout exceeds
    except:
        # Closes the driver
        driver.close()

        print('PDF extracted.')


def extract_mother_name_from_pdf(file_path):
    """Extracts text from a given .pdf file.

    Args:
        file_path (str): Path to the .pdf file to be extracted.

    Returns:
        The stripped mother's name or an empty string.

    """

    print('Trying to find mother name ...')

    # Extracts the text from the .pdf
    text = extract_text(file_path)

    # Matches the text with an initial `filha` or `filho` keyword
    initial_match = re.search(r'(filha|filho).+', text)

    # If the text has been matched
    if initial_match:
        # Finds another substring that refers to the mother's name
        mother_name = re.search(r'\se(.*),', initial_match.group())

        print('Name has been found.')

        return mother_name.group(1).strip()

    print('Could not find name.')

    return None
