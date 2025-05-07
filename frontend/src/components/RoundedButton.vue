<template>
    <div class="category-buttons">
      <button
        v-for="(category, index) in categories"
        :key="index"
        :class="['pill-button', { active: selected === category }]"
        @click="selectCategory(category)"
      >
        {{ category }}
      </button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const categories = ['NEW ARRIVALS', 'TSHIRT', 'CREWNECK', 'HOODIE & JACKET', 'ACCESSORIES']
  const selected = ref('NEW ARRIVALS')
  
  const selectCategory = (category) => {
    selected.value = category
    // emit an event if needed: defineEmits(['update:category'])
  }
  </script>
  
  <style scoped>
  .category-buttons {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    justify-content: center;
    padding: 16px;
  }
  
  .pill-button {
    padding: 10px 20px;
    border-radius: 999px;
    border: 1.5px solid #ccc;
    background-color: white;
    color: black;
    font-weight: 500;
    font-family: "Segoe UI", sans-serif;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  
  .pill-button:hover {
    background-color: #f0f0f0;
  }
  
  .pill-button.active {
    background-color: #1e40af; /* deep blue */
    color: white;
    border-color: #1e40af;
  }
  </style>
  