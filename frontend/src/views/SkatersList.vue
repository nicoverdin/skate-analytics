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

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="skater in skaters" :key="skater.id" 
            class="card-skate group relative overflow-hidden flex flex-col justify-between hover:bg-slate-800/50 transition-all duration-300">
          
          <div class="absolute -right-4 -top-4 w-24 h-24 bg-brand-primary/5 rounded-full blur-2xl group-hover:bg-brand-primary/10 transition-colors"></div>

          <div class="relative z-10">
            <div class="flex items-center gap-4 mb-5">
              <div class="h-12 w-12 rounded-full bg-slate-800 border border-border-soft flex items-center justify-center text-brand-primary font-bold shadow-inner group-hover:border-brand-primary/50 transition-colors">
                {{ skater.name.charAt(0).toUpperCase() }}
              </div>
              
              <div class="flex-1">
                <h2 class="text-lg font-bold text-white group-hover:text-brand-primary transition-colors truncate">
                  {{ skater.name }}
                </h2>
              </div>
            </div>

            <div class="bg-bg-main/50 rounded-xl p-3 border border-border-soft/50 mb-6">
              <div class="flex justify-between items-end">
                <span class="text-xs text-slate-500 font-semibold uppercase">Puntuación Media</span>
                <span class="text-xl font-mono font-bold text-white">
                  {{ skater.average_score > 0 ? skater.average_score.toFixed(2) : '--' }}
                </span>
              </div>
              <div class="w-full bg-slate-800 h-1 mt-2 rounded-full overflow-hidden">
                <div class="bg-brand-primary h-full rounded-full transition-all duration-500"
                    :style="{ width: skater.average_score > 0 ? `${(skater.average_score / 10) * 100}%` : '0%' }">
                </div>
              </div>
            </div>
          </div>

          <router-link 
            :to="`/skaters/${skater.id}`" 
            class="relative z-10 flex items-center justify-center w-full py-2.5 bg-slate-800 group-hover:bg-brand-primary rounded-lg text-slate-300 group-hover:text-bg-main text-xs font-black uppercase tracking-tighter transition-all duration-300 border border-slate-700 group-hover:border-brand-primary shadow-sm"
          >
            Análisis Estadístico
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-2 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </router-link>
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