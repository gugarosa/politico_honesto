import argparse
from datetime import datetime

import utils.checker as c
import utils.extractor as e
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

        # Extracts the .pdf file
        e.extract_pdf(url)

        # Extracts the mother's name from the .pdf file
        mother_name = e.extract_mother_name_from_pdf(archive['nome'])

        # If the name exists
        if mother_name:
            # Breaks the loop
            break

    # Prints out meta-information about the candidate
    # for further checking at https://consultaauxilio.dataprev.gov.br/consulta
    print(f"CPF: {data['cpf']}")
    print(f"Nome Completo: {data['nomeCompleto']}")
    print(f"Nome da Mãe: {mother_name}")
    print(f"Data de Nascimento: {datetime.fromtimestamp(data['dataDeNascimento']/1000).strftime('%d/%m/%Y')}")
    print(f"Total de Bens: {data['totalDeBens']}")
