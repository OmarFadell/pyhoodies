<template>
    <section class="hero-section">
      <video class="bg-video" autoplay muted loop playsinline>
        <source :src="heroVideo" type="video/mp4" />
      </video>
      <div class="overlay"></div>
  
      <div class="hero-content">
        <p class="tagline">DRIP SO HARD, THEY CAN'T LOOK AWAY.</p>
        <h1 class="hero-title">
          STEP UP YOUR STYLE<br />
          WITH OUR <span class="highlight">EXCLUSIVE</span><br />
          DROP
        </h1>
        <button class="cta-button">GO TO SHOP →</button>
      </div>
    </section>
  </template>
  
  <script setup>
  import heroVideo from '../assets/pablo.mp4' // replace with your file
  </script>
  
  <style scoped>
  .hero-section {
    position: relative;
    width: 100vw;
    height: 94.5vh;
    overflow: hidden;
    margin-top: -10vh;
    
  }
  
  .bg-video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100vh;
    min-height: 100%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    z-index: -2;
  }
  
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3));
    z-index: -1;
  }
  
  .hero-content {
    position: absolute;
    left: 5%;
    top: 55%;
    color: white;
    max-width: 650px;
    font-family: 'Red Hat Display', sans-serif;
    align-items: flex-start;
  }
  
  .tagline {
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: -2rem;
    color: #ccc;
    text-transform: uppercase;
    text-align: left;
  }
  
  .hero-title {
    font-size: 3.5rem;
    font-weight: 900;
    line-height: 0.9;
    text-align: left;
  }
  
  .hero-title .highlight {
    background: linear-gradient(to right, #0c3e94, #755faa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-style: italic;
    font-weight: 900;
    
  }
  
  .cta-button {
  padding: 16px 32px;
  font-size: 1.1rem;
  font-weight: 700;
  background-color: #3f55ff;
  color: white;
  border: none;
  border-radius: 35px;
  cursor: pointer;
  transition: background 0.3s ease;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
  margin-left: -20rem;
}
  
  .cta-button:hover {
    background-color: #757a9c;
  }

  @media (max-width: 768px) {

    .hero-section{
      height: 95vh;
    }
    .hero-content {
      left: 10%;
      top: 55%;
    }
    .hero-title {
      font-size: 2.5rem;
    }
    .tagline {
      font-size: 0.7rem;
    }
    .cta-button {
      
      padding: 12px 100px;
      font-size: 1rem;
      margin-left: -60px;
    }
    
    
  }
  </style>
  