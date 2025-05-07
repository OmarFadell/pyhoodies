<script setup>
import HeroSection from '../components/HeroSection.vue';
import belt from '../components/belt.vue';
import ProductGrid from '../components/ProductGrid.vue';
import ShowRoom from '../components/ShowRoom.vue';
import {ref} from 'vue';

const categories = ['NEW ARRIVALS', 'TSHIRT', 'CREWNECK', 'HOODIE & JACKET', 'ACCESSORIES'];
const selectedCategory = ref('NEW ARRIVALS');
</script>

<template>
  <HeroSection />
 
 
      <div class="three-column-layout">
    <div class="column"> </div>
    <div class="columnOne">
      
      <div class="titles">
        <p class="tagline">DROP 001 OUT NOW</p>
        <h1 class="title">Built for the Streets, Backed by the Squad</h1>
        <p class="bottomline">This drop is a tribute to the streets—where loyalty runs deep and style speaks louder than words. Crafted for the crew that moves in unison, each piece embodies the raw energy of the block. Limited in quantity but limitless in impact, it's time to gear up and make your statement.​</p>
      </div>
      <!-- <div class="button-group">
        <button
          v-for="category in categories"
          :key="category"
          :class="['cta-button-group', { active: selectedCategory === category }]"
          @click="selectedCategory = category"
        >
          {{ category }}
        </button>
    </div> -->
    </div>
    
    
    <div class="column"> </div>
  </div>


  <div class="three-column-layout">
  <div class="column"></div>
  <div class="columnOne">
    <ProductGrid category="hello"/>
    
  </div>
  <div class="column"></div>
</div>
  
</template>

<style scoped>
.bg{
  background-image: url('../assets/gradientt.png');
  background-size: cover;
  background-repeat: no-repeat;
  margin-top: -20px;
}
.home-page {
  display: column;
}

.showroom {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  margin: 0 auto;
}

.titles {
  text-align: center;
  margin-top: 20px;
  font-family: "Red Hat Display", sans-serif;
  color: #3a3a3a;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: auto;
  margin-left: auto;
  width: 100%;
}

.three-column-layout {
  display: flex;
  width: 100vw; /* Ensures the container spans the full viewport width */
  justify-content: space-between;
  margin-top: 20px;
  margin-left: 0; /* Reset any left margin */
}

.column,
.columnOne {
  flex: 1 0 1; /* Allows columns to grow and shrink equally */
  padding: 20px;
  /* border: 1px solid #ddd; */
  text-align: center;
  min-width: 100px;
  box-sizing: border-box; /* Includes padding and border in the element's total width and height */
}

.titles {
  text-align: center;
  font-family: "Red Hat Display", sans-serif;
  /* font-weight: 700; */
  color: #3a3a3a;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* Centers content horizontally and vertically */
  width: 100%;
  line-height: 1px;
  margin: 0 auto; /* Centers the container horizontally */
  font-weight: 400;
}

.tagline{
  font-size: 1.5rem;
  font-weight: 900;
  margin-bottom: -0.6rem;
  
}

.bottomline{
  font-size: 1.2rem;
  font-weight: 500;
  margin-top: -0.5rem;
  color: #3a3a3a;
  line-height: 1.5rem;
  margin-bottom: -0.5rem;
  max-width: 80%;
  
}

.title{
  font-weight: 900;
}

.button-group {
  display: flex;
  justify-content: center;
  /* gap: 20px; */
  margin-top: 30px;
}

@media (max-width: 768px) {
  .title{
    display: none;
  }

  .bottomline{
    display: none;
  }

  .tagline{
   margin: 1rem;
    font-size: 2rem;
    font-weight: 900;
    
  }

  .button-group{
    display: none;
  }

  .column{
    display: none;
  }

  .columnOne{
    width: 100%;
    padding: 0px;
  }
}


</style>
