import time
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
