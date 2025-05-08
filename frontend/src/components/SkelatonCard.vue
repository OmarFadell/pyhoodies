<template>
    <div class="product-card">
      <div class="skeleton skeleton-image"></div>
      <div class="product-info">
        <div class="skeleton skeleton-title"></div>
        <div class="product-meta">
          <div class="skeleton skeleton-price"></div>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .product-card {
    position: relative;
    border: 1px solid #e5e5e5;
    padding: 1rem;
    width: 250px;
    background: white;
    transition: transform 0.2s;
  }
  
  .product-info {
    text-align: center;
  }
  
  .product-meta {
    display: flex;
    align-items: center;
    gap: 8px;
    justify-content: center;
    width: 100%;
  }
  
  /* Skeleton styles */
  .skeleton {
    background-color: #e0e0e0;
    border-radius: 4px;
    animation: pulse 1.5s infinite ease-in-out;
  }
  
  .skeleton-image {
    width: 100%;
    height: 15rem;
    margin-bottom: 1rem;
  }
  
  .skeleton-title {
    height: 20px;
    width: 70%;
    margin: 0 auto 0.5rem auto;
  }
  
  .skeleton-price {
    height: 15px;
    width: 40%;
  }
  
  /* Animation */
  @keyframes pulse {
    0% {
      opacity: 1;
    }
    50% {
      opacity: 0.4;
    }
    100% {
      opacity: 1;
    }
  }
  
  @media (max-width: 768px) {
    .product-card {
      width: 100%;
      height: 50vh;
      display: flex;
      flex-direction: column;
    }
  
    .skeleton-image {
      height: 20rem;
    }
  }
  </style>
  