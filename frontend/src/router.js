import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './Pages/HomePage.vue';
import ProductPage from './Pages/ProductPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/product', component: ProductPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
