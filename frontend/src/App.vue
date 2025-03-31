<template>
  <div id="app">
    <h1 class="titulo">Operadoras de Plano de Saúde</h1>
    <SearchComponent />
  </div>
</template>

<style scoped>
.titulo {
  font-size: 3em; 
  text-align: center;
  margin-bottom: 20px;
}
</style>

<script>
import SearchComponent from './components/SearchComponent.vue';

export default {
  components: {
    SearchComponent,
  },
};
</script>