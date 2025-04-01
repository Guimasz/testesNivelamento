# Extração e Transformação de Tabelas em PDF

Este projeto fornece uma solução baseada em Python para extrair tabelas de arquivos PDF, transformar os dados, exportá-los para um arquivo CSV e compactar o resultado em um arquivo ZIP.

## Funcionalidades

- **Extração de Tabelas em PDF**: Extrai tabelas de arquivos PDF usando `tabula-py`.
- **Transformação de Dados**: Renomeia colunas com base em um dicionário fornecido.
- **Exportação para CSV**: Exporta os dados transformados para um arquivo CSV.
- **Compactação em ZIP**: Compacta o arquivo CSV em um arquivo ZIP.

## Requisitos

- Python 3.7+
- Dependências:
    - `tabula-py`
    - `pandas`

## Instalação

1. Clone o repositório:
     ```bash
     git clone <repository-url>
     cd <repository-folder>
     ```

2. Instale os pacotes Python necessários:
     ```bash
     pip install -r requirements.txt
     ```

3. Certifique-se de ter o Java instalado para que o `tabula-py` funcione.

## Uso

1. Coloque o arquivo PDF na pasta `downloads` e atualize a variável `CAMINHO_PDF` no script com o caminho do arquivo.

2. Atualize o dicionário `DICT_COLUNAS` com os mapeamentos de colunas que deseja aplicar.

3. Execute o script:
     ```bash
     python teste2.py
     ```

4. O arquivo CSV de saída e o arquivo ZIP serão gerados no diretório do projeto.

## Estrutura de Arquivos

```
/src
    └── teste2.py       # Script principal
/downloads
    └── Anexo I.pdf     # Exemplo de arquivo PDF de entrada
README.md             # Documentação do projeto
```

## Exemplo

Dado um arquivo PDF com tabelas, o script irá:

1. Extrair as tabelas em um único DataFrame.
2. Renomear as colunas com base no dicionário fornecido.
3. Exportar o DataFrame para um arquivo CSV.
4. Compactar o arquivo CSV em um arquivo ZIP.

## Tratamento de Erros

- O script verifica a ausência de arquivos e DataFrames vazios.
- Os erros são registrados com mensagens descritivas.

