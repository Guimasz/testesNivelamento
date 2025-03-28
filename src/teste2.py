import tabula
import pandas as pd
import os
from zipfile import ZipFile

class PDFTableExtractor:
    def __init__(self, caminho_pdf, pages='all'):
        self.caminho_pdf = caminho_pdf
        self.pages = pages
        
    def extract(self):
        if not os.path.exists(self.caminho_pdf):
            raise FileNotFoundError(f"⚠️ Arquivo PDF não encontrado: {self.caminho_pdf}")
        
        # Extrai as tabelas usando tabula-py
        # multiple_tables=True retorna uma lista de DataFrames
        df_list = tabula.read_pdf(self.caminho_pdf, pages=self.pages, multiple_tables=True)
        
        if not df_list:
            raise ValueError(f"⚠️ Nenhuma tabela encontrada no PDF: {self.caminho_pdf}")
        
        combined_df = pd.concat(df_list, ignore_index=True)
        return combined_df

class DataTransformer:
    def __init__(self, dict_colunas):
        """
        dict_colunas: dict com as chaves sendo os nomes abreviados e o valor a nova descrição.
        Ex.: {"OD": "Observação Detalhada", "AMB": "Atendimento Ambulatorial"}
        """
        self.dict_colunas = dict_colunas
        
    def transform(self, df: pd.DataFrame):
        return df.rename(columns=self.dict_colunas)

class CSVExporter:
    def __init__(self, caminho_csv):
        self.caminho_csv = caminho_csv
        
    def export(self, df: pd.DataFrame):
        dir_name = os.path.dirname(self.caminho_csv)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        
        if df.empty:
            raise ValueError("⚠️ DataFrame vazio, nada para exportar.")
        
        df.to_csv(self.caminho_csv, index=False)
        print(f"✅ CSV exportado para {self.caminho_csv}")
        return self.caminho_csv

class ZipCompressor:
    def __init__(self, caminho_zip):
        self.caminho_zip = caminho_zip
        
    def compress(self, caminho_arquivo):
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"⚠️ Arquivo para compactar não encontrado: {caminho_arquivo}")
        
        dir_name = os.path.dirname(self.caminho_zip)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
            
        with ZipFile(self.caminho_zip, "w") as zipf:
            zipf.write(caminho_arquivo, os.path.basename(caminho_arquivo))
        print(f"📦 Arquivo compactado como {self.caminho_zip}")
        return self.caminho_zip

def main(pdf_extractor: PDFTableExtractor, transformer: DataTransformer, 
         exporter: CSVExporter, compressor: ZipCompressor):
    df = pdf_extractor.extract()
    df_transformed = transformer.transform(df)
    csv_file = exporter.export(df_transformed)
    compressor.compress(csv_file)

if __name__ == "__main__":
    try:
        CAMINHO_PDF = "downloads/Anexo I.pdf"

        DICT_COLUNAS = {
            "OD": "Observação Detalhada",
            "AMB": "Atendimento Ambulatorial"
        }
        
        CAMINHO_CSV = "dados_rol.csv"
        CAMINHO_ZIP = "Teste_Guilherme_Araujo_De_Souza.zip"
        
        pdf_extractor = PDFTableExtractor(caminho_pdf=CAMINHO_PDF, pages='all')
        transformer = DataTransformer(dict_colunas=DICT_COLUNAS)
        exporter = CSVExporter(caminho_csv=CAMINHO_CSV)
        compressor = ZipCompressor(caminho_zip=CAMINHO_ZIP)
        
        main(pdf_extractor, transformer, exporter, compressor)
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")