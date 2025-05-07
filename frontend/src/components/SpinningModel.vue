<!-- SpinningModel.vue -->
<template>
    <canvas ref="canvas" class="three-canvas"></canvas>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import * as THREE from 'three'
  import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
  
  const canvas = ref(null)
  
  onMounted(() => {
    const scene = new THREE.Scene()
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    const renderer = new THREE.WebGLRenderer({ canvas: canvas.value, alpha: true })
    renderer.setSize(window.innerWidth, window.innerHeight)
  
    const light = new THREE.DirectionalLight(0xffffff, 1)
    light.position.set(5, 5, 5)
    scene.add(light)
  
    const loader = new GLTFLoader()
    loader.load('/models/my-logo.gltf', (gltf) => {
      const model = gltf.scene
      model.scale.set(1, 1, 1)
      scene.add(model)
  
      camera.position.z = 3
  
      const animate = function () {
        requestAnimationFrame(animate)
        model.rotation.y += 0.01
        renderer.render(scene, camera)
      }
      animate()
    })
  })
  </script>
  
  <style>
  .three-canvas {
    width: 100vw;
    height: 100vh;
    display: block;
  }
  </style>
  