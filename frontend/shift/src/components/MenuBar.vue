<template>
    <div @click="toggleMenu" class="hamburger-menu">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      toggleMenu() {
        this.$emit('toggle-menu');
      }
    }
  }
  </script>
  
  <style scoped>
  .hamburger-menu {
    width: 30px;
    height: 25px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
  }
  
  .bar {
    width: 100%;
    height: 4px;
    background-color: #333;
  }
  </style>