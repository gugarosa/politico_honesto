import utils.downloader as d
import utils.loader as l

# Defines some common use variables
url = 'https://www.recogna.tech/files/politico_honesto/consulta_cand_2020_BRASIL.csv'
file_path = 'consulta_cand_2020_BRASIL.csv'
delimiter = ';'

# Downloads the original TSE .csv file
d.download_file(url, file_path)

# Loads the desired .csv file into a dataframe
df = l.load_csv(file_path, delimiter)

# Defines the columns to be extracted (will be fixed for now)
columns = ['SG_UE', 'NM_UE', 'DS_CARGO', 'SQ_CANDIDATO', 'NR_CANDIDATO',
           'NM_CANDIDATO', 'NR_CPF_CANDIDATO', 'DT_NASCIMENTO', 'NM_EMAIL']

print('Starting to clean the file ...')

# Gathers the desired set of columns
cleaned_df = df[columns]

# Outputs the extracted dataframe to a new file
cleaned_df.to_csv('clean_' + file_path, sep=delimiter, index=False)

print('File cleaned and saved.')
