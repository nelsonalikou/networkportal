<template>
  <form @submit.prevent="login" class="space-y-4">
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1" for="email">Email</label>
      <input
        id="email"
        type="email"
        placeholder="Votre email"
        v-model="email"
        class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
        required
      />
    </div>

    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1" for="password">Mot de passe</label>
      <input
        id="password"
        type="password"
        placeholder="Votre mot de passe"
        v-model="password"
        class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
        required
      />
    </div>

    <button
      type="submit"
      class="w-full bg-green-600 hover:bg-green-700 transition-colors text-white py-3 rounded-lg font-semibold shadow"
    >
      Se connecter
    </button>

    <p v-if="errorMessage" class="text-red-500 mt-3 text-sm text-center">
      {{ errorMessage }}
    </p>
  </form>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '../utils/api';

const email = ref('');
const password = ref('');
const errorMessage = ref('');
const router = useRouter();

async function login() {
  try {
    const formData = new FormData();
    formData.append('username', email.value);  // OAuth2 spec
    formData.append('password', password.value);

    const response = await api.post('/users/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });

    const { access_token } = response.data;
    localStorage.setItem('access_token', access_token);
    router.push('/ports');
  } catch (error) {
    errorMessage.value = 'Email ou mot de passe incorrect';
  }
}
</script>

<style scoped>
</style>
