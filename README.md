# Político-Honesto: Consultas de Auxílio Emergencial

*Este repositório utiliza um processo de automação para extrair dados funcionais do [TSE](https://divulgacandcontas.tse.jus.br/divulga) e fornecer meta-informações necessárias para verificar se um determinado candidato realizou o pedido do auxílio emergencial.*

---

## Instruções do Repositório

### Instalação

Todos os requisitos necessários para instalar o repositório estão disponíveis com o seguinte comando:

```Python
pip install -r requirements.txt
```

### Arquivo de Configuração (Não Implementado)

Por favor, copie `config.ini.example` para `config.ini` e preenche a chave de API do 2Captcha.

*Note que esta etapa ainda não é necessária, pois a consulta final está sendo feita de forma manual.*

---

## Utilização

### Recuperação de Dados do TSE

O primeiro passo é recuperar os dados de todas as candidaturas presentes e disponíveis no site do TSE. Para facilitar a vida do usuário, nós disponibilizamos este arquivo em nossa [plataforma](https://www.recogna.tech/files/politico_honesto/consulta_cand_2020_BRASIL.csv).

Com o arquivo em mãos, é possível limpá-lo e utilizar apenas as informações necessárias para extrair novos dados de um candidato em particular. Tal procedimento pode ser realizado de acordo com o script a seguir:

```Python
python clean_tse_data.py
```

*Também disponibilizamos a versão limpa do arquivo em nossa [plataforma](https://www.recogna.tech/files/politico_honesto/clean_consulta_cand_2020_BRASIL.csv).*

### Extração de Informações do Candidato

Com o arquivo de candidaturas em mãos, é possível abrí-lo e pesquisar pelo candidato desejado. Note que existem vários campos passíveis de serem pesquisados, tais como município, nome do candidato, CPF, e-mail, dentre outros.

As colunas necessárias para a realização do presente passo são: `SG_UE` (código do município no TSE) e `SQ_CANDIDATO` (código do candidato no TSE).

Com estas informações em mãos, podemos utilizar o script a seguir:

```Python
python crawl_candidate_information.py <SG_UE> <SQ_CANDIDATO>
```

*Este script irá gerar um arquivo JSON contendo todas as informações do candidato disponíveis no site do TSE.*

### Verificação de Integridade

Finalmente, com o arquivo JSON em mãos, é possível rodar o último script e extrair as informações necessárias para verificar se o candidato realizou a solicitação do auxílio emergencial, disponível para consulta no [DataPrev](https://consultaauxilio.dataprev.gov.br/consulta).

Invoque o script a seguir, passando como parâmetro o arquivo JSON gerado no passo anterior:

```Python
python check_candidate_integrity.py <JSON_FILE>
```

O script irá gerar as seguintes meta-informações: CPF, nome do candidato, nome da mãe do candidato e data de nascimento, as quais são necessárias para realizar a consulta do auxílio emergencial. Adicionalmente, ele também irá mostrar a quantia de bens declarados do candidato em questão.

*Note que o robô de consulta automática no site da DataPrev ainda não está disponível devido ao tempo de resolução do CAPTCHA presente no site. Portanto, é necessário introduzir as informações de forma manual.* 

---

## Suporte

Apesar de tentarmos realizar o nosso melhor, é inevitável que possam existir erros ou bugs. Caso você deseje reportar um bug ou problema, fale conosco! Estamos disponíveis neste mesmo repositório ou através do e-mail: gustavo.rosa@unesp.br.

---
