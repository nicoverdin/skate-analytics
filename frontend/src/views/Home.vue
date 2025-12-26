<template>
  <div class="p-4 md:p-8 min-h-screen pb-20">
    <div class="max-w-6xl mx-auto">
      
      <header class="mb-8 md:mb-12">
        <h1 class="text-3xl md:text-4xl font-bold text-white mb-1 md:mb-2">Resumen General</h1>
        <p class="text-slate-400 text-sm md:text-base">Panel de control de Skate Analytics.</p>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6 mb-8 md:mb-12">
        
        <div v-if="isAdmin" class="card-skate group relative flex flex-col justify-between h-36 md:h-40 overflow-hidden">
          <div class="absolute -right-2 -top-2 text-brand-primary/10 transition-transform group-hover:rotate-12 group-hover:scale-110">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24 md:h-28 md:w-28" fill="currentColor" viewBox="0 0 24 24">
              <path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/>
            </svg>
          </div>

          <div class="relative z-10">
            <span class="text-slate-500 text-[10px] md:text-xs font-bold uppercase tracking-widest">Base de Datos</span>
            <h3 class="text-slate-400 text-xs md:text-sm font-medium mt-1">Total Patinadores Activos</h3>
          </div>

          <div class="relative z-10 flex items-end justify-between">
            <div class="flex items-baseline gap-2">
              <span v-if="loading" class="text-4xl md:text-5xl font-bold text-slate-700 animate-pulse">...</span>
              <span v-else class="text-4xl md:text-5xl font-black text-white tracking-tighter">
                {{ totalSkaters }}
              </span>
              <span class="text-slate-500 text-[10px] md:text-xs font-bold uppercase">Atletas</span>
            </div>

            <router-link 
              to="/skaters" 
              class="flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 hover:bg-brand-primary text-slate-300 hover:text-bg-main rounded-lg text-xs font-bold transition-all duration-300 border border-slate-700 hover:border-brand-primary"
            >
              Gestionar
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
              </svg>
            </router-link>
          </div>
        </div>

        <div v-if="!isAdmin" class="card-skate group relative flex flex-col justify-between h-36 md:h-40 overflow-hidden">
          <div class="absolute -right-4 -top-4 text-brand-primary/10 transition-transform group-hover:scale-110 group-hover:rotate-12">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-28 w-28 md:h-32 md:w-32" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/>
            </svg>
          </div>

          <div class="relative z-10">
            <span class="text-slate-500 text-[10px] md:text-xs font-bold uppercase tracking-widest">Tu Rendimiento</span>
            <h3 class="text-lg md:text-xl font-bold text-white mt-1">Mi Panel Técnico</h3>
          </div>

          <div class="relative z-10 flex items-center justify-between">
            <div v-if="loading" class="h-6 w-24 bg-slate-700 animate-pulse rounded"></div>
            
            <router-link 
              v-else-if="selfId"
              :to="`/skaters/${selfId}`" 
              class="flex items-center gap-2 bg-brand-primary/10 hover:bg-brand-primary text-brand-primary hover:text-bg-main px-3 py-1.5 md:px-4 md:py-2 rounded-lg text-xs md:text-sm font-bold transition-all duration-300"
            >
              Ver Análisis
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 md:h-4 md:w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </router-link>

            <span v-else class="text-slate-500 text-xs italic">Perfil no vinculado</span>
          </div>
        </div>

        <div class="card-skate flex flex-col justify-between h-36 md:h-40 opacity-70 border-dashed border-slate-600">
          <span class="text-slate-400 text-xs md:text-sm font-medium uppercase tracking-wider">Competiciones (v2)</span>
          <div class="flex items-end">
            <span class="text-4xl md:text-5xl font-bold text-slate-500">0</span>
            <span class="ml-3 text-slate-500 text-[10px] md:text-xs pb-2 uppercase tracking-tighter">Próximamente</span>
          </div>
        </div>

        <div class="card-skate group relative flex flex-col justify-between h-36 md:h-40 overflow-hidden">
          <div class="absolute -right-2 -bottom-2 text-brand-primary/5 transition-transform group-hover:scale-110">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 md:h-24 md:w-24" fill="currentColor" viewBox="0 0 24 24">
              <path d="M4 9h4v11H4zm12 4h4v7h-4zm-6-9h4v16h-4z"/>
            </svg>
          </div>

          <div class="relative z-10">
            <div class="flex items-center gap-2">
              <div class="h-1.5 w-1.5 md:h-2 md:w-2 rounded-full bg-brand-primary animate-pulse"></div>
              <span class="text-slate-500 text-[10px] md:text-xs font-bold uppercase tracking-widest">Métrica Global</span>
            </div>
            <h3 class="text-slate-400 text-xs md:text-sm font-medium mt-1">Rendimiento Medio / Elemento</h3>
          </div>

          <div class="relative z-10">
            <div class="flex items-baseline gap-2">
              <span v-if="loading" class="text-4xl md:text-5xl font-bold text-slate-700 animate-pulse">...</span>
              <span v-else class="text-4xl md:text-5xl font-black text-brand-primary tracking-tighter tabular-nums">
                {{ averagePerformance }}
              </span>
              <span class="text-slate-500 text-xs md:text-sm font-bold">PTS</span>
            </div>
            
            <div class="mt-3 w-full bg-slate-800 rounded-full h-1 md:h-1.5 overflow-hidden">
              <div 
                class="bg-brand-primary h-full transition-all duration-1000 ease-out"
                :style="{ width: `${(averagePerformance / 10) * 100}%` }"
              ></div>
            </div>
          </div>
        </div>
      </div>

      <section v-if="isAdmin" class="mt-8 md:mt-12">
        <div class="flex items-center gap-3 mb-6 md:mb-8">
          <div class="h-6 w-1 md:h-8 bg-brand-primary rounded-full"></div>
          <h2 class="text-xl md:text-2xl font-bold text-white tracking-tight">Acciones de Gestión</h2>
        </div>

        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 md:gap-4">
          
          <router-link to="/results/add" class="group bg-bg-card border border-border-soft p-4 md:p-5 rounded-2xl hover:border-brand-primary transition-all duration-300 shadow-sm hover:shadow-brand-primary/10">
            <div class="bg-slate-800 w-10 h-10 md:w-12 md:h-12 rounded-xl flex items-center justify-center mb-3 md:mb-4 group-hover:bg-brand-primary group-hover:text-bg-main transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
              </svg>
            </div>
            <h3 class="text-white text-sm md:text-base font-bold mb-1">Registrar</h3> <p class="text-slate-500 text-[10px] md:text-xs">Añadir puntuaciones.</p>
          </router-link>

          <router-link to="/results" class="group bg-bg-card border border-border-soft p-4 md:p-5 rounded-2xl hover:border-brand-primary transition-all duration-300 shadow-sm hover:shadow-brand-primary/10">
            <div class="bg-slate-800 w-10 h-10 md:w-12 md:h-12 rounded-xl flex items-center justify-center mb-3 md:mb-4 group-hover:bg-brand-primary group-hover:text-bg-main transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h3 class="text-white text-sm md:text-base font-bold mb-1">Historial</h3>
            <p class="text-slate-500 text-[10px] md:text-xs">Ver registros.</p>
          </router-link>

          <router-link to="/skaters/add" class="group bg-bg-card border border-border-soft p-4 md:p-5 rounded-2xl hover:border-brand-primary transition-all duration-300 shadow-sm hover:shadow-brand-primary/10">
            <div class="bg-slate-800 w-10 h-10 md:w-12 md:h-12 rounded-xl flex items-center justify-center mb-3 md:mb-4 group-hover:bg-brand-primary group-hover:text-bg-main transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
              </svg>
            </div>
            <h3 class="text-white text-sm md:text-base font-bold mb-1">Patinadores</h3>
            <p class="text-slate-500 text-[10px] md:text-xs">Crear perfiles.</p>
          </router-link>

          <router-link to="/catalog" class="group bg-bg-card border border-border-soft p-4 md:p-5 rounded-2xl hover:border-brand-primary transition-all duration-300 shadow-sm hover:shadow-brand-primary/10">
            <div class="bg-slate-800 w-10 h-10 md:w-12 md:h-12 rounded-xl flex items-center justify-center mb-3 md:mb-4 group-hover:bg-brand-primary group-hover:text-bg-main transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <h3 class="text-white text-sm md:text-base font-bold mb-1">Catálogo</h3>
            <p class="text-slate-500 text-[10px] md:text-xs">Valores SOV.</p>
          </router-link>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../api/axios';

// La lógica es IDÉNTICA a la que ya tenías, funciona perfecto.
const totalSkaters = ref(0);
const averagePerformance = ref(0);
const loading = ref(true);
const isAdmin = localStorage.getItem('is_staff') === 'true';
const selfId = ref(null);

const getUserIdFromToken = (token) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload).user_id;
  } catch (e) {
    return null;
  }
};

onMounted(async () => {
  try {
    const token = localStorage.getItem('access_token');
    const currentUserId = token ? getUserIdFromToken(token) : null;

    const [skatersRes, resultsRes] = await Promise.all([
      api.get('/api/skaters/'),
      api.get('/api/results/')
    ]);

    totalSkaters.value = skatersRes.data.length;

    if (!isAdmin && currentUserId) {
      const myProfile = skatersRes.data.find(s => String(s.user) === String(currentUserId));
      if (myProfile) {
        selfId.value = myProfile.id;
        console.log("Perfil encontrado. Skater ID:", selfId.value);
      }
    }

    if (resultsRes.data.length > 0) {
      const sum = resultsRes.data.reduce((acc, curr) => acc + parseFloat(curr.total_score || 0), 0);
      averagePerformance.value = (sum / resultsRes.data.length).toFixed(1);
    }
  } catch (error) {
    console.error("Error:", error);
  } finally {
    loading.value = false;
  }
});
</script>