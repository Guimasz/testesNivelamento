import os
import teste1

# Novas constantes definidas no main.py
URL_SITE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

ARQUIVOS_DESEJADOS = ['Anexo I', 'Anexo II']
TIPO_ARQUIVO = ".pdf"
PASTA_DOWNLOADS = "downloads"

def main():
    os.makedirs(PASTA_DOWNLOADS, exist_ok=True)

    # Instancia as classes com as constantes definidas no main.py
    scraper = teste1.WebScrapper(url=URL_SITE, arquivos=ARQUIVOS_DESEJADOS, tipo=TIPO_ARQUIVO)
    downloader = teste1.Downloader(PASTA_DOWNLOADS, tipo_arquivo= TIPO_ARQUIVO)

    # Chama a função main() do teste1
    teste1.main(scraper, downloader)
    
    
if __name__ == "__main__":
    main()