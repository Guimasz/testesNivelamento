import pandas as pd

class SearchService:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def search_text(self, termo):
        try:
            df = pd.read_csv(self.caminho_arquivo, sep=';', encoding='utf-8') 
        except FileNotFoundError:
            return {"erro": "Arquivo da planilha não encontrado"}

        resultados = {}

        for coluna in df.columns:
            match = df[df[coluna].astype(str).str.contains(termo, na=False, case=False)]
            if not match.empty:
                resultados[coluna] = match[coluna].astype(str).tolist()

        return resultados if resultados else {"erro": "Nenhum resultado encontrado para a busca"}