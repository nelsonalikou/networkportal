<template>
  <section class="min-h-screen bg-gradient-to-b from-green-50 to-green-100 flex items-center justify-center">
    <div class="text-center p-8 bg-white rounded-2xl shadow-xl max-w-xl w-full">
      <h1 class="text-5xl font-extrabold text-green-700 mb-4">🌐 Network Portal</h1>
      <p class="text-lg text-gray-700 mb-6">Bienvenue sur le portail réseau. Accédez aux informations essentielles de manière rapide et sécurisée.</p>
      
      <router-link
        to="/ports"
        class="bg-green-600 hover:bg-green-700 transition text-white px-8 py-3 rounded-full text-lg shadow-md"
      >
        Voir les ports
      </router-link>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
</style>

