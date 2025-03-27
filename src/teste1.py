import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from urllib.parse import urljoin

# configurando o ambiente
PASTA_DOWNLOADS = "downloads"
URL_SITE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
ARQUIVOS_DESEJADOS = ['Anexo I', 'Anexo II']
TIPO_ARQUIVO = ".pdf" # alterar para procurar tipo diferente de arquivo





#Classe para extrair links de uma página web
class WebScrapper:
    def __init__(self, URL_SITE):
        self.url = URL_SITE
        
    def get_links(self):
        
        anexos_encontrados = {} # dicionario para armazenar os links dos arquivos encontrados
        anexos_pendentes = set(ARQUIVOS_DESEJADOS) #arquivos que ainda não foram encontrados
        
        try:
            response = requests.get(self.url)# recupera a página
            response.raise_for_status()# lança uma exceção se a resposta não for bem sucedida
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all("a", href=True) #encontra todos os elementos <a> que possuem o atributo href, ou seja, os links
            
            
            
            for link in links: 
                # Se a lista de pendentes estiver vazia, finaliza a busca
                if not anexos_pendentes:
                    break

                # ignora se a url não termina com o tipo de arquivo desejado
                if not link["href"].endswith(TIPO_ARQUIVO):
                    continue
                
                for nome_arquivo in ARQUIVOS_DESEJADOS:   
                    # atribui apenas o primeiro link encontrado para o nome do arquivo
                    if nome_arquivo in anexos_encontrados:
                        continue
                    # verifica se o nome do arquivo desejado está no texto do elemento com link e se o link termina com o tipo de arquivo desejado  
                    if nome_arquivo.lower() in link.text.lower():
                        url_completo = urljoin(self.url, link["href"]) 
                        anexos_encontrados[nome_arquivo] = url_completo # atribui o link ao nome do arquivo
                        anexos_pendentes.remove(nome_arquivo) #atualiza a lista de pendentes
                        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar links {self.url}: {e}")           
        return anexos_encontrados # dicionario com nome do arquivo e o link completo dele
    
# classe responsavel por gravar um arquivo em uma pasta    
class Downloader:
    def __init__(self, pasta_destino):
        self.pasta_destino = pasta_destino
    
    def download_arquivo(self, url, nome_arquivo):
        nome_arquivo = f"{nome_arquivo}{TIPO_ARQUIVO}" # adiciona a extensão do arquivo ao nome
        
        caminho = os.path.join(self.pasta_destino, nome_arquivo)
        try:
            resposta = requests.get(url, stream=True) # permite baixar or arquivo em partes (chunks)
            
            if resposta.status_code == 200:
                with open(caminho, "wb") as arquivo:# abre o arquivo para escrita 
                    for chunk in resposta.iter_content(1024): # baixa o arquivo em partes de 1024 bytes
                        arquivo.write(chunk)
                print(f"✅ Arquivo {nome_arquivo} baixado com sucesso!")
                return caminho #retorna onde o arquivo foi salvo
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao baixar o arquivo {nome_arquivo}: {e}")
            return None
            
        
# classe responsavel por compactar arquivos em zip        
class Compactador:  
    @staticmethod
    def compactar_arquivos(arquivos, nome_zip): #recebe o caminho dos arquivos e o nome do arquivo zip
        
        if not arquivos:
            print("Nenhum arquivo para compactar!")
            return None
        try:    
            with ZipFile(nome_zip, "w") as zipf:
                for arquivo in arquivos:
                    zipf.write(arquivo)
                print(f"📦 Arquivos compactados com sucesso em {nome_zip}!")
                return nome_zip # retorna o caminho do arquivo compactado
        except Exception as e:  
            print(f"❌ Erro ao compactar arquivos: {e}")
            return None
        
 # execucao do programa
def main():
    scraper = WebScrapper(URL_SITE) # instancia o WebScrapper com a url configurada
    
    # criando a pasta de downloads se não existir
    os.makedirs(PASTA_DOWNLOADS, exist_ok=True)
    
    downloader = Downloader(PASTA_DOWNLOADS) # instancia o Downloader com a pasta de downloads configurada
    
    # Passo 1: Acha os links dos arquivos desejados
    anexos = scraper.get_links() 
    
    # Passo 2: Baixa os arquivos
    arquivos_baixados = []
    for nome_arquivo, url in anexos.items():
         local_arquivo = downloader.download_arquivo(url, nome_arquivo)
         if local_arquivo:
             arquivos_baixados.append(local_arquivo)
    
     # Passo 3: Compacta os arquivos baixados
    Compactador.compactar_arquivos(arquivos_baixados, "arquivos.zip")
            
            
            
if __name__ == "__main__":
    main()