<template>
  <div class="grid">
    <div class="product-grid">
      <Card href="/product"
        v-for="(product, index) in products"
        :key="index"
        :image="product.image"
        :title="product.title"
        :price="product.price"
        :isNew="product.isNew"
        :isFavorited="product.isFavorited"
      />
    </div>
  </div>
  </template>
  
  <script setup>
import Card from './Card.vue';  
  const products = [
    {
      image: '../src/assets/shirt.png',
      title: 'Mas Que Nada',
      price: 240,
      isNew: false,
      isFavorited: true
    },
    {
        image: '../src/assets/shirt.png',
      title: 'IRON VOLTAGE TOUR 2023',
      price: 240,
      isNew: true,
      isFavorited: false
    },
    {
        image: '../src/assets/shirt.png',
      title: 'DEATHCORE LEGENDS',
      price: 240,
      isNew: true,
      isFavorited: true
    },
    {
        image: '../src/assets/shirt.png',
      title: 'MOSH SEASON DROP',
      price: 240,
      isNew: false,
      isFavorited: false
    },
    {
        image: '../src/assets/shirt.png',
      title: 'EXCLUSIVE TOUR MERCH',
      price: 240,
      isNew: true,
      isFavorited: true
    },
    {
        image: '../src/assets/shirt.png',
      title: 'OG STREETWEAR',
      price: 240,
      isNew: false,
      isFavorited: false
    }
  ]

  defineProps({
    category: {
      type: String,
      required: true
    }
  })
  
  </script>
  <style scoped>
  
  .product-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr); 
    gap: 2rem;
    max-width: 1000px;
    margin-left: auto;
    
    /* border: 3px blue solid; */
    
  }

  .grid{
    display: block;
    /* border: 3px red solid; */
    margin: auto;
    justify-content: center;
    align-items: center;  
  }

  @media (max-width: 768px) {
    .product-grid {
      grid-template-columns: repeat(1, 1fr); /* Two columns on smaller screens */
      margin: auto 10px;
    }
  }
  </style>
  