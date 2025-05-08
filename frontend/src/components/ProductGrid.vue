<template>
  <div class="grid">
    <div class="product-grid" v-if="!store.loading">
      <Card
        href="/product"
        v-for="(product, index) in store.products"
        :key="index"
        :image="product.image_url"
        :title="product.name"
        :price="product.price"
      />
    </div>

    <div class="homecarousel" v-if="!store.loading">
      <Carousel v-bind="carouselConfig">
        <Slide v-for="(product, index) in store.products" :key="index">
          <div class="carousel__item">
            <Card
              :image="product.image_url"
              :title="product.name"
              :price="product.price"
            />
          </div>
        </Slide>

        <template #addons>
          <Navigation />
          <Pagination />
        </template>
      </Carousel>
    </div>

    <div class="product-grid">
      <SkelatonCard v-if="store.loading" v-for="n in 6" :key="n" />
    </div>
  </div>
</template>


<script setup>
import Card from './Card.vue'
import SkelatonCard from './SkelatonCard.vue'
import { useProductStore } from '../productStore.js'
import 'vue3-carousel/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

const store = useProductStore()

const carouselConfig = {
  wrapAround: true,
  breakpoints: {
    0: { itemsToShow: 1 },
    768: { itemsToShow: 2 },
    1024: { itemsToShow: 5 }
  }
}
</script>

  <style scoped>

  .homecarousel {
    display: none;
    margin: auto 10px;
    width: 100%;
    height: 100%;
  }

  .loading-message {
    text-align: center;
    font-size: 1.5rem;
    color: #555;
    margin-top: 2rem;
  }
  
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
      display: none;
    }
    
    .homecarousel {
      display: block;
      margin: auto 10px;
      width: 100%;
      height: 100%;
    }
    .homecarousel .carousel__item {
      width: 100%;
      height: 50vh;
    }

  }
  </style>
  