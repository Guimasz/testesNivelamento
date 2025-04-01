# Operadoras de Plano de Saúde

Este projeto consiste em dois componentes:

- **Back-end:** API Flask que realiza a busca na planilha CSV.
- **Front-end:** Aplicação Vue 3 + Vite que consome a API.

## Pré-requisitos

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Node.js](https://nodejs.org/) (recomendado: LTS)
- [npm](https://www.npmjs.com/)

## Configurando o Back-end

1. **Instalar dependências**

   No terminal, acesse a pasta do back-end:

   ```bash
   cd /Users/guimas/Documents/Code/prosel/intuitiveCare/testesNivelamento
   ```

   Instale as dependências listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Verifique a estrutura**
   
   Certifique-se de que o arquivo da planilha (planilha.csv) se encontra na pasta `downloads`:
   
   ```
   testesNivelamento/
   ├── downloads/
   │   └── planilha.csv
   ├── src/
   │   ├── main.py
   │   └── services.py
   └── requirements.txt
   ```

3. **Inicie a API Flask**

   Execute o servidor:
   
   ```bash
   python src/main.py
   ```

   A API rodará (por padrão) em http://127.0.0.1:5000.

## Configurando o Front-end

1. **Instalar dependências**

   Acesse a pasta do front-end:

   ```bash
   cd /Users/guimas/Documents/Code/prosel/intuitiveCare/testesNivelamento/frontend
   ```

   Instale as dependências via npm:

   ```bash
   npm install
   ```

2. **Rodar o ambiente de desenvolvimento**

   Inicie o servidor de desenvolvimento do Vite:

   ```bash
   npm run dev
   ```

   A aplicação front-end estará disponível (por padrão) em http://localhost:5173.

## Testando a Integração

- Com o back-end rodando em `http://127.0.0.1:5000` e o front-end em `http://localhost:5173`, a aplicação Vue consumirá a rota `/buscar` da API.
- Para testar diretamente via Postman, use a rota:
  ```
  http://127.0.0.1:5000/buscar?termo=bradesco
  ```
- Certifique-se de que o CORS está ativo (já configurado no back-end via flask-cors) para permitir que a aplicação front-end acesse a API.

## Resumo da Estrutura de Pastas

```
testesNivelamento/
├── downloads/
│   └── planilha.csv
├── src/
│   ├── main.py             # API Flask
│   └── services.py         # Lógica da busca
├── requirements.txt
└── frontend/
    ├── index.html
    ├── package.json
    ├── README.md           # Front-end instructions (este arquivo)
    ├── vite.config.js
    └── src/
        ├── App.vue
        ├── main.js
        ├── style.css
        └── components/
            ├── SearchComponent.vue
            └── ResultCard.vue
```

## Observações

- Sempre que alterar o código, reinicie o servidor do back-end e/ou do front-end conforme necessário.
- Coleção postman em json está incluída no diretório