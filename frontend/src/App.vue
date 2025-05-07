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
    padding-top: 0rem;
    padding: 0rem 0rem;
  }
  </style>
  
