<template>
  <div class="p-8">
    <div class="max-w-6xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-white">Mis Patinadores</h1>
        <router-link v-if="isAdmin" to="/skaters/add" class="btn-primary text-sm px-4">
          + Añadir
        </router-link>
        <div class="bg-brand-primary px-4 py-2 rounded-lg text-sm font-semibold text-black">
          {{ skaters.length }} Registrados
        </div>
      </div>

      <div v-if="loading" class="text-center text-slate-400 font-medium">
        Cargando patinadores...
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="skater in skaters" :key="skater.id" class="card-skate group">
          <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-bold text-white group-hover:text-brand-primary transition-colors">
              {{ skater.name }}
            </h2>
            <span class="text-xs font-mono bg-bg-input px-2 py-1 rounded text-slate-300">
              ID: {{ skater.id }}
            </span>
          </div>
          
          <p class="text-slate-400 text-sm mb-4">Puntuación media: --</p>

          <div class="flex items-center text-brand-primary text-sm font-semibold">
            Ver estadísticas completo
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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
const isAdmin = localStorage.getItem('is_staff') === 'true';

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