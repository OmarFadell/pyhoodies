import {defineStore} from 'pinia';
import {ref} from 'vue';
import axios from 'axios';

export const useProductStore = defineStore('product', () => {
    const products = ref([]);
    const loading = ref(false);

    async function fetchProducts() {
        if (products.value.length > 0) return // already loaded
        loading.value = true
        const res = await axios.get('http://localhost:8000/api/products/')
        products.value = res.data
        loading.value = false
    }

  return { products, loading, fetchProducts }
})