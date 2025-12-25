<template>
  <div class="p-8">
    <div class="max-w-6xl mx-auto">
      <header class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-2">Resumen General</h1>
        <p class="text-slate-400">Panel de control de Skate Analytics.</p>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        <div class="card-skate flex flex-col justify-between h-40">
          <span class="text-slate-400 text-sm font-medium uppercase tracking-wider">Total Patinadores</span>
          <div class="flex items-end justify-between">
            <span class="text-5xl font-bold text-white">{{ loading ? '...' : totalSkaters }}</span>
            <router-link to="/skaters" class="text-brand-primary text-sm hover:underline font-semibold">Gestionar</router-link>
          </div>
        </div>

        <div class="card-skate flex flex-col justify-between h-40 opacity-70 border-dashed border-slate-600">
          <span class="text-slate-400 text-sm font-medium uppercase tracking-wider">Competiciones (v2)</span>
          <div class="flex items-end">
            <span class="text-5xl font-bold text-slate-500">0</span>
            <span class="ml-3 text-slate-500 text-xs pb-2 uppercase tracking-tighter">Próximamente</span>
          </div>
        </div>

        <div class="card-skate flex flex-col justify-between h-40">
          <span class="text-slate-400 text-sm font-medium uppercase tracking-wider">Rendimiento Medio / Elemento</span>
          <div class="flex items-end">
            <span class="text-5xl font-bold text-brand-primary">{{ loading ? '...' : averagePerformance }}</span>
          </div>
        </div>
      </div>

      <section v-if="isAdmin">
        <h2 class="text-xl font-semibold text-white mb-6">Acciones Rápidas</h2>
        <div class="flex gap-4">
          <router-link to="/results/add" class="btn-primary">
            Registrar Resultado
          </router-link>
          <router-link to="/skaters/add" class="btn-primary text-center">
            Añadir Nuevo Patinador
          </router-link>
          <router-link to="/catalog" class="btn-primary text-center">
            Gestionar Valores Elementos
          </router-link>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '../api/axios';

const totalSkaters = ref(0);
const averagePerformance = ref(0);
const loading = ref(true);
const isAdmin = localStorage.getItem('is_staff') === 'true';

onMounted(async () => {
  try {
    const [skatersRes, resultsRes] = await Promise.all([
      api.get('/api/skaters/'),
      api.get('/api/results/')
    ]);

    totalSkaters.value = skatersRes.data.length;

    if (resultsRes.data.length > 0) {
      const sum = resultsRes.data.reduce((acc, curr) => {
        return acc + parseFloat(curr.total_score || 0);
      }, 0);
      averagePerformance.value = (sum / resultsRes.data.length).toFixed(1);
    }
  } catch (error) {
    console.error("Error cargando métricas:", error);
  } finally {
    loading.value = false;
  }
});
</script>