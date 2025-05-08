<template>
    <div class="product-card" @click="$router.push('/product')">
  
      
    
      <img :src="image" :alt="title" class="product-image" />
  
      <div class="product-info">
        <p class="product-title">{{ title }}</p>
        <div class="product-meta">
          <span class="price">€ {{ price }}</span>
          
        </div>
      </div>
    </div>
  </template>

<script setup>
const props = defineProps({
  image: String,
  title: String,
  price: [String, Number]
})
import { defineProps } from 'vue'
</script>

<style scoped>
.product-card {
  position: relative;
  border: 1px solid #e5e5e5;
  padding: 1rem;
  /* border-radius: 6px; */
  width: 250px;
  background: white;
  transition: transform 0.2s;
  
  
}

.product-card:hover {
  transform: scale(1.02);
}

.favorite-btn {
  position: absolute;
  top: 10px;
  left: 10px;
  background: white;
  border: none;
  border-radius: 50%;
  padding: 10px;
  cursor: pointer;
  font-size: 1rem;
}

.favorite-btn i {
  color: black;
}

.product-image {
  width: 100%;
  object-fit: cover;
  /* margin-bottom: 1rem; */
  max-height: 15rem;
}

.product-info {
  text-align: center;
}

.product-title {
  font-size: 1.1rem;
  margin-bottom: 0.3rem;
  color: #000000;
  /* font-family: "Red Hat Display", sans-serif; */
  font-family: "playfair display", serif;
  text-align: center;
    font-weight: 500;
}

.product-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  text-align: center;
  width: 100%;
  justify-content: center;
}

.price {
  font-weight: bold;
  color:black;
  font-family: "Red Hat Display", sans-serif;
  text-align: center;
  
}

.new-badge {
  background-color: black;
  color: white;
  font-size: 0.65rem;
  padding: 3px 6px;
  border-radius: 12px;
  text-transform: uppercase;
}

@media (max-width: 768px) {
  .product-card {
    width: 100%;
    display: flex;
    flex-direction: column;
    /* padding: 0.5rem; */
    height: 50vh;
    
    
  }

  .product-image {
    max-height: 20rem;
    margin-bottom: 0.5rem;
  }
/* 
  .product-title {
    font-size: 1rem;
    margin: 0;
  
  }

  .price {
    font-size: 1rem;
  }

  .new-badge {
    font-size: 0.6rem;
    padding: 2px 4px;
  }

  .product-image {
    width: 100%;
    
    
     }

  .product-card{
    padding: 0;
  }
  .product-image{
    margin: 0;
  } */
}

</style>