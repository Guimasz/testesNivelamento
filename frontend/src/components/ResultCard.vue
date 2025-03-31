<template>
    <div class="card">
      <p>{{ resultado }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      resultado: {
        type: String,
        required: true,
      },
    },
  };
  </script>
  
  <style>
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
    transition: transform 0.2s ease;
  }
  
  /* .card:hover {
    transform: scale(1.02);
  } */
  
  .card p {
    margin: 0;
    font-size: 16px;
    color: #333;
  }
  </style>