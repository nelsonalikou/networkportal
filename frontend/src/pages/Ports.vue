<template>
  <section class="min-h-screen bg-green-50 py-16 px-4">
    <div class="max-w-5xl mx-auto bg-white rounded-2xl shadow-xl p-10">
      <h2 class="text-3xl font-extrabold text-green-700 text-center mb-10">📦 Liste des Ports</h2>
      <PortList />
    </div>
  </section>
</template>

<script setup>
import PortList from '../components/PortList.vue';
</script>

<style scoped>
</style>
