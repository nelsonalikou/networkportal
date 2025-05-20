<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue';
</script>

<style>
/* Global styles can go here */
body {
  font-family: 'Inter', sans-serif;
  background-color: #f9fafb;
  margin: 0;
}
</style>
