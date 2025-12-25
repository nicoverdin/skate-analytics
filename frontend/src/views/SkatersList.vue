<template>
  <div class="p-8">
    <div class="max-w-6xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-white">Mis Patinadores</h1>
        <div class="bg-indigo-600 px-4 py-2 rounded-lg text-sm font-semibold">
          {{ skaters.length }} Registrados
        </div>
      </div>

      <div v-if="loading" class="text-center text-slate-400">Cargando datos...</div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="skater in skaters" :key="skater.id" 
          class="bg-slate-800 border border-slate-700 p-6 rounded-2xl hover:border-indigo-500 transition shadow-lg group">
          <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-bold text-white group-hover:text-indigo-400">{{ skater.name }}</h2>
            <span class="text-xs font-mono bg-slate-700 px-2 py-1 rounded text-slate-300">ID: {{ skater.id }}</span>
          </div>
          <div class="flex items-center text-indigo-300 text-sm font-medium">
            Ver detalles 
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../api/axios';

const skaters = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const response = await api.get('/api/skaters/');
    skaters.value = response.data;
  } catch (error) {
    console.error('Error cargando skaters:', error);
  } finally {
    loading.value = false;
  }
});
</script>