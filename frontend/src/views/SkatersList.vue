<template>
  <div class="p-4 md:p-8 min-h-screen text-white pb-20">
    <div class="max-w-6xl mx-auto">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6 md:mb-8">
        <div>
          <h1 class="text-2xl md:text-3xl font-bold text-white flex items-center gap-2">
            Mis Patinadores
            <span class="md:hidden text-xs bg-slate-800 text-brand-primary px-2 py-0.5 rounded-full border border-white/10 font-mono">
              {{ skaters.length }}
            </span>
          </h1>
          <p class="text-slate-500 text-xs md:text-sm mt-1">Gestión de atletas y rendimiento</p>
        </div>

        <div class="flex items-center gap-3 w-full md:w-auto">
          <div class="hidden md:block bg-brand-primary px-4 py-2 rounded-lg text-sm font-semibold text-black">
            {{ skaters.length }} Registrados
          </div>
          
          <button 
            v-if="isAdmin" 
            @click="navigate('/skaters/add')" 
            class="btn-primary text-sm px-6 py-3 md:py-2.5 flex-1 md:flex-none text-center justify-center flex items-center gap-2 shadow-lg shadow-brand-primary/20 active:scale-95 transition-transform"
          >
            <span class="text-lg leading-none font-bold">+</span> Añadir Nuevo
          </button>
        </div>
      </div>

      <div v-if="loading" class="text-center py-12 text-slate-400 font-medium flex flex-col items-center gap-3 animate-pulse">
        <div class="h-8 w-8 rounded-full border-2 border-slate-600 border-t-brand-primary animate-spin"></div>
        Cargando equipo...
      </div>

      <template v-else>
        
        <div class="md:hidden space-y-3">
          <div 
            v-for="skater in skaters" 
            :key="`mob-${skater.id}`"
            @click="goToSkater(skater.id)"
            class="block bg-slate-800 border border-white/5 rounded-2xl p-4 active:scale-[0.98] transition-all cursor-pointer shadow-sm relative overflow-hidden group"
          >
            <div class="absolute left-0 top-0 bottom-0 w-1 bg-brand-primary/50"></div>

            <div class="flex items-center justify-between pl-2">
              <div class="flex items-center gap-3">
                <div class="h-10 w-10 rounded-full bg-slate-700/50 flex items-center justify-center text-brand-primary font-black text-sm border border-white/10 shadow-inner">
                  {{ skater.name.charAt(0).toUpperCase() }}
                </div>
                <div>
                  <h3 class="font-bold text-white text-base leading-tight">{{ skater.name }}</h3>
                  <p class="text-[10px] text-brand-primary uppercase tracking-wider font-bold mt-0.5 flex items-center gap-1">
                    Ver Análisis
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" /></svg>
                  </p>
                </div>
              </div>

              <div class="text-right">
                <span class="block text-2xl font-black text-white tracking-tighter tabular-nums">
                  {{ skater.average_score > 0 ? skater.average_score.toFixed(2) : '--' }}
                </span>
                <span class="text-[9px] text-slate-500 uppercase font-bold">Media Pts</span>
              </div>
            </div>
          </div>
        </div>

        <div class="hidden md:grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="skater in skaters" :key="skater.id" 
              class="card-skate group relative overflow-hidden flex flex-col justify-between hover:bg-slate-800/80 hover:border-brand-primary/30 transition-all duration-300 shadow-lg hover:shadow-brand-primary/5">
            
            <div class="absolute -right-4 -top-4 w-24 h-24 bg-brand-primary/5 rounded-full blur-2xl group-hover:bg-brand-primary/10 transition-colors"></div>

            <div class="relative z-10">
              <div class="flex items-center gap-4 mb-5">
                <div class="h-12 w-12 rounded-full bg-slate-800 border border-border-soft flex items-center justify-center text-brand-primary font-bold shadow-inner group-hover:border-brand-primary/50 transition-colors group-hover:scale-110 duration-300">
                  {{ skater.name.charAt(0).toUpperCase() }}
                </div>
                
                <div class="flex-1 min-w-0">
                  <h2 class="text-lg font-bold text-white group-hover:text-brand-primary transition-colors truncate">
                    {{ skater.name }}
                  </h2>
                  <p class="text-xs text-slate-500 truncate">Perfil de atleta</p>
                </div>
              </div>

              <div class="bg-bg-main/50 rounded-xl p-3 border border-border-soft/50 mb-6 group-hover:border-white/10 transition-colors">
                <div class="flex justify-between items-end">
                  <span class="text-xs text-slate-500 font-semibold uppercase tracking-wider">Puntuación Media</span>
                  <span class="text-xl font-mono font-bold text-white">
                    {{ skater.average_score > 0 ? skater.average_score.toFixed(2) : '--' }}
                  </span>
                </div>
                <div class="w-full bg-slate-800 h-1 mt-2 rounded-full overflow-hidden">
                  <div class="bg-brand-primary h-full rounded-full transition-all duration-1000 ease-out"
                      :style="{ width: skater.average_score > 0 ? `${(skater.average_score / 10) * 100}%` : '0%' }">
                  </div>
                </div>
              </div>
            </div>

            <button 
              @click="goToSkater(skater.id)" 
              class="relative z-10 flex items-center justify-center w-full py-3 bg-slate-800 group-hover:bg-brand-primary rounded-xl text-slate-300 group-hover:text-bg-main text-xs font-black uppercase tracking-widest transition-all duration-300 border border-slate-700 group-hover:border-brand-primary shadow-sm cursor-pointer"
            >
              Análisis Estadístico
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-2 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </button>
          </div>
        </div>

      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '../api/axios';

const skaters = ref([]);
const loading = ref(true);
const isAdmin = localStorage.getItem('is_staff') === 'true';
const router = useRouter();

const navigate = (path) => {
  router.push(path);
};

const goToSkater = (id) => {
  router.push(`/skaters/${id}`);
};

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