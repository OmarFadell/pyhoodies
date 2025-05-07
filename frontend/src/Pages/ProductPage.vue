<template>
    <div class="prodpage">
    <div class="prodparent">
        <div class="prodimage">
            <img src="../assets/model.png" alt="Product Image" style="width: 100%; height: 100%; object-fit:contain;">
        </div>
        <div class="prodinfo">

            <h1>Recycling Everything about you tee</h1>
            <h2>DROP 002</h2>
            <p>who's calling my phone? who's calling that shit?</p>
            
            <div class="color-picker">
                <div
                 v-for="(color,index) in colors"
                 :key="index"
                 class="color-circle"
                 :style="{ backgroundColor: color, border: selectedColor == color ? '3px solid black':'1px solid #ccc' }"
                 @click="selectColor(color)"></div>

            </div>

            <Counter/>
            <button class="cta-button-group">Add to Cart</button>

            <!-- <ul>
                <li>Price: 240</li>
                <li>Size: M</li>
                <li>Color: Black</li>
                <li>Material: Cotton</li>
                <li>Care Instructions: Machine wash cold, tumble dry low</li>
                <li>Shipping: Free shipping on orders over €50</li>
                <li>Returns: 30-day return policy</li>
            </ul> -->
            
           

        </div>
        <!-- <div class="prodshow"></div> -->

            
    </div>
    <div class="dropname">
        <div class="promo-belt">
      <div class="scroll-text">
        <span v-for="n in 20" :key="n">
         DREIPEDALE DROP 002 © 
        </span>
      </div>
    </div>
        
    </div>
    <div class="pov">
        <h1>CHECK THIS OUT TOO.</h1>
        <Carousel v-bind="carouselConfig">
    <Slide v-for="slide in 10" :key="slide">
      <div class="carousel__item"><AnothCard
  :image="'../src/assets/shirt.png'"
  :title="'Mas Que Nada'"
  :price="199.99"
  :isNew="true"
  :isFavorited="false"
  @toggle-favorite="handleFavoriteToggle"
/></div>
    </Slide>

    <template #addons>
      <Navigation />
      <Pagination />
    </template>
  </Carousel>
    
        
    </div>
</div>
</template>

<script setup>
import 'vue3-carousel/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import { ref } from 'vue';
import Counter from '../components/Counter.vue';
const colors = ['red', 'blue', 'green', 'yellow', 'purple'];
import AnothCard from '../components/AnothCard.vue';

const carouselConfig = {
  wrapAround: true,
  breakpoints: {
    0: {
      itemsToShow: 1
    },
    768: {
      itemsToShow: 2
    },
    1024: {
      itemsToShow: 5
    }
  }
}
function handleFavoriteToggle() {
  console.log('Favorite toggled!')
}
const selectedColor = ref(null);


function selectColor(color) {
    selectedColor.value = color;
    console.log('Selected color:', color);
}
</script>

<style scoped>




.color-picker {
  display: flex;
  gap: 1rem;
  margin: 1rem 0;
}

.color-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  transition: border 0.2s ease;
}

.prodparent{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
    margin: 0 auto;
    width: 100%;
    color: black;
    height: 100vh;
    margin-bottom: 4rem;
}


.prodinfo{
/* border: 1px solid red; */
width: 100%;
height: 100vh;
display: flex;
flex-direction: column;
justify-content: center;   /* horizontally center */
align-items: center;       /* vertically center */
text-align: center;


}

.prodinfo h1{
    font-family: "Red Hat Display", sans-serif;
    color: #3a3a3a;
    font-weight: 900;
    margin: 1rem 10rem;
}

.prodinfo ul{
    list-style: none;
    padding: 0;
    margin: 0;
    font-family: "Red Hat Display", sans-serif;
    color: #3a3a3a;
    font-weight: 500;
    text-align: left;
}

.prodimage{
    /* border: 1px solid green; */
    width: 75%;
    height: 100vh;
}

.cta-button-group{
    margin-left: 25px ;
    margin-top: 3rem; 
    padding: 0.8rem 5rem;
}

.dropname{
    color: black;
    padding: 0rem 0rem;
    margin: 0rem 0rem;
    font-size: 5rem;
    height: 20vh;
    /* background-color: red; */
    width: 100%;
    display: flex;
    flex-direction: column;
}

.promo-belt {
    width: 100vw;
    /* background-color: #0e34c9; */
    overflow: hidden;
    white-space: nowrap;
    height: 60vh;
    display: flex;
    align-items: center;
  }
  
  .scroll-text {
    display: inline-block;
    animation: scroll-left 300s linear infinite;
    font-weight: 900;
    color: black;
    font-size: 16rem;
    text-transform: uppercase;
    padding-left: 100%;
    font-family: "Red Hat Display", sans-serif;
    
    

  }

  .highlight {
    color: #ffcc00; /* bright yellow */
    font-weight: 900;
  } 
  
  @keyframes scroll-left {
    0% {
      transform: translateX(0%);
    }
    100% {
      transform: translateX(-100%);
    }
  }

  .pov{
    height: 100vh;
    /* border: 1px violet solid; */
    width: 100%;
    color: black;
    font-family: "Red Hat Display", sans-serif;
    


  }

  .pov h1{
    font-weight: 900;
    text-align: left;
  }

@media (max-width: 768px) {

    .cta-button-group{
        
    margin-left: 25px;
    margin-top: 1rem;
    margin-bottom: 1rem; 
    padding: 0.8rem 5rem;
    }
    .prodparent{
        margin-top: 2rem;
        flex-direction: column;
        width: 100%;
        height: 100vh;
        line-height: 1rem;
    }
    .prodimage{
        width: 100%;
        height: 50vh;
    }
    .prodinfo{
        width: 100%;
        /* height: 50vh; */
    }
}
</style>