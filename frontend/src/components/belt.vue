<template>
    <div class="promo-belt">
      <div class="scroll-text">
        <span v-for="n in 20" :key="n">
          * 25% OFF <span class="highlight">ENDS</span> TOMORROW&nbsp;&nbsp;
        </span>
      </div>
    </div>
  </template>
  
  <style scoped>
  .promo-belt {
    width: 100vw;
    background-color: #0e34c9; /* vivid blue background */
    overflow: hidden;
    white-space: nowrap;
    height: 40px;
    display: flex;
    align-items: center;
  }
  
  .scroll-text {
    display: inline-block;
    animation: scroll-left 35s linear infinite;
    font-weight: 700;
    color: white;
    font-size: 1.2rem;
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
  </style>
  