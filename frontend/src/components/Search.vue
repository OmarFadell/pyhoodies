<script setup>
import { ref, watch, computed } from 'vue'
import debounce from 'lodash/debounce'
import Card from './Card.vue'
import SkelatonCard from './SkelatonCard.vue'
import { useProductStore } from '../productstore'
const store = useProductStore()
store.fetchProducts() 

const searchTerm = ref('')
const searchResults = ref([])


const productsToShow = computed(() => {
  return searchTerm.value.trim() === ''
    ? store.products
    : searchResults.value
})

const loading = ref(false)

// Debounced 
const fetchResults = debounce(async () => {
  const query = searchTerm.value.trim()
  if (!query) return

  loading.value = true
  try {
    const res = await fetch(`http://localhost:8000/api/products/?search=${query}`)
    const data = await res.json()
    searchResults.value = data
  } catch (error) {
    console.error('Search failed:', error)
  } finally {
    loading.value = false
  }
}, 400)

function onSearchInput() {
  if (searchTerm.value.trim() === '') {
    searchResults.value = []
  } else {
    fetchResults()
  }
}
</script>


<template>
    <div class="search-parent">
        <div class="search-child">
            <div class="search-bar">
                <h1>SEARCH</h1>
                <input type="text" v-model="searchTerm" @input="onSearchInput" placeholder="Search..." />

                <button class="search-button">

                    <span class="material-symbols-outlined" style="font-size: 2.5rem; font-weight: 500;">
                    search
                    </span>


                </button>
            </div>
            
        </div>
        <div class="search-results">
            <div class="keymenu">

            </div>
            <div class="results">
                <div class="product-grid" v-if="!loading">
                    <Card
                      v-for="(product, index) in searchResults"
                      :key="index"
                      :image="product.image_url"
                      :title="product.name"
                      :price="product.price"
                    />
                </div>
                <div class="product-grid" v-if="loading">
                    <SkelatonCard v-if="loading" v-for="n in 3" :key="n" />
                </div>



            </div>

        </div>
        
    </div>
    
</template>

<style scoped>
.search-parent {
  position: fixed; /* or absolute, depending on context */
  /* top: 0; */
  margin-top: 6.5rem;
  left: 0;
  width: 100vw;
  height: 50vh;
  background-color: #ffffff;
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.search-child {
  width: 100%;
  height: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border: 1px red solid;


}

.keymenu{
    border: 1px green solid;
    width: 30%;
    height: 100%;
}

.results{
    width: 100%;
    border: 1px rgb(197, 110, 11) solid;
    height: 100%;
}

.search-results {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* flex-direction: column; */
  border: 1px blue solid;
}

.search-bar h1{
    color: black;
    font-size: 1.9rem;
    font-family: 'Red Hat Display', sans-serif;
    margin-right: 1rem;
}

.search-bar {
  display: flex;
  width: 100vw;
  padding: 0 2rem; /* Optional horizontal padding */
  box-sizing: border-box;
  align-items: center;
}

.search-bar input {
  flex:auto;
  font-size: 1.2rem;
  /* padding: 1rem; */
  border: 2px solid #000000;
  border-radius: 0;
  width: 90%;
  box-sizing: border-box;
  background-color: white;
  justify-content: center;
  align-items: center;
  height: 3rem;
  color: black;
  
  
  
}

.search-button {
  padding: 1rem 2rem;
  font-size: 0.4rem;
  background: none;
  color: rgb(0, 0, 0);
  border: none;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.product-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    max-width: 1000px;
    margin-left: auto;
    justify-content: flex-start;
}

.search-button:hover {
  transform: scaleX(-1);
}

</style>