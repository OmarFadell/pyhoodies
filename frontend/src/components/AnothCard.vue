<template>
    <div class="product-card">
    
  
      <img :src="image" :alt="title" class="product-image" />
  
      <div class="product-info">
        <p class="product-title">{{ title }}</p>
        <p class="price">€ {{ price.toFixed(2) }}</p>
      </div>
    </div>
  </template>

<script setup>

defineProps({
  image: String,
  title: String,
  price: Number,
  isNew: Boolean,
  isFavorited: Boolean
})

const emit = defineEmits(['toggle-favorite'])

function toggleFavorite(){
    emit('toggle-favorite')
}

</script>

<style scoped>
.product-card {
  position: relative;
  border: 1px solid #e5e5e5;
  /* padding: 1rem; */
  /* border-radius: 6px; */
  width: 320px;
  background: white;
  transition: transform 0.2s;
  height: 540px;
  
  
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
  object-fit:cover;
  /* margin-bottom: 1rem; */
  height: 400px;
}

.product-info {
  text-align: center;
  /* margin-top: -20px; */
  
  /* background-color: white;
  border: 1px red solid; */
}

.product-title {
  font-size: 2rem;
  margin-bottom: 0.3rem;
  color: #3a3a3a;
  font-family: "Red Hat Display", sans-serif;
    font-weight: 900;
    line-height: 1rem;
    
}


.price {
  font-weight: bold;
  color:black;
  
  
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
    padding: 0.5rem;
    
  }

  .product-title {
    font-size: 2.5rem;
    margin: 0;
    font-weight: 900;
    margin-top: 20px;
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
    height: auto;
  }

  .product-card{
    padding: 0;
  }
  .product-image{
    margin: 0;
  }
}

</style>