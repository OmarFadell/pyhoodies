<template>
    <div class="showroom">
      <div class="content">
        <p>Welcome to our showroom!</p>
        <p>Explore our exclusive collection of products.</p>
        <p>Find the perfect item for you.</p>
        <ProductGrid />
      </div>
    </div>
  </template>
  

<script>
import ProductGrid from './ProductGrid.vue';

export default {
    name: 'ShowRoom',
    components: {
        ProductGrid,
    },
};
</script>

<style scoped>
.showroom {
  
  margin: 0 auto;
  border: red 3px solid;
}

.content {
  width: 100%;
  /* max-width: 1200px; */
  padding: 2rem auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
</style>