from flask import Flask, request, jsonify
from flask_cors import CORS 
from services import SearchService

app = Flask(__name__)
CORS(app)

CAMINHO_CSV = "downloads/planilha.csv"
search_service = SearchService(CAMINHO_CSV)

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo')
    if not termo:
        return jsonify({"erro": "O parâmetro 'termo' é obrigatório"}), 400

    resultado = search_service.search_text(termo)

    return jsonify({"resultados": resultado})

if __name__ == '__main__':
    app.run(debug=True)