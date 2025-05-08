<template>
    <div class="sidemenu">
        

        <ul class="mob-navs">
                <!-- <button class="close-btn" @click="menuOpen = false">×</button> -->
                <li><a href="/">HOME</a></li>
                <li><a href="/products">CATALOG</a></li>
                <li><a href="/products">COLLECTIONS</a></li>
                <li><a href="/products">RETURN POLICY</a></li>
        </ul>

        <div class="bottomactions">
            <div class="bottomchild">
                <span class="material-symbols-outlined" style="font-size: 2.5rem; font-weight: 500; color: black;" @click="$emit('close')">
                    alternate_email
                </span>
            </div>
            <div class="bottomchild"></div>
            <div class="bottomchild">
                <span class="material-symbols-outlined" style="font-size: 2.5rem; font-weight: 500; color: black;">
                    shopping_cart
                </span>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref,defineExpose} from 'vue';
defineEmits(['close']);
const closesidemenubutton = ref(null);
defineExpose({
    closesidemenubutton
});
</script>

<style scoped>

.bottomactions{
    display: flex;
    justify-content:flex-end;
    height: 9rem;
    width: 100%;  
    left: 0%;

}



.bottomchild{
    width: 100%;
    height: 35rem;
    /* background-color: #ccc; */
    justify-content: center;
    align-items: center;
    display: flex;
    


    /* border-radius: 5px; */
}

.sidemenu{

    width: 100%;    
    margin-top: 100px;

}

.minigoto{
    display: flex;
    top: 0%;
    left: 0%;
    padding: 2rem;
    width: 100%;
    /* height: 100%; */
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 9999;
    
}

.mob-navs{
    list-style: none;
    /* justify-content: center; */
    align-items: center;
    display: flex;
    flex-direction: column;
    font-size: 5rem;
    top: 0%;
    /* margin-left: -45px; */
    font-family: "Red Hat Display", sans-serif;
    font-weight: 700;
    padding: 0;
    /* height: 58vh; */
    
}

.mob-navs li {
  /* padding: 1rem; */
  border-bottom: 1px solid #ccc;
  /* margin-left: 2rem; */
  margin-right: 1rem;
  width: 80%;
  margin-top: -20px;
  
  
  
}

.mob-navs li:first-child {
  /* border-top: none; no divider above first item */
  /* width: 100%; */
}

.mob-navs a{
    color: black;
    text-decoration: none;
    font-family: "Red Hat Display", sans-serif;
    font-weight: 900;
    font-size: 2rem;
    text-align: center;
    width: 100%;
}
</style>