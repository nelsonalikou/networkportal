<template>
  <div>
    <AddPortForm @port-added="ports.push($event)" />
    <ul>
      <PortItem
        v-for="port in ports"
        :key="port.id"
        :port="port"
        @port-deleted="removePort"
      />
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../utils/api';
import AddPortForm from './AddPortForm.vue';
import PortItem from './PortItem.vue';

const ports = ref([]);

async function fetchPorts() {
  try {
    const token = localStorage.getItem('access_token');
    const response = await api.get('/ports', {
      headers: { Authorization: `Bearer ${token}` },
    });
    ports.value = response.data;
  } catch (error) {
    console.error('Erreur lors de la récupération des ports', error);
  }
}

function removePort(id) {
  ports.value = ports.value.filter((p) => p.id !== id);
}

onMounted(fetchPorts);
</script>
