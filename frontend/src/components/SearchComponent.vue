<template>
    <div>
      <input
        type="text"
        v-model="termo"
        placeholder="Digite o termo para buscar"
        @keyup.enter="buscar"
      />
      <button @click="buscar">Buscar</button>
  
      <div v-if="resultados.length">
        <h2>Resultados:</h2>
        <ul>
          <li v-for="(resultado, index) in resultados" :key="index">
            {{ resultado }}
          </li>
        </ul>
      </div>
  
      <div v-if="erro" class="error">
        {{ erro }}
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        termo: '',
        resultados: [],
        erro: '',
      };
    },
    methods: {
      async buscar() {
        this.resultados = [];
        this.erro = '';
        if (!this.termo) {
          this.erro = 'Por favor, insira um termo para buscar.';
          return;
        }
        try {
          const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${this.termo}`);
          console.log(response.data);
          this.resultados = response.data.resultados;
        } catch (error) {
          this.erro = 'Erro ao buscar os dados. Tente novamente.';
        }
      },
    },
  };
  </script>
  
  <style>
  input {
    padding: 10px;
    width: 300px;
    margin-right: 10px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #2b8619;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .error {
    color: red;
    margin-top: 20px;
  }
  </style>