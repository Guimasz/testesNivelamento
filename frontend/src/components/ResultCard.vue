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
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }
  
  .card p {
    margin: 0;
    font-size: 18px;
    color: #333;
    font-weight: 500;
    text-align: center;
  }
  </style>