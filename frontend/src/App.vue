<script setup>
import TheNavbar from './components/TheNavbar.vue'; // Keep your navbar
import Footer from './components/Footer.vue';
</script>

<template>
    <TheNavbar/>
    <main class="page-content">
      <router-view />
    </main>
    <Footer/>
  </template>
  
  <style>
  .page-content {
  width: 100vw;
  padding-top: 1.5rem;
  margin: 0;
}
  </style>
  
