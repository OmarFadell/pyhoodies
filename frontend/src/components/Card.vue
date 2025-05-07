<template>
    <div class="product-card" @click="$router.push('/product')">
  
      
    <button @click="toggleFavorite" class="favorite-btn" href="/product">
        <span
        class="material-symbols-outlined"
        :style="{
          fontVariationSettings: `'FILL' ${isFavorited ? 1 : 0}, 'wght' 400, 'GRAD' 0, 'opsz' 24`,
          color: isFavorited ? 'black' : 'black'
        }"
      >
        favorite
      </span>
    </button>
  
      <img :src="image" :alt="title" class="product-image" />
  
      <div class="product-info">
        <p class="product-title">{{ title }}</p>
        <div class="product-meta">
          <span class="price">€ {{ price.toFixed(2) }}</span>
          <span v-if="isNew" class="new-badge">NEW</span>
        </div>
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
  object-fit: contain;
  margin-bottom: 1rem;
}

.product-info {
  text-align: left;
}

.product-title {
  font-size: 0.85rem;
  margin-bottom: 0.3rem;
  color: #3a3a3a;
  font-family: "Red Hat Display", sans-serif;
    font-weight: 700;
}

.product-meta {
  display: flex;
  align-items: center;
  gap: 8px;
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
    font-size: 1rem;
    margin: 0;
    font-weight: 900;
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