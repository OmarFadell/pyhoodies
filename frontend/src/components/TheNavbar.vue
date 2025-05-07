<template>

    <div class="nvbrparent">
    <belt/>
    <div class="navbar">
        <div class="child">

        <!-- <button class="burger" @click="toggleMenu">
            &#9776;
        </button> -->

        <div class="togglethemenu">
            <span v-if="!menuOpen" class="material-symbols-outlined" style="font-size: 2.5rem; margin-top: 6px; color: black;" @click="toggleMenu">
                menu
            </span>
            <span v-else style="font-size: 2.5rem; margin-top: 6px; color: black;" class="material-symbols-outlined" @click="toggleMenu">
                close
            </span>
        </div>

            <ul class="nav-links">
                <li><a href="/">HOME</a></li>
                <li><a href="/products">CATALOG</a></li>
                <li><a href="/products">COLLECTIONS</a></li>
                <li><a href="/products">FAQ</a></li>
            </ul>
                
        </div>
        <div class="child">
            <img src="../assets/bonologo.png" alt="Logo" class="logo" />
            
            
        </div>
        <div class="child">
            
            <ul class="nav-links">
               
                <li><span class="material-symbols-outlined" style="font-size: 2.5rem; font-weight: 500; color: black;">
                    shopping_cart
                </span></li>
            </ul>

            <div class="search">
                <span style="font-size: 2.5rem; margin-top: 10px;" class="material-symbols-outlined">
                    search
                </span>
            </div>
        </div>
        <div class="side-menu" :class="{ 'open': menuOpen }">
            <SideMenu v-if="menuOpen" @close="toggleMenu" />

        <!-- <button @click="closesidemenubutton">Focus Child Button</button> -->

        </div>

    </div>
</div>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import SideMenu from './SideMenu.vue';
import SpinningLogo from './SpinningLogo.vue';
import belt from '../components/belt.vue';

const childRef = ref(null);

function focusChildButton() {
   childRef.value.closesidemenubutton?.focus();
}
const menuOpen = ref(false);
const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
};

</script>


<style scoped>

.nvbrparent {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.navbar {
    display: flex;
    /* flex-direction: space-between; */
    justify-content: space-between;
    /* background-color: indigo; */
    position: relative;
    z-index: 1000;
    width: 100%;  
    padding: 0rem 0rem;
    max-height: 6.5rem;

}

.spin-fade-enter-active,
.spin-fade-leave-active {
  transition: all 0.3s ease;
  transform: rotate(360deg);
  opacity: 1;
}
.spin-fade-enter-from,
.spin-fade-leave-to {
  transform: rotate(0deg);
  opacity: 0;
}


.side-menu {
  display: none;
}

.side-menu.open {
  left: 0;
}

.side-menu ul {
  list-style: none;
  padding: 0;
  margin-top: 2rem;
  color: black;
}

.side-menu li {
  margin-bottom: 1rem;
  color: black;
}

.side-menu a {
  text-decoration: none;
  color: black;

  font-size: 1.2rem;
}
.child{
    flex: 1;
    display: flex;
    background-color: white;
    padding: 1rem 0rem;
    /* border: 1px solid black; */
    justify-content: center;
    align-items: center;
    /* max-height: 1rem; */
}


.logo{
    max-width: 6rem;
}

.nav-links{
    display: flex;
    list-style: none;
    gap: 1.5rem;
    
    
}

.nav-links a{
    color: black;
    font-weight: 900;
    font-family: "Red Hat Display", sans-serif;

}

.mob-navs{
    list-style: none;
    /* justify-content: center; */
    align-items: center;
    display: flex;
    flex-direction: column;
    font-size: 5rem;
    top: 0%;
    margin-left: 30px;
    font-family: "Red Hat Display", sans-serif;
    font-weight: 700;
    
}

.mob-navs a{
    color: black;
    text-decoration: none;
    font-family: "Red Hat Display", sans-serif;
    font-weight: 900;
    font-size: 2rem;
    text-align: center;
}

.burger {
  display: none;
  font-size: 2rem;
  cursor: pointer;
  padding: 0rem 0rem;
  background-color: none;
}


.search{
    display: none;
}

.togglethemenu{
    display: none;
}

@media (max-width: 768px) {
    /* .navbar .child:nth-child(3){
        display:none;
    } */

    .nvbrparent{
        width: 100%;
        display: flex;
        flex-direction: column;
        
    }
    .navbar{
        width: 100%;
    }

    .togglethemenu{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0rem 0rem;
    }

    .nav-links{
        display: none;
    }

    .search{
        display: block;
        color: black;
        background: none;
        border: none;    
        }


    .burger{
        display: block;
        color: black;
        background: none;
        border: none;
    }
    .side-menu {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background: white;
  z-index: 1002;
 
  transition: transform 0.3s ease-in-out;
}



}





</style>