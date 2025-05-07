<template>
    <div class="logo-containter">
        <img src="../assets/pylogo.png" alt="Logo" class="logo" />
    </div>
</template>

<style scoped>
.logo-containter {
    width: 150px;
    height: 50px;
    /* perspective: 1000px; */
}

.logo{
    width:100%;
    height: auto;
    animation: spinY 4s linear infinite;
    transform-style: preserve-3d;
}


/* Keyframes for horizontal spin */
@keyframes spinY {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(360deg);
  }
}
</style>