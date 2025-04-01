# Projeto - Teste 1

Este projeto é um teste que automatiza as seguintes tarefas:

- Buscar links de arquivos específicos (baseado em nomes parciais e extensão) a partir de uma página web.
- Baixar os arquivos identificados para uma pasta local.
- Compactar os arquivos baixados em um arquivo ZIP.

## Pré-requisitos

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Instalação e Configuração

1. **Clone o repositório e acesse o diretório do projeto:**

    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    cd testesNivelamento
    ```

2. **Baixar Dependências**

    Instale as dependências necessárias utilizando o pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Executando o Projeto**

    Para rodar o teste, execute o script principal que realiza a busca, o download e a compactação dos arquivos:

    ```bash
    python src/teste1.py
    ```

4. **Fluxo de Execução**

    - O script acessa a página configurada e busca pelos links dos arquivos desejados.
    - Os arquivos são baixados para uma pasta local.
    - Por fim, os arquivos baixados são compactados em um arquivo ZIP.

5. **Mensagens e Logs**

    Durante a execução, o terminal exibirá mensagens indicando o sucesso ou possíveis erros em cada etapa.
