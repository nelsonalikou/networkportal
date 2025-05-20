<template>
  <li class="flex justify-between items-center border-b py-2">
    <span class="text-success">{{ port.name }} - {{ port.status }}</span>
    <button
      @click="deletePort"
      class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600 text-sm"
    >
      Supprimer
    </button>
  </li>
</template>

<script setup>
import api from '../utils/api';

const props = defineProps({
  port: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['port-deleted']);

async function deletePort() {
  try {
    const token = localStorage.getItem('access_token');
    await api.delete(`/ports/${props.port.id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    emit('port-deleted', props.port.id);
  } catch (error) {
    console.error('Erreur lors de la suppression du port', error);
  }
}
</script>

<style scoped>
.text-success {
  color: green;
}
</style>
