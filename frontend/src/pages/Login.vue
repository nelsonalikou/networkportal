<template>
  <section class="min-h-screen flex items-center justify-center bg-green-50 px-4">
    <div class="w-full max-w-md p-10 bg-white rounded-2xl shadow-2xl">
      <h2 class="text-3xl font-bold text-green-700 text-center mb-6">🔐 Connexion</h2>
      <LoginForm />
    </div>
  </section>
</template>

<script setup>
import LoginForm from '../components/LoginForm.vue';
</script>

<style scoped>
</style>
