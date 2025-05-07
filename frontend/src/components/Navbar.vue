<template>
  <nav class="navbar">

    <ul class="nav-links">
      <li><a href="/">HOME</a></li>
      <li><a href="/products">CATALOG</a></li>
      <li><a href="/cart">CONTACT</a></li>
    </ul>
    <div class="container">
      <SpinningLogo />
    </div>
    <ul class="nav-links">
      <li><a href="/">DOCS</a></li>
      <li><a href="/products">CART</a></li>
      
    </ul>
  </nav>
</template>

<script setup>
import SpinningLogo from './SpinningLogo.vue';
</script>

<style scoped>
.navbar {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0rem;
  background: transparent;
  color: white;
  position:absolute;      
  top: 0;
  left: 0;
  z-index: 1000;
}

.logo a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.2rem;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 10;
  margin-right: 20px;


}

.nav-links a {
  color: white;
  text-decoration: none;
  font-family: "Red Hat Display", sans-serif;
  font-weight: 700;
  
}

.nav-links a:hover {
  text-decoration: underline;
}
</style>
