import time

from selenium import webdriver


def check_integrity(cpf, name, mother_name, birth_date):
    """Checks the integrity of a candidate given its input parameters.

    Args:
        cpf (str): Candidate's CPF.
        name (str): Candidate's name.
        mother_name (str): Candidate's mother name.
        birth_date (str): Candidate's birth date.

    """

    print(f'Checking integrity from candidate: {name}')

    # Creates the checking URL
    url = 'https://consultaauxilio.dataprev.gov.br/consulta'

    # Instantiates the driver, gets the URL, sleeps and retrieves the information
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(5)

    # Fills the form elements
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div/input').send_keys(cpf)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div/div/input').send_keys(name)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[4]/div/div/input').send_keys(mother_name)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]/div[6]/div/div/div/input').send_keys(birth_date)

    # Still need to address the captcha solving mechanism
