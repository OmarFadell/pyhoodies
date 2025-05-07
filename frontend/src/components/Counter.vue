<template>
    <div class="quantity-counter">
      <button @click="decrease">−</button>
      <span>{{ quantity }}</span>
      <button @click="increase">+</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  // Reactive quantity value
  const quantity = ref(1)
  
  function increase() {
    quantity.value++
  }
  
  function decrease() {
    if (quantity.value > 1) quantity.value--
  }
  </script>
  
  <style scoped>
.quantity-counter {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 140px;
  padding: 0.3rem 0.5rem;
  border-radius: 9999px; /* more pill-like */
  border: 2px solid #ccc;
  font-size: 1.5rem;
  font-weight: bold;
  background-color: #f9f9f9;
}

.quantity-counter button {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  width: 2.5rem;
  height: 2.5rem;
  font-size: 1.5rem;
  cursor: pointer;
  user-select: none;
  color: black;
}

.quantity-counter span {
  width: 2rem;
  text-align: center;
}
  </style>
  