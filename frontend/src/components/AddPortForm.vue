<template>
  <form @submit.prevent="addPort" class="mb-6 p-4 border rounded shadow-sm bg-gray-50">
    <h3 class="text-lg font-semibold mb-2">Ajouter un port</h3>
    <input
      type="text"
      v-model="newPort.name"
      placeholder="Nom du port"
      class="w-full mb-2 p-2 border rounded"
      required
    />
    <input
      type="text"
      v-model="newPort.description"
      placeholder="Statut"
      class="w-full mb-2 p-2 border rounded"
      required
    />
    <button
      type="submit"
      class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
    >
      Ajouter
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue';
import api from '../utils/api';

const emit = defineEmits(['port-added']);

const newPort = ref({ name: '', description: '' });

async function addPort() {
  try {
    const token = localStorage.getItem('access_token');
    const response = await api.post('/ports', newPort.value, {
      headers: { Authorization: `Bearer ${token}` },
    });

    emit('port-added', response.data);
    newPort.value.name = '';
    newPort.value.description = '';
  } catch (error) {
    console.error('Erreur lors de l’ajout du port', error);
  }
}
</script>
