<template>
  <nav class="bg-green-600 text-white px-6 py-4 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <ul class="flex space-x-6 text-lg font-medium">
        <li>
          <router-link to="/" class="hover:underline">Accueil</router-link>
        </li>
        <li>
          <router-link to="/ports" class="hover:underline">Ports</router-link>
        </li>
      </ul>
      <div v-if="isAuthenticated">
        <button
          @click="logout"
          class="bg-red-500 hover:bg-red-600 transition-colors px-4 py-2 rounded-lg font-semibold shadow"
        >
          Déconnexion
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { isAuthenticated, logout } from '../utils/auth';
</script>

<style scoped>
</style>
